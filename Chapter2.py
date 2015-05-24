## Selected exercises from the book Natural Language Processing with Python
## Chapter 2

## NLTK might be at Lib//site-packages so you may have to use
## import sys
## sys.path.append('C://Python27//Lib//site-packages//nltk')


## Ex 1
## Create a variable phrase containing a list of words and
## experiment with indexing, slicing, addition, multiplication, sorting
phrase = ['It','is','a','beautiful','morning']
## Indexing
phrase[0]
## Slicing
phrase[2:]
## Addition
phrase + ['today']
## Multiplication
phrase * 2
## Sorting
sorted(phrase)



## Ex 2
## Use the corpus module to find tokens and types of austen-persuasion,txt

from nltk.corpus import gutenberg
words = gutenberg.words('austen-emma.txt')
tokens = len(words)
types = len(set(words))

## Ex 5
## Investigate the holonym- meronym relations for some nouns

from nltk.corpus import wordnet as wn
wn.synset('body.n.01').part_meronyms()
wn.synset('arm.n.01').part_holonyms()
wn.synset('canis.n.01').member_meronyms()
wn.synset('italy.n.01').member_holonyms()
wn.synset('bread.n.01').substance_meronyms()
wn.synset('curd.n.02').substance_holonyms()


## Ex 7
## According to Stunk and White's Eelements of style
## the word "however" used at the start of the sentence means
## "in whatever way". eg "However you advise him, he will do as he thinks best"
## Use the concordance tool to study actual usage of this word
## Using the Wall Street Journal Corpus, we can see that's not entirely true

from nltk.book import *
text7.concordance('However')

## Ex 11
## Can you find closed classes of words that exhibit significant differences
## across different genres?
## I use the closed class of pronouns here. For romance, the result is
## I: 0 you: 558 he: 1068 she: 728 it: 717 we: 109 they: 237 me: 194 us: 42
## which is kind of expected, with the most occurences being those of 'he' and 'she'
## For the learned category, which includes text from medicine, mathematics,
## social and political sciences, humanities etc the result is
## I: 0 you: 42 he: 387 she: 67 it: 1146 we: 526 they: 407 me: 44 us: 79
## with the most occurences being those of 'it', 'we' and 'they'

import nltk
from nltk.corpus import brown
romance = brown.words(categories='romance')
learned = brown.words(categories='learned')
fdist1 = nltk.FreqDist([w.lower() for w in romance])
fdist2 = nltk.FreqDist([w.lower() for w in learned])
pronouns = ['I','you','he','she','it','we','they','me','us']
for p in pronouns:
	print p + ':', fdist1[p],

for p in pronouns:
	print p + ':', fdist2[p],


## Ex 12
## What fraction of words in the CMU Pronouncing Dict.
## have more than one possible pronunciation?
	
cmu = nltk.corpus.cmudict.words()
fdist = nltk.FreqDist(cmu)
keys = fdist.keys()
len([w for w in keys if fdist[w]>1])



## Ex 14
## Define a function 'supergloss' that takes a synset s as its argument
## and returns a string of the concatenation of the definition of s
## and the definitions of all the hypernyms and hyponyms of s

def supergloss(s):
        from  nltk.corpus import wordnet as wn
        originaldef = wn.synset(s).definition()
        originalsyn = wn.synset(s)
        hyponyms = originalsyn.hyponyms()
        hypernyms = originalsyn.hypernyms()
        extradeflist = hyponyms + hypernyms
        extradefnames = [synset.name() for synset in extradef]
        extradefs = [wn.synset(w).definition() for w in extradefnames]
        extradefs = ' '.join(extradefs)
        print originaldef, extradefs



## Ex 17
## A function that finds the 50 most frequently
## occuring words of a text that are not stopwords

import nltk
from book import *
from nltk.corpus import stopwords
stopwords = nltk.corpus.stopwords.words('english')

def freqwords(text):
    fdist=nltk.FreqDist(text)
    fdist=list(fdist)
    for w in fdist[:50]:
        if w not in stopwords:
            print w

## To test this you can use a text from the gutenberg corpus eg
## from nltk.corpus import gutenberg
## gutenberg.fileids()
## words = gutenberg.words('austen-emma.txt')
## freqwords(words)

## Ex 18
## A function that finds the 50 most frequent bigrams of a text
## omitting bigrams that contain stopwords

def freqbigrams(text):
    '''
    returns pairs of strings
    '''
    
    global bigrams
    bigrams=bigrams(text)
    fdist=nltk.FreqDist(bigrams)
    fdist=list(fdist)
    for w in fdist[:20]:
        if w not in stopwords:
            print w


## Ex 20
## A function that takes a word and the name of a section of the Brown
## Corpus and computes the frequency of the word in that section


def word_freq(word,category):
    '''
    takes a word and a brown category as strings
    and returns the word and the frequency as integer
    '''

    category=brown.words(categories=category)
    fdist=nltk.FreqDist(category)
    if word in category:
        print word,fdist[word]



## Ex 25
## Define a function find_language() that takes a string as its argument
## and returns a list of languages that have that string as a word
## Use the Universal Declaration of Human Rights corpus


import nltk
from nltk.corpus import udhr
ids = nltk.corpus.udhr.fileids()
def find_language(word):
        for language in ids:
                if word in nltk.corpus.udhr.words(language):
                        print language
