import nltk
import re

__author__ = 'mspyropoulou'


# Ex3
# There are two ways of creating a tuple
# tups = (4,) or tups = 4,
# Either way, the comma makes the tuple, not the parenthesis


# Ex4

words = ['is', 'NLP', 'fun', '?']
tmp = words[1]
words[1] = words[0]
words[3] = '!'
words[0] = tmp

# Ex10


def cmp_len(word1, word2):
    result = cmp(len(word1), len(word2))
    return result


def sort_by_shortest(seq):
    new_list = []
    for i in seq:
        new_list.append(i)
    for i in range(len(new_list)-1):
        while cmp_len(new_list[i], new_list[i+1]) == 1:
            temp = new_list[i+1]
            new_list[i+1] = new_list[i]
            new_list[i] = temp
    return new_list

# This one needs work because it returns
# sort_by_shortest(['catss', 'ff', 'ddd', 'bbahseeea', 'cat', 'tttre'])
# ['ff', 'ddd', 'catss', 'cat', 'tttre', 'bbahseeea']

# Ex15


def freq_of_word(sent):
    """

    :param sent: a sentence as a string
    :return: word, freq of word in alphabetical order

    >>> freq_of_word('I saw a dog, a cat, and another dog')
    I 1
    a 2
    and 1
    another 1
    cat 1
    dog 2
    saw 1
    """
    assert isinstance(sent, str)
    listing = re.split(r'\W+', sent)
    fd = nltk.FreqDist(listing)
    for key in sorted(fd):
        print key, fd[key]
