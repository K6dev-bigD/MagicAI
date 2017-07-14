import sys
import traceback

_author_ = 'kundan kumar'

import re
import tweepy

from tweepy import OAuthHandler
from textblob import TextBlob
from Utilities.CustomExceptions import EmptyObjectException, TypeMismatchException, EmptyTweetsException, TweetException
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class TwitterApiClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    sid = SentimentIntensityAnalyzer()

    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        '''
        Class constructor or initialization method.
        '''
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)

        except :
            print("[Internal API ERROR][Authentication]: Authentication Failed")



    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())


    def __get_tweet_sentiment(self, tweet=""):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_text_polarity_using_textblob(self, tweet):
        '''
            This module uses textblob python package for sentiment analysis
            please check this link for more info :
            https://textblob.readthedocs.io/en/dev/
        '''
        analysis = TextBlob(self.clean_tweet(tweet))
        return analysis.sentiment.polarity



    def get_text_polarity_using_intensity_analyzer(self, tweet):
        '''
        SentimentIntensityAnalyzer uses popular VADER (Valence Aware Dictionary and sEntiment Reasoner) rule based algorithm for calculating text sentiment score .
        please check this link for more info :
        https://github.com/cjhutto/vaderSentiment
        '''
        ss = self.sid.polarity_scores(tweet)
        return ss['compound']

    def __get_tweet_sentiment_score_by_polarity(self, polarity=0):
        if polarity > 0:
            return 'positive'
        elif polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_raw_tweets(self,query, count=10):
        '''
        Function to pull raw tweets based on some query phrase . 
        '''
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)
            return fetched_tweets

        except tweepy.TweepError as e:
            print >> sys.stderr, traceback.format_exc()


    def get_tweet_schema(self):
        tweets = self.api.search(q="twitter", count=1)
        print "======================= Tweet Schema ======================="
        for tweet in tweets:
            for k in tweet.__dict__.keys():
                print k,' = ""'
        print "============================================================="



    def get_scored_tweets_by_query(self, query, count=5):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q=query, count=count)


            # parsing tweets one by one
            for tweet in fetched_tweets:

                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text

                # getting tweet polarity score
                polarity = self.get_text_polarity_using_intensity_analyzer(tweet.text)
                parsed_tweet['polarity'] = polarity

                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.__get_tweet_sentiment_score_by_polarity(polarity)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            print >> sys.stderr, traceback.format_exc()



    def get_scored_tweets(self,raw_fetched_tweets):

        tweets = []
        try:

            if raw_fetched_tweets is None:
                raise EmptyObjectException(" raw_fetched_tweets is empty .")

            if not isinstance(raw_fetched_tweets, tweepy.models.SearchResults):
                raise TypeMismatchException("raw_fetched_tweets is not of type tweepy.models.SearchResults . ")

            # parsing tweets one by one
            for tweet in raw_fetched_tweets:

                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text

                # getting tweet polarity score
                polarity = self.get_text_polarity_using_intensity_analyzer(tweet.text)
                parsed_tweet['polarity'] = polarity

                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.__get_tweet_sentiment_score_by_polarity(polarity)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except EmptyObjectException as e:
            print >> sys.stderr, traceback.format_exc()

        except TypeMismatchException as e:
            print >> sys.stderr, traceback.format_exc()

        except tweepy.TweepError as e:
            print >> sys.stderr, traceback.format_exc()



    def get_sentiment_summary(self,score_tweets=[]):
        try:

            if len(score_tweets)==0:
                raise EmptyTweetsException("list 'tweets' is empty .")
            if not isinstance(score_tweets, list):
                raise TypeMismatchException("tweets not of type List .")
            if 'sentiment' not in score_tweets[0].keys():
                raise TweetException("provide 'scored' list of tweets as argument .")

            print "======================= Sentiment Summary ======================="

            print "No of Tweets = " ,len(score_tweets)
            print ""
            # picking positive tweets from tweets
            ptweets = [tweet for tweet in score_tweets if tweet['sentiment'] == 'positive']
            # percentage of positive tweets
            print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(score_tweets)))
            # picking negative tweets from tweets
            ntweets = [tweet for tweet in score_tweets if tweet['sentiment'] == 'negative']
            # percentage of negative tweets
            print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(score_tweets)))
            # percentage of neutral tweets
            print("Neutral tweets percentage: {} % ".format(100 * (len(score_tweets) - len(ntweets) - len(ptweets)) / len(score_tweets)))

            # printing first 5 positive tweets
            print("\n\nPositive tweets:")
            for tweet in ptweets[:10]:
                print(tweet['text'])

            # printing first 5 negative tweets
            print("\n\nNegative tweets:")
            for tweet in ntweets[:10]:
                print(tweet['text'])

        except TypeMismatchException:
            print >> sys.stderr, traceback.format_exc()
        except EmptyTweetsException:
            print >> sys.stderr, traceback.format_exc()
        except TweetException:
            print >> sys.stderr, traceback.format_exc()

        print "====================================================================="



    def get_sentiment_classification_by_query(self,query,count=5):

        try:
            fetched_raw_tweets = self.get_raw_tweets(query,count)
            score_tweets = self.get_scored_tweets(fetched_raw_tweets)
            self.get_sentiment_summary(score_tweets)

        except:
            print >> sys.stderr, traceback.format_exc()