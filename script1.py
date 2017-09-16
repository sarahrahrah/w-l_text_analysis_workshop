#Script to illustrate important concepts in python programming

# 1) VARIABLES
#-------------------------------------
#create a varible

breakfastfood = "omelettes"

# create another variable

number = 5

# 2) LISTS
#--------------------------------------
#put these variables into a list

anewlist = [breakfastfood, number]

# 3) BUILT-IN FUNCTIONS
#-------------------------------------
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


# 4) OPERATIONS
#______________________________________


# + addition and concatenation
# - subtraction
# * multiplication
# / divisions
# ** exponent
# % modulo (remainder in division)

print (number * 5)
print (breakfastfood * 5)


# 5) FOR LOOPS
#---------------------------------------

catbreeds = ["persian", "tabby", "sphinx", "domestic shorthair"]

for breed in catbreeds:
    print (breed)

# we can also declare for loops as below using indexing and the range()
# and len() functions

for breed in range(0, len(catbreeds)):
    print (catbreeds[breed])


# 6) WRITING FUNCTIONS
#________________________________________
def exclamation(word):
    wordwithexclamationmark = word + "!!!"
    return wordwithexclamationmark


result = exclamation("hello")

print (result)

# 7) BUILT-IN FUNCTIONS FOR LISTS
#-----------------------------------------

#count()
#append()
#remove()
#sort()

vegetables = ['broccoli', 'beets', 'cabbage', 'zucchini','peas', 'carrots','beets']

print (vegetables.count('beets'))

vegetables.remove('beets')

print (vegetables)

vegetables.append('cauliflower')

print (vegetables)

vegetables.sort()

print (vegetables)

# 8) IF STATEMENTS
#------------------------------------------

x = 2
if 2 * x == 5:
    print ("equals five!")
else:
    print ("does not!")

for vegetable in vegetables:
    if len(vegetable) > 6:
        print ("long word")
    else:
        print ("not that long of a word")



# 9) LIST INDICIES
#___________________________________________

cities = ['Tokyo','Moscow','Chicago','Barcelona']

print (cities[0])
print (cities[1:4])
print (cities[-1])

# 10) DICTIONARIES
#___________________________________________

countries = ['Japan','Russia','USA','Spain']
countriesandcities = dict(zip(countries, cities))

print (countriesandcities)



