import nltk
from nltk.corpus import brown
import random

# usage: python3 brown.py 

# set seed for reproducibility

random.seed(1)

sentences = brown.tagged_sents(categories='romance')
mystery = brown.tagged_sents(categories='mystery')
sentences_romance = []
sentences_mystery = []

for i in sentences:
    if len(i) > 3:
        sentences_romance.append(i)

for i in mystery:
    if len(i) > 3:
        sentences_mystery.append(i)

# select 1000 random samples

random_romance = random.sample(sentences_romance, 1000)
random_mystery = random.sample(sentences_mystery, 1000)

romance_count = []
mystery_count = []

# count occurences of personal pronouns per sentence

for sentence in random_romance:
    personal_pronoun_count = 0
    
    for elem in sentence:
        
        if 'PPS' in elem[1]:
            personal_pronoun_count += 1
    romance_count.append(personal_pronoun_count)

for sentence in random_mystery:
    personal_pronoun_count = 0
    
    for elem in sentence:
        
        if 'PPS' in elem[1]:
            personal_pronoun_count += 1
    mystery_count.append(personal_pronoun_count)
    

# print the counts (vectors) to the screen

print(romance_count)
print(mystery_count)

