

_author_ = 'kundan kumar'

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import enchant
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

class TextModeller:

    def __init__(self):
        self.__dictionary = enchant.Dict("en_US")
        self.__STOP_TYPES = 'english'
        self.__stop_words = set(stopwords.words(self.__STOP_TYPES))
        self.__stop_words.update(['.', '--', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

    def get_pos_tagging(self, text):
        chunked = pos_tag(word_tokenize(text))
        return chunked

    def get_named_identities_from_text(self,text):
        chunked = ne_chunk(pos_tag(word_tokenize(text)))
        prev = None
        continuous_chunk = []
        current_chunk = []
        for i in chunked:
            if type(i) == Tree:
                current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue
        return continuous_chunk

    def check_if_word_present_in_dictionary(self,word):
        return self.__dictionary.check(word)

    def suggest_nearest_words(self, word ):
        return self.__dictionary.suggest(word)

    def update_stop_words(self,list_of_stopwords=[]):
        self.__stop_words.update(list_of_stopwords)

    def remove_stop_words_and_punctuation(self, text):
        # remove it if you need punctuation
        return ''.join([i.lower()+' ' for i in wordpunct_tokenize(text) if i.lower() not in self.__stop_words])


