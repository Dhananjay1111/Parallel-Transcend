

fruit = " apple " # assign a string to a variable
print (len ( fruit )) # print the length
print ("<" + fruit *10 + ">" ) # print the fruit 10 times and
# add delimiter symbols at the beginning and at the
# end of this long string
print("#######")



fruits = " apple " + " peach " + " melon " + " orange " # define a string
# with 4 fruits and concatenate them
print (len ( fruits )) # print the length
print (3* fruits ) # print it 3 times
print("#######")



fruits = " apple   pear   lemon   orange   kiwi " # 5 fruits separated by a
# space character
print ( fruits [::2]) # print characters every 2 steps
print ( fruits [::4]) # print characters every 4 steps
print ( fruits [:: -2]) # print using negative step
print ( fruits [:: -1]) # print using negative step

if "watermelon" == "waterMelon":
    print('true')
else:
    print('false')
d= "watermelon" == "waterMelon"
print(d)
g= "a" in "aladin"
print(g)


print('##################################################################')

j="pear***apple".isalnum()
print(j)

fruits = " pineapple   lemon   orange   kiwi ", "djfhkdjfhkjdf"
print(fruits)
list_characters = list ( fruits )

print (len ( list_characters ))



characters_str = "". join ( list_characters ) # list into single string
print ( characters_str )

separated_str = characters_str . replace (" "," ->")
print ( separated_str )


print('333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333')

fruits = "orange ->kiwi -> banana -> pineapple -> lemon "
print ( fruits )

list_fruits = fruits . split (" ->") # Converting a single string into list
print ( list_fruits )

print("Lund"*60)
del list_fruits [0]
print ( list_fruits )

fruits_str = " ". join ( list_fruits ) # converts list into single string
print ( fruits_str )

print ( fruits_str . replace ("*"," "))

for char in fruits : # iterate the list so every time you find a
            # vowel in it , the program prints the vowel
    if char in " aeiou ":
        print ( char )