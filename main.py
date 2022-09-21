import pprint

import nltk
import re
import os
from nltk.corpus import stopwords as sw

# To process the first five files
files_to_process = ['reut2-000.sgm' 'reut2-001.sgm', 'reut2-002.sgm', 'reut2-003.sgm', 'reut2-004.sgm']

"""
This function will be used to remove any lines before and after the html tag <BODY></BODY>
@:param lines will be used to read the lines of the .sgm files 
"""


def get_pure_sentences(lines):
    valid_lines = []
    not_done = True
    i = 0
    while not_done:
        match = re.search(r'.*<BODY>', lines[i])
        if match:
            first_line = True
            not_end = True
            while not_done and not_end:
                matchb = re.search(r'.*</BODY>', lines[i])
                if matchb:
                    not_end = False
                else:
                    if first_line:
                        sentence = re.sub(r'.*<BODY>', "", lines[i])
                        valid_lines.append(sentence)
                    else:
                        valid_lines.append(lines[i])
                i += 1
                if i == len(lines):
                    not_done = False
        else:
            if not_done:
                i += 1
                if i == len(lines):
                    not_done = False
    return valid_lines


"""
This function is used to read and clean the filenames while having a latin-1 encoded
@:param filename used for the .sgm file names
@:param path used to set the directory
"""


def read_doc(filename, path):
    filename = path + '/' + filename
    with open(filename, encoding='latin-1') as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


"""
The function is used to tokenize each word found in the files using the ntlk.word_tokenize
@:param lines used to read the lines of the files and tokenize each word 
"""


def tokenizer(lines):
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


# if f in files_to_process
if __name__ == "__main__":
    # loop files directory using os.listidir()
    # if re.match(r'.*\.sgm', f)
    files = [f for f in os.listdir('reuters21578') if f in files_to_process]

    sentences = []
    for file in files:
        # calling read_doc function to read the project directory
        raw = read_doc(file, 'reuters21578')
        # print('raw', raw)
        # get_pure_sentences to retrieve the temporary senteces in reuters
        temp_sentences = get_pure_sentences(raw)

        # merging the files into one array rather than a multidimensional
        sentences.extend(temp_sentences)

    # tokenize each words
    words = tokenizer(sentences)

    # meant to lower case the words tokenized
    lower_case_words = lowercase(words)

    # using the Porter stemmer to stem the lower_case_words
    stemmer_words = stemmer(lower_case_words)

    # filter the stop_words
    filter_words = filter_stop_words(stemmer_words)

    # pretty print the filter_words
    print(filter_words)
