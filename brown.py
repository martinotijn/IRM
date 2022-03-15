import nltk
from nltk.corpus import brown
from nltk import Counter

mystery = {}
romance = {}


cfd = nltk.ConditionalFreqDist( (genre, word) for genre in brown.categories() for word in brown.words(categories=genre))
genre_word = [(genre, word) for genre in ['mystery', 'romance'] for word in brown.words(categories=genre)]
genres = ['romance', 'mystery']

modals = ["I", "you" ,"he", "she", "it", "we", "they", "them", "us", "him", "her", "his", "hers", "its", "theirs", "our", "your"]
wordcounts = Counter(brown.words(categories='romance'))
for i in modals:
    
    romance[i] = wordcounts[i]/len(wordcounts)
wordcounts = Counter(brown.words(categories='mystery'))

for i in modals:
    
    mystery[i] = wordcounts[i]/len(wordcounts)
    
print(mystery)
print(romance)


cfd.tabulate(conditions=genres, samples=modals)