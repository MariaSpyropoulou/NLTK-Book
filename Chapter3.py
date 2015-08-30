# coding=utf-8
__author__ = 'mspyropoulou'
# Python Version 2.7.10 on PyCharm

import nltk
from bs4 import BeautifulSoup
from urllib import urlopen
from readability.readability import Document


# Ex 1
s = 'colorless'
s = s[:4]+'u'+s[4:]

# Ex2
w1 = 'dishes'[:-2]
w2 = 'running'[:-4]
w3 = 'nationality'[:-5]
w4 = 'preheat'[:-4]

# Ex3
# Yes, it is possible to produce an IndexError
# Just try w1 = 'maria' and then w1[-7]

# Ex4
# Step for slice
w5 = 'exponentiation'[2:11:2]
w6 = 'exponentiation'[12:2:-2]
w7 = 'exponentiation'[12::-2]
w8 = 'exponentiation'[:5:-2]
w9 = 'exponentiation'[::2]
w10 = 'exponentiation'[4::]

# Ex5
# 'monty'[::-1] gives you 'ytnom'
# because the start index and end index are default
# while step index is 1

# Ex6
# If you want to test you write it like this
nltk.re_show(r'[[a-zA-Z]+]+', 'october2009')
# [a-zA-Z]+ = one or more of alphabet
nltk.re.findall(r'[a-zA-Z]+', 'October2009')
# returns ['October']
# [A-Z][a-z]* = Kleene Closure, same as previous
# p[aeiou]{,2}t = p and then up to 2 vowels and t
nltk.re.findall(r'p[aeiou]{,2}t', 'paella, pat, pout')
# returns ['pat', 'pout']
# \d+(\.\d+)? = extract one or more decimals of a floating number
nltk.re.findall(r'\d+(\.\d+)?', '0.99, 2345, 234.5')
# This gives us ['.99', '', '.5']
# Remember that parentheses, except for defining operator scope
# have a second function, to select substrings to be extracted
# Zero or one of the decimal in the front \d+?
# ([^aeiou][aeiou][^aeiou])* = extract zero or more of any character other than a vowel,
# then a vowel, then any character other than a vowel
# Remember the ^ operator has another function as the first character
# inside square brackets
nltk.re.findall(r'([^aeiou][aeiou][^aeiou])*', 'california angel')
# This gives us ['cal', '', 'for', '', '', '', 'gel', '']
# If we want empty strings gone we use + instead of *, which means one or more
# \w+|[^\w\s]+ = one or more alphanumeric character or no alphanumeric with any whitespace character
nltk.re.findall(r'\w+|[^\w\s]+', 'california\nangel\t1004')
# This gives us ['california', 'angel','1004']

# Ex7
# A regex to detect single determiners
nltk.re.findall(r'\b[aA]\b|\b[aA]n\b|\b[tT]he\b', 'A nice day at the pub. Anyone with a brain. The right choice.')
# A regex to match an arithmetic expression
nltk.re.findall(r'\d+\*?\+?\d+', 'When we do 33*2+8 we do math basically')
nltk.re.findall(r'\d*(?:\*|\+)+\d*', 'When we do 6.33*2+8 we do math basically')


# Ex8
# Write a utility function that takes a URL as its argument and returns
# the contents with all HTML markup removed.
# For this we will use the BeautifulSoup package
# Download bs with easy_install BeautifulSoup4 or download the tarball and
# make sure bs4 is extracted and put under site-packages or sth
# I also installed the modules readability, chardet and lxml


def cleantext():
    url = 'http://www.bbc.co.uk/news/world-europe-34007859'
    html = urlopen(url).read()
    readable_article = Document(html).summary()
    soup = BeautifulSoup(readable_article, "lxml")
    clean = soup.text
    return clean[:500]



# Ex9
def load(f=str):
    import re
    files = open(f)
    raw = files.read()
    pattern = re.compile(r"""\$?\d+(\.\d+)?%?    # currency
                             \d+/\d+/\d+         #dates""", re.VERBOSE)
    nltk.regexp_tokenize(raw, pattern)


# Ex10
sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
[(w, len(w)) for w in sent]

# Ex11
sent2 = 'He stayed at the hotel until the end of August'
sent2.split('h')

# Ex12
for w in sent2:
    print w

# Ex13
# .split() just returns the tokens of the string as separate strings
# split(' ') does the exact same thing. So sent2.split() and sent2.split(' ')
# both return ['He', 'stayed', 'at', 'the', 'hotel', 'until', 'the', 'end', 'of', 'August']
# If the sentence contains tab chars or consecutive whitespace chars
# .split(' ') returns those chars as well
# sent3 = 'Lana   and her boyfriend  went on a trip'
# ['Lana', '', '', 'and', 'her', 'boyfriend', '', 'went', 'on', 'a', 'trip']

# Ex14
# words.sort() and sorted(words) both return the strings in alphabetical order

# Ex17
a = '%6s' % 'exponentiation'
b = '%-6s' % 'exponentiation'
# Both a and b return 'exponentiation'
c = '%6s' % 'expo'
d = '%-6s' % 'expo'
# These return '  expo' and 'expo  ' respectively

# Ex18
# You can find a corpus with nltk.corpus.sth

import re
emma = sorted(set(nltk.corpus.treebank.words()))
result = [w for w in emma if re.search(r'^wh(at|ere|o|y|en|ich)$', w)]

# Ex19
exercise = open('testfile.txt').readlines()
exercises = [line.split() for line in exercise]
result1 = [[y, int(x)] for y, x in exercises]

# Ex20
url2 = 'http://www.bbc.co.uk/weather/2643743'
html2 = urlopen(url2).read()
readable_article2 = Document(html2).summary()
soup2 = BeautifulSoup(readable_article2, "lxml")
clean2 = soup2.text
cleanstring = clean2.encode('utf8')
assert isinstance(cleanstring, str)
print cleanstring
re.findall(r'\w+°C\b', cleanstring)

# Ex21
def unknown(url):
    html3 = urlopen(url).read()
    readable3 = Document(html3).summary()
    soupobj = BeautifulSoup(readable3, "lxml")
    clean3 = soupobj.text
    cleanstr = clean3.encode('utf8')
    words = nltk.corpus.words.words()
    result = re.findall(r'\b[a-z]+\b', cleanstr)
    unknownwords = [w for w in result if w not in words]
    return unknownwords

































