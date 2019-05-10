names = ['David', 'Peter', 'Michael', 'John', 'Bob']

namesLength = len(names)

for i in range(namesLength):
    theString = str(names[i], end = " and ")

##    charlist = list(theString)
##
##    yup = charList[:-9] #to erase the last " and None" string in charlist
##
##    yup2 = ''.join(yup)

print(theString)

##for i in range (len (names)):
##    print("{} {}".format(i + 2, names[i]))
