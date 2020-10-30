from nltk.book import *

print("Words:", len(text2))
print("Distinct words:", len(set(text2)), '\n')

text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])
print()

text5.collocations()
print()

print('v = set(text4)\n len(v)\n')

my_string = 'My String'
print(my_string)
print(my_string + my_string)
print(my_string * 3 + '\n')

my_sent = ['to', 'be', 'or', 'not', 'to', 'be']
sentence = ' '.join(my_sent)
print(sentence)
print(sentence.split(), '\n')

phrase1 = 'My'
phrase2 = 'String'
print(len(phrase1 + phrase2))
print(len(phrase1) + len(phrase2), '\n')

print('The latter one will be more relevant in NLP. Since we are dealing with words more than the single characters, we are more likely to use index in list rather than slicing in string.\n')

print('The third character of the third word in sent1.\n')

indices = [i for i, x in enumerate(sent3) if x == 'the']
print(indices)