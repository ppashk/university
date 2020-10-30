import nltk
import re
import pprint
import random
from urllib import request
from nltk import word_tokenize
from nltk.corpus import brown
from nltk.corpus import wordnet as wn

raw = """THE Dawn of Love is an oil painting by English artist 
William Etty, first exhibited in 1828. Loosely based on a passage 
from John Milton's 1634 Comus, it shows Venus leaning across to 
wake the sleeping Love by stroking his wings. It was very poorly 
received when first exhibited; the stylised Venus was thought unduly 
influenced by foreign artists such as Rubens as well as being overly 
voluptuous and unrealistically coloured, while the painting as a whole 
was considered tasteless and obscene. The Dawn of Love was omitted 
from the major 1849 retrospective exhibition of Etty's works, and 
its exhibition in Glasgow in 1899 drew complaints for its supposed 
obscenity. In 1889 it was bought by Merton Russell-Cotes, and has 
remained in the collection of the Russell-Cotes Art Gallery & Museum ever since."""
tokens = word_tokenize(raw)

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

porter_output = [porter.stem(t) for t in tokens]
lancaster_output = [lancaster.stem(t) for t in tokens]

print(porter_output)
print(lancaster_output, '\n')

print('inexpressible'.index('re'))
words = ['a', 'list', 'of', 'words']
print(words.index('of'), '\n')

pattern = r'(\w+)ian'
repl = r'\1a'
print(re.sub(pattern, repl, 'Canadian'), '\n')

text = """ I wil straight dispose, as best I can, th'inferiour Magistrate ...
And I haue thrust my selfe into this maze, Happily to wiue and thriue, as best I may ...
In fine, my life is that of a great schoolboy, getting into scrapes for the fun of it,
and fighting my way out as best as I can!
As best as she can she hides herself in the full sunlight
"""
print(re.findall(r'(?i)as best (?:as )?(?:I|we|you|he|she|they|it) can', text), '\n')

text = 'sight kite dude over kitty little'
text = re.sub(r'ight', 'iet', text)
text = re.sub(r'\bdude\b', 'dood', text)
text = re.sub(r'([b-df-hj-np-tv-z])(e)\b', r'\2\1', text)
text = re.sub(r'er\b', 'ah', text)
text = re.sub(r'y\b', 'eh', text)
text = re.sub(r'le\b', 'el', text)
print(text, '\n')

file = open('resources/BBC.html').read()
file = re.sub(r'<.*>', '', file)
file = re.sub(r'\s+', ' ', file)

text = """long-
term"""
pattern = r'\w+-\n\w+'
print(re.findall(pattern, text))
pattern = r'(\w+-)(\n)(\w+)'
re.findall(pattern, text)
print(re.sub(pattern, r'\1\3', text), '\n')


def soundex(word):
    word = word.upper()

    sound = word[0]

    word = re.sub(r'([BFPV])[BFPV]', r'\1', word)  #
    word = re.sub(r'([CGJKQSXZ])[CGJKQSXZ]', r'\1', word)
    word = re.sub(r'([DT])[DT]', r'\1', word)
    word = re.sub(r'LL', r'L', word)
    word = re.sub(r'([MN])[MN]', r'\1', word)
    word = re.sub(r'RR', r'R', word)

    word = re.sub(r'([BFPV])([HW])[BFPV]', r'\1\2', word)
    word = re.sub(r'([CGJKQSXZ])([HW])[CGJKQSXZ]', r'\1\2', word)
    word = re.sub(r'([DT])([HW])[DT]', r'\1\2', word)
    word = re.sub(r'L([HW])L', r'L\1', word)
    word = re.sub(r'([MN])([HW])[MN]', r'\1\2', word)
    word = re.sub(r'R([HW])R', r'R\1', word)

    word = re.sub(r'[AEIOUYHW]', r'', word)
    word = re.sub(r'[BFPV]', '1', word)
    word = re.sub(r'[CGJKQSXZ]', '2', word)
    word = re.sub(r'[DT]', '3', word)
    word = re.sub(r'L', '4', word)
    word = re.sub(r'[MN]', '5', word)
    word = re.sub(r'R', '6', word)

    if sound in 'AEIOUYHW':
        sound = (sound + word + '000')[:4]
    else:
        sound = (sound + word[1:] + '000')[:4]
    return sound

print(soundex('Honeyman'), '\n')


