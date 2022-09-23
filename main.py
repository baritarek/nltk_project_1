"""
Tarek Bari 40131955
COMP 479
Project 1
"""

import nltk
import os

from nltk import RegexpTokenizer
from nltk.corpus import stopwords as sw

# To process the first five files
files_to_process = ['reut2-000.sgm', 'reut2-001.sgm', 'reut2-002.sgm', 'reut2-003.sgm', 'reut2-004.sgm']

"""
This function is used to read and clean the filenames while having a latin-1 encoded while also removing any lines 
before and after the html tags. 
@:param folder used to process the reuters21578 file directory 
@:param files_to_process will be processing the first five selected fiels 
"""


def process_readable_files(folder='reuters21578', files_to_process=files_to_process):
    # loop files directory using os.listidir()
    files = [f for f in os.listdir(folder) if f in files_to_process]
    sentences = []
    for file in files:
        get_pure_sentences = open(f'reuters21578/{file}', encoding='latin-1').read()
        tokenizer = RegexpTokenizer('\s+|<[^>]*>|&#[\d+][\S+]|;', gaps=True)
        raw = tokenizer.tokenize(get_pure_sentences)
        sentences.append(' '.join(raw))

    return sentences


"""
The function is used to tokenize each word found in the files using the ntlk.word_tokenize
@:param lines used to read the lines of the files and tokenize each word 
"""


def tokenize(lines):
    words = []
    for res in lines:
        word = nltk.word_tokenize(res)
        for w in word:
            words.append(w)
    return words


"""
This function is meant to lower case all the words in the files
@:param words used to store the the words of the file in order to lowercase
"""


def lowercase(words):
    for i in range(len(words)):
        words[i] = words[i].lower()
    return words


"""
This function uses the porter stemmer of nltk while stemming all words 
@:param used to store the words in nltk.PorterStemmer().stem()
"""


def stemmer(words):
    for i in range(len(words)):
        words[i] = nltk.PorterStemmer().stem(words[i])
    return words


"""
This function is used to remove a list of stop words from the list
@:param words will be used to filter the words in files 
@:param stop_words is used to accept words as a list
"""


def filter_stop_words(words, stop_words=sw.words('english')):
    filtered_words = []
    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return filtered_words


if __name__ == "__main__":
    docs_to_read = []
    # process and read reuters files
    docs_to_read = process_readable_files()

    # tokenize each words
    words = tokenize(docs_to_read)

    # meant to lower case the words tokenized
    lower_case_words = lowercase(words)

    # using the Porter stemmer to stem the lower_case_words
    stemmer_words = stemmer(lower_case_words)

    # filter the stop_words
    filter_words = filter_stop_words(stemmer_words)
