_author_ = 'kundan kumar'


import re

def clean_tweet(self, text):
    '''
    Utility function to clean text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", text).split())


def display(obj):
    if isinstance(obj,list):
        for attr in obj:
            print attr
    elif isinstance(obj,basestring):
        print obj
    elif isinstance(obj, dict):
        for k,v in obj:
            print "key = ",k," value = ",v
    else:
        for attr in obj:
            print attr
