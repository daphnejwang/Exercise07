from sys import argv
import string

script, file_name = argv

f = open(file_name)
data = f.read().lower()
exclude = set(string.punctuation)
clean_data = ''.join(ch for ch in data if ch not in exclude)

word_frequency = {}

words = clean_data.split()

for each_word in words:
    if not word_frequency.get(each_word):
        word_frequency[each_word] = 1
    else:
        word_frequency[each_word] +=1

for each_word, number in word_frequency.iteritems():
    print each_word, number
