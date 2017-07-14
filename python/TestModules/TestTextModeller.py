from TextAnalysisBox.TextModeller import TextModeller
from Utilities.UtilityFunctions import display

_author_ = 'kundan kumar'

'''
This api underneath python libraries like : 

NLTK
TextBlob
PyEnchant

'''


if __name__ == '__main__':


    raw_text = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E." \
               " Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that" \
               " African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."


    modeller = TextModeller()

    # api to get pos tagged version of the raw text
    pos_tagged_text = modeller.get_pos_tagging(raw_text)
    #display(pos_tagged_text)


    # api to get named identities from raw text
    named_identities = modeller.get_named_identities_from_text(raw_text)
    #display(named_identities)

    # api to check if a word present in a dictionary
    # it look for word in english US dictionary as of now
    #print(modeller.check_if_word_present_in_dictionary(word="hello"))


    # api to suggest valid words near to the word
    #few dictionaries (en_GB, en_US, de_DE, fr_FR)
    #display(modeller.suggest_nearest_words(word="hel"))

    # we can add more words to stop words
    # modeller.update_stop_words(['word1', 'word2'])


    # api to remove stopwords and punctuations
    #print(modeller.remove_stop_words_and_punctuation(raw_text))







