import re
import string
import subprocess
frequency = {}
file = open('text.txt', 'r')
text_string = file.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    print(words, frequency[words])