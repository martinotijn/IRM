import nltk
from nltk.corpus import brown
from nltk import Counter
import random
mystery = {}
romance = {}

random.seed(1)
cfd = nltk.ConditionalFreqDist( (genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genre_word = [(genre, word) for genre in ['mystery', 'romance'] for word in brown.words(categories=genre)]
genres = ['romance', 'mystery']

modals = ['i', 'me', 'you', 'he', 'him', 'she', 'her', 'it', 'we', 'us', 'they', 'them', 'one','I', 'Me', 'You', 'He', 'Him', 'She', 'Her', 'It', 'We', 'Us', 'They', 'Them', 'One']
sentences = brown.tagged_sents(tagset='universal', categories='romance')

print(len(sentences))
mystery = brown.sents(categories='mystery')
sentences_romance = []
sentences_mystery = []
for i in sentences:
    if len(i) > 8 and len(i) < 10:
        sentences_romance.append(i)
        
print(len(sentences_romance))

for i in mystery:
    if len(i) > 6 and len(i) < 10:
        sentences_mystery.append(i)
        
print(len(sentences_mystery))

random_romance = random.sample(sentences_romance, 100)
random_mystery = random.sample(sentences_mystery, 100)

count_romance = []
count_mystery = []
for i in random_romance:
    count_romance.append(sum(el in i for el in modals))

for i in random_mystery:
    print(i)
    count_mystery.append(sum(el in i for el in modals))

print(sentences[0])

print(count_mystery)