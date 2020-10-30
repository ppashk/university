import nltk
import re
import random
from urllib import request
from nltk import word_tokenize
from nltk.corpus import brown
from bs4 import BeautifulSoup

s = 'colorless'
s = s[:4] + 'u' + s[4:]
print(s, '\n')

dish = 'dishes'[:-2]
run = 'running'[:-4]
nation = 'nationality'[:-5]
do = 'undo'[2:]
heat = 'preheat'[3:]
print()

print('s[-(len(s)+1)]\n')

monty = 'Monty Python'
print(monty[::-1])

re_a = r'(\ban?\b|\bthe\b)'
re_b = r'[\d\*\+]+'
print()

# def content_of_URL(URL):
#     html = request.urlopen(URL).read().decode('utf8')
#     raw = BeautifulSoup(html).get_text()
#     tokens = word_tokenize(raw)
#     return tokens
#
# def load_punctuations(f):
#     file = open(f)
#     raw = file.read()
#     pattern = r'''(?x)        # set flag to allow verbose regexps
#         [,\.]                 # comma, period
#       | [\[\](){}<>]          # brackets () {} [] <>
#       | ['"“]                 # quotation marks
#       | [?!]                  # question mark and exclamation mark
#       | [:;]                  # colon and semicolon
#       | \.\.\.                # ellipsis
#       | [，。？！、‘：；]       # some Chinese punctuations
#     '''
#     return nltk.regexp_tokenize(raw, pattern)
# load_punctuations('resources/recorpus.txt')
#
# def load_monetary(f):
#     file = open(f)
#     raw = file.read()
#     pattern = r'''(?x)
#         \$\d+(?:,\d+)*(?:\.\d+)?      # USD
#       | £\d+(?:,\d+)*(?:\.\d+)?       # GBP
#       | ￥\d+(?:\.\d+)?               # CNY
#     '''
#     return nltk.regexp_tokenize(raw, pattern)
# load_monetary('resources/corpus.txt')
#
# def load_date(f):
#     file = open(f)
#     raw = file.read()
#     pattern = r'''(?x)
#         \d{,4}[/\.-]\d{1,2}[/\.-]\d{1,2}       # big-endian, e.g., 1996-10-23, 1996.10.23, 1996/10/23
#       | \d{1,2}[/\.-]\d{1,2}[/\.-]\d{,4}       # little-endian or middle-endian, dd/mm/yyyy or mm/dd/yyyy
#     '''
#
#     return nltk.regexp_tokenize(raw, pattern)
# load_date('resources/corpus.txt')
#
# f = 'resources/corpus.txt'
# file = open(f)
# raw = file.read()
# tokens = word_tokenize(raw)
# print([wh for wh in tokens if wh.lower().startswith('wh')], '\n')
#
# filename = 'resources/word_freq.txt'
# lines = open(filename).readlines()
# fields = []
# for line in lines:
#     field = line.split()
#     field[1] = int(field[1])
#     fields.append(field)
# print(fields, '\n')
#
# url = "https://www.accuweather.com/en/ua/kyiv/324505/weather-forecast/324505"
# html = request.urlopen(url).read().decode('utf8')
# soup = BeautifulSoup(html)
# today = soup.find(class_="info city-fcast-text")
# print(today.get_text(), '\n')
#
# def unknown(url):
#     html = request.urlopen(url).read().decode('utf8')
#     lowers = re.findall(r'\b[a-z]+', html)
#     unknowns = [w for w in lowers if w not in nltk.corpus.words.words()]
#     return unknowns
# print(unknown('https://ru.wikipedia.org'))
#
# file = open('resources/BBC.html').read()
# lowers = re.findall(r'[a-z]+', file)
# unknowns = [w for w in lowers[:100] if w not in nltk.corpus.words.words()]
# print(unknowns)

pattern = r"\w+(?:'t)?"

s = []
for i in range(500):
    s.append(random.choice("aehh "))
ori = ''.join(s)
print(' '.join(ori.split()), '\n')

def miu_w(category):
    word_length = sum(len(w) for w in brown.words(categories=category))
    word_number = len(brown.words(categories=category))
    return word_length / word_number

def miu_s(category):
    sent_length = sum(len(s) for s in brown.sents(categories=category))
    sent_number = len(brown.sents(categories=category))
    return sent_length / sent_number

def ari(category):
    return 4.71 * miu_w(category) + 0.5 * miu_s(category) - 21.43

for category in brown.categories():
    print(category, ari(category))
