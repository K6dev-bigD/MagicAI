import gensim
from gensim import corpora

_author_ = 'kundan kumar'

""" DEMO """
documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

#print type(texts)
#print texts[0:10]
# remove words that appear only once
all_tokens = sum(texts, [])

print type(all_tokens)
print all_tokens
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)

texts = [[word for word in text if word not in tokens_once] for text in texts]

print texts

# Create Dictionary.
id2word = corpora.Dictionary(texts)
# Creates the Bag of Word corpus.
corpus = [id2word.doc2bow(text) for text in texts]

#print corpus

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=1, update_every=1, chunksize=10000, passes=1)


topics =lda.print_topics(num_topics=2)

for i in topics:
    print i

#print "end"