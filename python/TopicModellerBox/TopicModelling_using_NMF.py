_author_ = 'kundan kumar'

import pprint
from sklearn.datasets import fetch_20newsgroups
import logging
logging.basicConfig()


# using NMF method
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF



def display_topics(model, feature_names, no_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print "Topic %d:" % (topic_idx)
        print " ".join([feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1]])



dataset = fetch_20newsgroups(shuffle=True, random_state=1, remove=('headers', 'footers', 'quotes'))
documents = dataset.data
# select first 10 records
documents = documents[0:10]
pprint.pprint(documents)




no_features = 100
# NMF is able to use tf-idf
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=no_features, stop_words='english')
tfidf = tfidf_vectorizer.fit_transform(documents)
tfidf_feature_names = tfidf_vectorizer.get_feature_names()
pprint.pprint(tfidf_feature_names)




no_topics = 5
# Run NMF
nmf = NMF(n_components=no_topics, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd').fit(tfidf)


no_top_words = 10
display_topics(nmf, tfidf_feature_names, no_top_words)


