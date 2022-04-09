#Created by Roxanne Pradillon 
import nltk
from nltk.stem import WordNetLemmatizer
import inflect
from Chapter01.pos_tagging import pos_tag_nltk

#Read in the text file 
print("Counting nouns – plural and singular nouns")
file = open("Chapter01/sherlock_holmes_1.txt", "r", encoding="utf-8")
sherlock_holmes_text = file.read()

#Remove newlines for better readability
sherlock_holmes_text = sherlock_holmes_text.replace("\n"," ")

#Do part of speech tagging
words_with_pos = pos_tag_nltk(sherlock_holmes_text)

#Define the get_nouns function, which will filter out the nouns from all the words
def get_nouns(words_with_pos):
    noun_set = ["NN", "NNS"]
    nouns = [word for word in words_with_pos if
    word[1] in noun_set]
    return nouns

#Run the preceding function on the list of POS-tagged words and print it
nouns = get_nouns(words_with_pos)
print("List of names")
print(nouns)

#Plural or singular

#NLTK tags
def is_plural_nltk(noun_info):
    pos = noun_info[1]
    if (pos == "NNS"):
        return True
    else:
        return False

#WordNetLemmatizer class in the nltk.stem package
def is_plural_wn(noun): 
    wnl = WordNetLemmatizer()
    lemma = wnl.lemmatize(noun, 'n')
    plural = True if noun is not lemma else False
    return plural

# change a singular noun into plural
def get_plural(singular_noun):
    p = inflect.engine()
    return p.plural(singular_noun)

# change a plural noun into singular
def get_singular(plural_noun):
    p = inflect.engine()
    plural = p.singular_noun(plural_noun)
    if (plural):
        return plural
    else:
        return plural_noun

#determine if the noun is plural.
def plurals_wn(words_with_pos):
    other_nouns = []
    for noun_info in words_with_pos:
        word = noun_info[0]
        plural = is_plural_wn(word)
        if (plural):
            singular = get_singular(word)
            other_nouns.append(singular)
        else:
            plural = get_plural(word)
            other_nouns.append(plural)
    return other_nouns

# return a list of changed nouns
other_nouns_wn = plurals_wn(nouns)
print("List of changed nouns : \n")
print(other_nouns_wn)








