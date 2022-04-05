# -*- coding: utf-8 -*-
"""Assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qndbyGV3Aqs-EDbOSvvod8qc7675rq04
"""

import json
import csv
import nltk 
nltk.download('stopwords')
nltk_stops = nltk.corpus.stopwords.words('english')
nltk.download("punkt")
from nltk import FreqDist
from nltk.util import ngrams
from nltk.collocations import *

with open("NLP_Assignment1_Source.json") as f: 
    overall_list = []
    total = 0
    average = 0
    rounds = 0
    country_dic = {}
    master_list = []

    for line in f:
        csv_line = []
        x = json.loads(line)

        # These are the fields of the data 
        csv_line.append(str(x["thread"]["social"]["facebook"]))
        csv_line.append(x["title"])
        csv_line.append(x["published"])
        csv_line.append(str(x["thread"]["replies_count"]))
        csv_line.append(x["author"])
        csv_line.append(x["url"])
        csv_line.append(x["thread"]["country"])
        total = total + len(x["text"])
        average = average + x["thread"]["replies_count"]
        token = nltk.word_tokenize(x["text"])
        token_lower = [w.lower() for w in token]
        csv_line.append(" ".join(token_lower))
        master_list.extend(token_lower)

        overall_list.append(csv_line)
        rounds = rounds + 1

        if x["thread"]["country"] in country_dic:
            country_dic[x["thread"]["country"]] += 1
        else:
            country_dic[x["thread"]["country"]] = 1

        country_dic[x["thread"]["country"]] = country_dic[x["thread"]["country"]] + 1
filename = "nlp_ass1.csv"
fields = ['facebook', 'title', 'published', 'replies_count', 'author', 'url', 'country', 'text']
print("number of extries:", rounds)
print("avg_length_text:", (total/rounds))
print(country_dic)
print("Average Number of Replies:", average/rounds)

with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(overall_list)

# Frequency Question Part 3

# original amount of tokens 
print(len(master_list))
token_isotope = [w for w in master_list if w.isalpha()]
token_stop = [w for w in token_isotope if w not in nltk_stops]

# number of tokens after stop words, numbers, and punctuations removed 
print(len(token_stop))

# Caculating frequency 
fdist = FreqDist(token_stop)
topkeys = fdist.most_common(50)
fdist.plot(50, title="Top 50 Tokens by Frequency")
print(topkeys)

# turning frequency in percentages
for i in topkeys: 
  x= i[1] / len(token_stop)
  print(i[0], x)

import re
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(master_list)

def alpha_filter(w):
  # pattern to match word of non-alphabetical characters
  pattern = re.compile('^[^a-z]+$')
  if (pattern.match(w)):
    return True
  else:
    return False
    
finder.apply_word_filter(alpha_filter)
finder.apply_word_filter(lambda w: w in nltk_stops)
scored = finder.score_ngrams(bigram_measures.raw_freq)
for bscore in scored[:50]:
    print (bscore)

finder.apply_freq_filter(5)
scored = finder.score_ngrams(bigram_measures.pmi)
for bscore in scored[:50]:
    print (bscore)

# contents/context

text = nltk.Text(token_stop)
#text.concordance("coronavirus")
text.similar('coronavirus')
text.similar('vaccine')
text.similar('outbreak')
