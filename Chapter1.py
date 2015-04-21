## Selected exercises from the book Natural Language Processing with Python
## Chapter 1

## Ex 15
## Find all words in Chat Corpus that start with a b in alphabetical order

from nltk.book import *
sorted([w for w in set(text5) if w.startswith("b")])

## Ex21
## Slice expression that extracts the last two words of text2

text2[-2:]

## Ex22
## Find all the four-letter words in text5 and with the help of a frequency
## distribution show these words in decreasing order of frequency

s1= set([w for w in text5 if len(w)==4])
s1fr=FreqDist(s1)
s1fr.keys()

## Ex23
## Loop over the words of text6 and print all the uppercase words, one per line

for w in text6:
    if w.istitle():
        print w

## Ex26
## The expression sum([len(w) for w in text1]) sums up all the letters of the text
## Use it to work out the average word length

from __future__ import division
sum([len(w) for w in text1])/len(text1)

## Ex28
## Define a function percent(word,text) that calculates how often a given
## word occurs in a text and expresses the result as a percentage

from __future__ import division

def percent(word,text):
    fdist=FreqDist(text)
    wfreq=fdist[word]
    print 100*wfreq/ len(text)


