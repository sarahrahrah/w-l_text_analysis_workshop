# Text Analysis with Python.  Tutorial Script #1
# This tutorial script uses the python programming language by itself without
# any external packages. Used with presentation to discuss variables, for loops
# if statements, strings, and functions in python.


# 1) Create a variable that holds our text

story = open( 'story.txt', mode='r', encoding='utf8').read()


# 2) Turn it into a list. 

listwords_story = story.split()


# 3) Initialize a separate list for the wordfrequencies.

wordfreq = []

# 4) Using a for loop, put entries into this new list.

for w in listwords_story:
    wordfreq.append(listwords_story.count(w))



# 5) Link the two lists together by creating a dictionary.
# Create the dictionary within the context of a function


def makeadictionary(listofwords, frequencyofwords):
    mynewdictionary = dict(zip(listofwords, frequencyofwords))
    return mynewdictionary

result = makeadictionary(listwords_story, wordfreq)


# 6) Show the word frequencies.


print (result)


# 7) Let's say we don't want to include very infrequent words. Let's add another if statement to
#filter the dictionary.

newresult = {}

for key, value in result.items():
    itemsinthisloop = {key:value}
    if value > 3:
        newresult.update(itemsinthisloop)

# this is actually more elegantly done with a list comprehension
# newresult = dict((key, value) for (key, value) in result.items() if value > 5)


# 8) Incorporate stopwords using a if statement
    

stopwords = ['the', 'a', 'in', 'was', 'there', 'for', 'but', 'that', 'this', 'he', 'or', 'on', 'as',
             'what', 'who','at','which','have','is', 'it','and','to','an','had','of','be','from']

newdict = {}

for key, value in newresult.items():
    iteminthisloop = {key:value}
    if key in stopwords:
        pass
    else:
        newdict.update(iteminthisloop)

# 9) Let's look at our new word frequencies.

print (newdict)

# 10) Let's divide our text into four quarters, and compare the word frequencies for the
#each section.

length = (len(listwords_story))

mod = length % 4
length = length - mod
quarter = length / 4
quarter = int(quarter)
print (quarter)

section1 = listwords_story[:quarter]
section2 = listwords_story[quarter:quarter*2]
section3 = listwords_story[quarter*2:quarter*3]
section4 = listwords_story[quarter*3:]

wordtocount = 'word'

section1count = section1.count(wordtocount)
print ("The count for " + wordtocount + " in Section 1 is : " + str(section1count))

section2count = section2.count(wordtocount)
print ("The count for " + wordtocount + " in Section 2 is : " + str(section2count))

section3count = section3.count(wordtocount)
print ("The count for " + wordtocount + " in Section 3 is : " + str(section3count))

section4count = section4.count(wordtocount)
print ("The count for " + wordtocount + " in Section 4 is : " + str(section4count))




