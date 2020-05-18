# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:10:27 2020

@author: theaddies
"""
output_file = './data/sentence_data.csv'
csvpath = './data/paragraph_1.txt'

letters =[]
words = []

import csv
import re
with open(csvpath, newline='') as f:
    reader = f.read()

sentences = re.split(' *[\.\?!][\'"\)\]]* *', reader)

numWords = len(reader.split(" "))
numSentences = len(sentences)


for char in reader:
    letters.append(char)

numLetter = len(letters)

print(numWords)
print(numSentences)
print(numLetter)