
# data scrap dictionary to create list of all words with n number of letters
import string
txt = open("dictionary.txt", 'r')

def find_words(n, txt):
    txt = txt.translate(str.maketrans('', '', string.punctuation))
    list_words = []
    for word in txt.split():
        if len(word) == n:
            list_words.append(word.lower())
    
    list_words = list(set(list_words))
    print(list_words)

#save in another doc?

list_words = find_words(5, txt)


# first guess based on letter frequencies
from collections import Counter
from itertools import chain
def first_guess():
    char_count = Counter(list_words)
    print(char_count)

first_guess()

def guess():
    return
