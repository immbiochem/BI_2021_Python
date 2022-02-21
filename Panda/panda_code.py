#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv(r'train.csv')

# data

fig_dims = (14, 8)
fig, axes = plt.subplots(figsize=fig_dims)
sns.barplot(x=data['pos'], y=data['A'], color='red')
sns.barplot(x=data['pos'], y=data['T'], color='blue')
sns.barplot(x=data['pos'], y=data['C'], color='green')
sns.barplot(x=data['pos'], y=data['G'], color='yellow')
axes.set(xlabel='Position', ylabel='Amount of reads')
plt.grid()

alphabet = ['A', 'T', 'G', 'C']
colors = ['red', 'blue', 'green', 'orange']
# fig_dims = (20, 15)
# fig, axes = plt.subplots(figsize=fig_dims)
for i in range(len(alphabet)):
    plt.subplot(2, 2, i + 1)
    sns.barplot(x=data['pos'], y=data[alphabet[i]], color=colors[i])
    plt.title("Base " + alphabet[i])
    plt.xticks(rotation=90)
    plt.grid()

# data.loc[data.matches > data.matches.mean(), ["pos", "reads_all", "mismatches", "deletions", "insertions"]]

data.loc[data.matches > data.matches.mean(), ["pos", "reads_all", "mismatches", "deletions", "insertions"]].to_csv(
    'train_part.csv')

table = pd.read_excel(r'imm.xlsx', sheet_name='Metabolites')

# table

table.info()

table.describe()

sns.pairplot(table[['6hr', '20hr', '30hr']])

sns.pairplot(table.loc[:, table.columns != '0Hr'], hue='SUPER_PATHWAY', height=5)

table.query('SUPER_PATHWAY == "Amino acid"').iloc[:, 5].hist()

table.query('SUPER_PATHWAY == "Amino acid"').iloc[:, 6].hist()

table.query('SUPER_PATHWAY == "Amino acid"').iloc[:, 7].hist()

common_pathway = table.iloc[:, [1, 4, 5, 6, 7]].groupby('SUPER_PATHWAY').mean()
# common_pathway

vector = [0, 6, 20, 30]
fig_dims = (14, 8)
fig, axes = plt.subplots(figsize=fig_dims)
axes.plot(vector, common_pathway.iloc[0], color="r")
axes.plot(vector, common_pathway.iloc[1], color="g")
axes.plot(vector, common_pathway.iloc[2], color="y")
axes.plot(vector, common_pathway.iloc[3], color="b")
axes.plot(vector, common_pathway.iloc[4], color="m")
axes.plot(vector, common_pathway.iloc[5], color="c")
axes.plot(vector, common_pathway.iloc[6], color="k")
axes.set(xlabel='Hours', ylabel='Log concentration fold')
plt.legend(common_pathway.index)
plt.grid()


def read_gff(path):
    counter = 0
    with open('rrna_annotation.gff') as file:
        for line in file:
            if line[0] == '#':
                counter += 1
                continue
            else:
                break
    cols = ["chromosome", "source", "type", "start", "end", "score", "strand", "phase", "atributes"]
    tab = pd.read_csv(path, sep='\t', names=cols, skiprows=counter)
    return tab


def read_bed6(path):
    counter = 0
    with open('rrna_annotation.gff') as file:
        for line in file:
            if line[0] == '#':
                counter += 1
                continue
            else:
                break
    cols = ["chromosome", "start", "end", "name", "score", "strand"]
    tab = pd.read_csv(path, sep='\t', names=cols, skiprows=counter)
    return tab


gff = read_gff(r'rrna_annotation.gff')
# gff

bed = read_bed6('alignment.bed')
# bed
