from SentimentBox.TwitterAnalyzer import TwitterApiClient

_author_ = 'kundan kumar'

# keys and tokens from the Twitter Dev Console
consumer_key = 'CJ7914JbkgkGxfqWCP9g8mUXE'
consumer_secret = 'qBFfYcXsc50KAitsXxQ5In98349aL9rD1knsjW0NofD6AoH20l'
access_token = '447751357-nyBSwbZkl2cHwQsLR3ovQz3UQi2Oh1ed7sFsa8bD'
access_token_secret = '8NNnSLkCAvN26QP7bXt5ibp89MunF3YvLW7QqlFMmAWDK'

api = TwitterApiClient(consumer_key, consumer_secret, access_token, access_token_secret)


paragraph = "he is not only good but the best "
print "input text = ",paragraph
print "score using VADER = ",api.get_text_polarity_using_intensity_analyzer(paragraph)
print "score using TEXTBLOB = ",api.get_text_polarity_using_textblob(paragraph)


paragraph = "he is good but not the best"
print "input text = ",paragraph
print "score using VADER = ",api.get_text_polarity_using_intensity_analyzer(paragraph)
print "score using TEXTBLOB = ",api.get_text_polarity_using_textblob(paragraph)

paragraph = "he used to be good but in recent times he isn't making a mark"
print "input text = ",paragraph
print "score using VADER = ",api.get_text_polarity_using_intensity_analyzer(paragraph)
print "score using TEXTBLOB = ",api.get_text_polarity_using_textblob(paragraph)


paragraph = "he is not good"
print "input text = ",paragraph
print "score using VADER = ",api.get_text_polarity_using_intensity_analyzer(paragraph)
print "score using TEXTBLOB = ",api.get_text_polarity_using_textblob(paragraph)


