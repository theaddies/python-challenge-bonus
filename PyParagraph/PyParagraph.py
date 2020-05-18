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

avgLetter = round(len(letters) / numWords, 1)

avgWordsinSentence = round(numWords / numSentences , 1)

print("Paragraph analysis")
print("----------------------------------------")
print(f"Approximate Word Count: {numWords}")
print(f"Approximate Sentence Count: {numSentences}")
print(f"Average Letter Count: {avgLetter}")
print(f"Average Sentence length: {avgWordsinSentence}")