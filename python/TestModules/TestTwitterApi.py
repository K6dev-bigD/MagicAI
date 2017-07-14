from SentimentBox.TwitterAnalyzer import TwitterApiClient
from Utilities.UtilityFunctions import display

_author_ = 'kundan kumar'

if __name__ == '__main__':

    print "App Start"

    # keys and tokens from the Twitter Dev Console
    consumer_key = 'CJ7914JbkgkGxfqWCP9g8mUXE'
    consumer_secret = 'qBFfYcXsc50KAitsXxQ5In98349aL9rD1knsjW0NofD6AoH20l'
    access_token = '447751357-nyBSwbZkl2cHwQsLR3ovQz3UQi2Oh1ed7sFsa8bD'
    access_token_secret = '8NNnSLkCAvN26QP7bXt5ibp89MunF3YvLW7QqlFMmAWDK'

    # create instance if SentiBox Twitter API client
    api = TwitterApiClient(consumer_key, consumer_secret, access_token, access_token_secret)

    # api to get typical tweet schema from twitter
    api.get_tweet_schema()

    # api to get raw tweets from twitter based on query .
    raw_tweets = api.get_raw_tweets(query='donal trump', count=20)
    display(raw_tweets)

    # api to manually get sentiment score for the raw tweets
    scored_tweets = api.get_scored_tweets(raw_tweets)
    display(scored_tweets)

    # api to get sentiment summary out of scored tweets we obtained in previous step
    api.get_sentiment_summary(scored_tweets)


    # ALTERNATIVELY , we can use this api to get sentiment summary base on keyword query on twitter
    api.get_sentiment_classification_by_query(query="obama" , count=20)


    print "end "
