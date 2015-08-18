__author__ = 'mspyropoulou'
Python Version 2.7.10 on PyCharm

#Ex 1
s = s[:4]+'u'+s[4:]

#Ex2
w1 = 'dishes'[:-2]
w2 = 'running'[:-4]
w3 = 'nationality'[:-5]
w4 = 'preheat'[:-4]

#Ex3
#Yes, it is possible to produce an IndexError
# Just try w1 = 'maria' and then w1[-7]

#Ex4
#Step for slice
w5 = 'exponentiation'[2:11:2]
w6 = 'exponentiation'[12:2:-2]
w7 = 'exponentiation'[12::-2]
w8 = 'exponentiation'[:5:-2]
w9 = 'exponentiation'[::2]
w10 = 'exponentiation'[4::]

#Ex5
# 'monty'[::-1] gives you 'ytnom'
# because the start index and end index are default
# while step index is 1

#Ex6
# If you want to test you write it like this
nltk.re_show(r'[[a-zA-Z]+]+','october2009')
# [a-zA-Z]+ = one or more of alphabet
nltk.re.findall(r'[a-zA-Z]+','October2009')
# returns ['October']
# [A-Z][a-z]* = Kleene Closure, same as previous
# p[aeiou]{,2}t = p and then up to 2 vowels and t
nltk.re.findall(r'p[aeiou]{,2}t','paella, pat, pout')
# returns ['pat', 'pout']
# \d+(\.\d+)? = extract one or more decimals of a floating number
nltk.re.findall(r'\d+(\.\d+)?','0.99, 2345, 234.5')
# This gives us ['.99', '', '.5']
# Remember that parentheses, except for defining operator scope
# have a second function, to select substrings to be extracted
# Zero or one of the decimal in the front \d+?
# ([^aeiou][aeiou][^aeiou])* = extract zero or more of any character other than a vowel,
# then a vowel, then any character other than a vowel
# Remember the ^ operator has another function as the first character
# inside square brackets
nltk.re.findall(r'([^aeiou][aeiou][^aeiou])*','california angel')
# This gives us ['cal', '', 'for', '', '', '', 'gel', '']
# If we want empty strings gone we use + instead of *, which means one or more
# \w+|[^\w\s]+ = one or more alphanumeric character or no alphanumeric with any whitespace character
nltk.re.findall(r'\w+|[^\w\s]+','california\nangel\t1004')
# This gives us ['california', 'angel','1004']


