#follow along sidescript for important concepts to show class

# create a varible

breakfastfood = "omelettes"

# create another variable

number = 5

# put these variables into a list

anewlist = [breakfastfood, number]

# various python built-in functions

#print ()
#len()
#int()
#str()
#type()

print (anewlist)

print (len(anewlist))

# The following wont work because the variable number needs to be turned
#into a string
#print ("Number of " + breakfastfood + " : " + number)

print ("Number of " + breakfastfood + " : " + str(number))


print (type(anewlist))
print (type(number))
print (type(breakfastfood))


# for loop

catbreeds = ["persian", "tabby", "sphinx", "domestic shorthair"]

for breed in catbreeds:
    print (breed)

# we can also declare for loops as below using indexing and the range()
# and len() functions

for breed in range(0, len(catbreeds)):
    print (catbreeds[breed])


# writing your own function

def exclamationcats(catlist):
    catstring = ''
    for breed in catlist:
        catstring = catstring + breed + "!!! "
    return catstring


result = exclamationcats(catbreeds)

print (result)


#  Built-in list functions

#count()
#append()
#remove()
#sort()

vegetables = ['broccoli', 'beets', 'cabbage', 'zucchini', 'carrots','beets']

print (vegetables.count('beets'))

vegetables.remove('beets')

print (vegetables)

vegetables.append('cauliflower')

print (vegetables)

vegetables.sort()

print (vegetables)

# list indexing

cities = ['Tokyo','Moscow','Chicago','Madrid']

print (cities[0])
print (cities[1:4])
print (cities[-1])

#dictionaries

countries = ['Japan','Russia','USA','Spain']
countriesandcapitals = dict(zip(countries, cities))

print (countriesandcapitals)



