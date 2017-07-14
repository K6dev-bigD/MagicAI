_author_ = 'kundan kumar'

import gensim
from gensim import corpora
from nltk.corpus import stopwords
import enchant

class TopicModeller:


    def __init__(self):
        self.__dictionary = enchant.Dict("en_US")
        self.__STOP_TYPES = 'english'
        self.__stop_words = set(stopwords.words(self.__STOP_TYPES))
        self.__stop_words.update(['.', '--', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])



    def get_topic_weights_for_the_document_using_LDA(self, documents=[]):

        cleaned_text = [[word for word in document.lower().split() if word not in self.__stop_words] for document in
                        documents]
        merged_tokens = sum(cleaned_text, [])
        # tokens for which count = 1
        tokens_once = set(word for word in set(merged_tokens) if merged_tokens.count(word) == 1)
        # tokens for which count > 1
        weighted_texts = [[word for word in text if word not in tokens_once] for text in cleaned_text]
        # Create Dictionary.
        id2word = corpora.Dictionary(weighted_texts)
        # Creates the Bag of Word corpus.
        corpus = [id2word.doc2bow(text) for text in weighted_texts]

        lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=id2word, num_topics=1, update_every=1,
                                              chunksize=10000, passes=1)
        topics = lda.print_topics(15)

        return topics



