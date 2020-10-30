from nltk.book import *

print(sorted(w for w in set(text5) if w.startswith('b')), '\n')

print(list(range(10)))
print(list(range(10, 20)))
print(list(range(10, 20, 2)))
print(list(range(20, 10, -2)), '\n')

print(text9.index('sunset'))
print(' '.join(text9[621:644]), '\n')

print(len(sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))), '\n')

print("sorted(set(w.lower() for w in text1)):", len(sorted(set(w.lower() for w in text1))))
print("sorted(w.lower() for w in set(text1)):", len(sorted(w.lower() for w in set(text1))))
print('Consider the statements in sorted() function: The fisrt line searches each word in text1, then convert the words to lower case, finally use set() to avoid repetitions.\nThe second line removes repetitions in the original text, and then convert the words to lower case. The result may contain repetitions.\nThe second will give a larger value as long as there\'re a word with different formats in the original text(upper case and lower case)\n')

w = 'Hello'
print('w.isupper() ', w.isupper())
print('not w.islower() ', not w.islower())
print('The truth condition for w.isupper() requires all the characters are upper case. The truth condition for not w.islower() requires at least one of the characters is upper case.\n')

print(text2[-2:], '\n')


fdist = FreqDist(w for w in text5 if len(w) == 4)
print(fdist.most_common(), '\n')

words = [w for w in text6 if w.isupper()]
for w in words:
    print(w)
print()

a = [w for w in text6 if w.endswith('ize')]
b = [w for w in text6 if 'z' in w]
c = [w for w in text6 if 'pt' in w]
d = [w for w in text6 if w.istitle()]

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print([w for w in sent if w.startswith('sh')])
print([w for w in sent if len(w) > 4], '\n')

total_length = sum(len(w) for w in text1)
total_words = len(text1)
average_word_length = total_length / total_words
print(average_word_length, '\n')

def vocab_size(text):
    return len(set(text))

def percent(word, text):
    return 100 * text.count(word) / len(text)

print(set(sent3) < set(text1))