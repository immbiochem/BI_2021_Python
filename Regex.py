#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
import pandas as pd
import seaborn as sns

# 1)
exp = re.compile('ftp\.[\w\.\/\#]+[^;\s]')
file = []
with open(r'.\references.txt', 'r') as text:
    for line in text:
        file += re.findall(exp, line.strip())
with open(r'.\ftps.txt', 'w') as output:
    for link in file:
        output.write(link + '\n')

# 2)
exp = re.compile('\d+\.?\d*')
numeric = []
with open(r'.\2430AD.txt', 'r') as text:
    for line in text:
        numeric += re.findall(exp, line.strip())
# print(numeric) ['2430', '1969', '2430', '2430', '57', '57', '1970', '3.68', '35', '460', '2430']
# print(len(numeric)) 11

# 3)
exp = re.compile('[B-Zb-z]*a+\-*[A-Za-z]*', re.IGNORECASE)
list_of_a_words = []
with open(r'.\2430AD.txt', 'r') as text:
    for line in text:
        list_of_a_words += re.findall(exp, line.strip())
# print(len(list_of_a_words)) 985

# 4)
exp = re.compile(r'[A-Z][\w\s\,\:\;]*\!')
exclamations = []
with open(r'.\2430AD.txt', 'r') as text:
    for line in text:
        exclamations += re.findall(exp, line.strip())
# print(exclamations) ['Yes!', 'Literally!', 'There was once a time!', 'Centuries ago!', 'Think, Cranwitz!', 'If we succeed!']
# print(len(exclamations)) 6

# 5)
exp = re.compile(r'\w+')
all_words = []
with open(r'.\2430AD.txt', 'r') as text:
    for line in text:
        all_words += re.findall(exp, line.strip())
all_uniq_words = set(all_words)
dictionary_of_len_in_uniq_words = {}
for i in range(1, 21):
    for j in all_uniq_words:
        if len(j) == i and i not in dictionary_of_len_in_uniq_words:
            dictionary_of_len_in_uniq_words[i] = 1
        elif len(j) == i:
            dictionary_of_len_in_uniq_words[i] += 1
        else:
            continue
for key in dictionary_of_len_in_uniq_words.keys():
    dictionary_of_len_in_uniq_words[key] = dictionary_of_len_in_uniq_words[key] * 100 / len(all_uniq_words)

df = pd.DataFrame(list(dictionary_of_len_in_uniq_words.items()), columns=['Length of word', 'Percent %'])
plot = sns.barplot(x='Length of word', y='Percent %', data=df)
plot.set_ylim(0, max(df['Percent %'] + 2))
