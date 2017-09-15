# Text Analysis with Python.  Tutorial Script #2
# This tutorial script brings in the packages nltk and matplotlib to explore
# some further functionality with python.


# 1) Import the python packages matplotlib and nltk
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import ne_chunk
from nltk.corpus import stopwords
from nltk.util import ngrams


# 2)  Let's open our text again.

story = open( 'story.txt', mode='r', encoding='utf8').read()

# 3) Tokenize -- NLTK allows your to tokenize sentences or words easily.

storywordtokens = word_tokenize(story)

#print (storywordtokens)

storysentencetokens = sent_tokenize(story)

# 4) Stopwords - NLTK has stopword lists available for numerous languages.

stoplist = stopwords.words('english')

newstorywordtokens = [word for word in storywordtokens if word not in stoplist]


# 5) Rare words, common words, and frequency distribtuion

freq_dist = nltk.FreqDist(newstorywordtokens)

rarewords = list(freq_dist.keys())[-50:]

print (freq_dist.most_common(50))


#print (rarewords)



# 6) Parts of speech tagging

partsofspeech = nltk.pos_tag(newstorywordtokens)

##this function creates a list of tuples.


#print (partsofspeech)

#print (type(partsofspeech[1]))


# 7) Named entity recognition
# In order to do this, the word_tokenize and pos_tag functions must be applied first.

ne = ne_chunk(partsofspeech)

#print (ne)


# 8) N-grams in nltk

bigrams = list(ngrams(newstorywordtokens,2))
trigrams = ngrams(newstorywordtokens,3)

print (bigrams)


# 9) Plotting sentence length as a histogram with matplotlib
lengthsarray = []

for x in storysentencetokens:
    length = len(x)
    lengthsarray.append(length)

print (lengthsarray)
plt.hist(lengthsarray)


# 10) Add some labels to the plot

xaxislabel = 'Number of characters in sentence.'
yaxislabel = 'Frequency'
title = 'Sentence Length in My Text'
plt.xlabel(xaxislabel)
plt.ylabel(yaxislabel)
plt.title(title)
plt.show()












