import re
import nltk
from nltk.corpus import wordnet as wn
from collections import OrderedDict

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
    for i in range(len(new_list) - 1):
        while cmp_len(new_list[i], new_list[i + 1]) == 1:
            temp = new_list[i + 1]
            new_list[i + 1] = new_list[i]
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


# Ex 19
# A list comprehension that sorts a list of WordNet synsets for proximity
# to a given synset


def sort_by_proximity(syns, syn):
    """

    :param syns: a list of wordnet synsets
    :param syn: a wordnet synset
    :return: the synsets according to proximity to the synset
    """
    assert isinstance(syns, list)
    assert isinstance(syn, str)
    syn = wn.synset(syn)
    distances = [((syn.min_depth() - wn.synset(entry).min_depth()), entry) for entry in syns]
    distances.sort(reverse=True)
    return distances


# Ex 20


def elements_by_freq(duplicates):
    """

    :param duplicates: a list of string containing duplicates
    :return: a list of the set of elements with decreasing frequency

    >>> elements_by_freq(['table', 'chair', 'table', 'lamp', 'lamp', 'lamp'])
    ['lamp', 'table', 'chair']
    """
    fd = nltk.FreqDist(duplicates)
    dist = OrderedDict(sorted(fd.items(), key=lambda t: t[1]))
    dist = dist.__reversed__()
    [str(word) for word in dist]


# Ex 21


def text_difference(text, vocab):
    """

    :param text: a list of strings
    :param vocab: a list of strings
    :return: a list of words in the text but not the vocabulary
    """
    assert isinstance(text, list)
    assert isinstance(vocab, list)
    set(w for w in text).difference(set(w for w in vocab))