def ari(fileid):
    words = nltk.corpus.abc.words(fileids=fileid)

    text = nltk.corpus.abc.raw(fileids=fileid)
    sents = nltk.sent_tokenize(text)

    word_number = len(words)
    word_length = sum(len(w) for w in words)
    miu_w = word_length / word_number

    sent_length = sum(len(s.split()) for s in sents)
    sent_number = len(sents)
    miu_s = sent_length / sent_number

    ari = 4.71 * miu_w + 0.5 * miu_s - 21.43
    return ari


print(ari('rural.txt'))
print(ari('science.txt'), '\n')

words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
vsequences = [''.join(re.findall(r'[aeiou]', v)) for v in words]
print(sorted(vsequences), '\n')


class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((wn.synsets(self._stem(word))[0].offset(), i)
                                 for (i, word) in enumerate(text)
                                 if wn.synsets(self._stem(word)) != [])



    def concordance(self, word, width=40):
        key = wn.synsets(self._stem(word))[0].offset()
        wc = int(width / 4)  # words of context
        for i in self._index[key]:
            lcontext = ' '.join(self._text[i - wc:i])
            rcontext = ' '.join(self._text[i:i + wc])
            ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
            rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
            print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()


porter = nltk.PorterStemmer()
grail = nltk.corpus.webtext.words('grail.txt')
text = IndexedText(porter, grail)
text.concordance('women')
print()

def guess_language(text):
    candidate_language = ['English-Latin1', 'French_Francais-Latin1',
                          'German_Deutsch-Latin1', 'Italian-Latin1', 'Spanish-Latin1']

    fdist = nltk.FreqDist(lang for lang in candidate_language
                               for w in text if w in nltk.corpus.udhr.words(lang))
    return fdist

text_english = "Wikipedia is a project dedicated to the building of free encyclopedias in all languages of the world. The project started with the English-language Wikipedia on January 15, 2001. On March 23, 2001 it was joined by a French Wikipedia, and shortly afterwards by many other languages. Large efforts are underway to highlight the international nature of the project. On 20 September 2004 Wikipedia reached a total of 1,000,000 articles in over 100 languages.".split()
text_french = "Wikipédia Écouter est un projet d'encyclopédie universelle, multilingue, créé par Jimmy Wales et Larry Sanger le 15 janvier 2001 en wiki sous le nom de domaine wikipedia.org. Les versions des différentes langues utilisent le même logiciel de publication, MediaWiki, et ont la même apparence, mais elles comportent des variations dans leurs contenus, leurs structures et leurs modalités d'édition et de gestion.".split()
text_german = "Wikipedia ist ein am 15. Januar 2001 gegründetes gemeinnütziges Projekt zur Erstellung einer Enzyklopädie in zahlreichen Sprachen mit Hilfe des Wiki­prinzips. Gemäß Publikumsnachfrage und Verbreitung gehört Wikipedia unterdessen zu den Massenmedien. Aufgrund der für die Entstehung und Weiterentwicklung dieser Enzyklopädie charakteristischen kollaborativen Erstellungs-, Kontroll- und Aushandlungsprozesse der ehrenamtlichen Beteiligten zählt Wikipedia zugleich zu den Social Media.".split()
text_italian = "Wikipedia (pronuncia: vedi sotto) è un'enciclopedia online a contenuto libero, collaborativa, multilingue e gratuita, nata nel 2001, sostenuta e ospitata dalla Wikimedia Foundation, un'organizzazione non a scopo di lucro statunitense. Lanciata da Jimmy Wales e Larry Sanger il 15 gennaio 2001, inizialmente nell'edizione in lingua inglese, nei mesi successivi ha aggiunto edizioni in numerose altre lingue. Sanger ne suggerì il nome,[1] una parola macedonia nata dall'unione della radice wiki al suffisso pedia (da enciclopedia).".split()
text_spanish = "Wikipedia es una enciclopedia libre, políglota y editada de manera colaborativa. Es administrada por la Fundación Wikimedia, una organización sin ánimo de lucro cuya financiación está basada en donaciones. Sus más de 46 millones de artículos en 288 idiomas han sido redactados conjuntamente por voluntarios de todo el mundo, lo que hace un total de más de 2000 millones de ediciones, y prácticamente cualquier persona con acceso al proyecto6​ puede editarlos, salvo que la página se encuentre protegida contra vandalismos para evitar problemas y/o trifulcas.".split()

print(guess_language(text_english).max())
print(guess_language(text_french).max())
print(guess_language(text_german).max())
print(guess_language(text_italian).max())
print(guess_language(text_spanish).max(), '\n')
