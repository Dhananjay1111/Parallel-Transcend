import numpy as np
import matplotlib . pyplot as plt

list = np. random . randint (1, 100 , 40)
print("list-",list)
# create a collection of 40 integer numbers and use it to
# create a numpy array

array = np. array ( list ) # create a numpy array
print ( "array-",array ) # print the array
print ( array . shape ) # print shape
print ( array . size ) # print size
print ( array . ndim ) # print " dim" attributes

#######################################################################################################################

array = np. empty (20 , dtype =np.float64)
# create an empty numpy array with 20 items of type float .

print("empty-",array)
array . fill (42) # all items must have as value the number 42.0.
print ( array )

array2 = array . reshape (4, 5)
# use the method . reshape () to turn this array into a two -dim
# array of 4 rows and 5 columns
print ( array2 . ndim ) # check number of dimensons
print ( array2 . shape ) # check shape
print ( array2 )

########################################################################################################################

array = np.arange(1,17,1)
array2 = array.reshape(4,4)
print(array2)

print(array2[3][3])
print(array2[2:3,-1])
print(array2[2:3, 1:])
print(array2[0:3, 3:])
print(array2[1:3,1:3])

########################################################################################################################



a = np. random . randint (0 ,255 ,900) # generate three arrays
b = np. random . randint (0 ,255 ,900)
c = np. random . randint (0 ,255 ,900)

array1 = a. reshape (30 ,30) # reshape to 30 x30
array2 = b. reshape (30 ,30)
array3 = c. reshape (30 ,30)

print ( array1 ) # print the arrays . Each represents one RGB channel
print ( array2 )
print ( array3 )

print ( array1 . shape ) # print the shape of the arrays
print ( array2 . shape )
print ( array3 . shape )

# Apply to each of the arrays a color scale according to the channel
# they represent . Pass a cmap parameter with a proper color map
# to the function imshow ()

plt . subplot (2, 2, 1)
plt . imshow ( array1 , cmap ="Greens")
# img1 = plt. imshow (array1 , cmap =" Greens ", interpolation =" nearest ")
    # interpolation

plt . subplot (2, 2, 2)
plt . imshow ( array2 , cmap ="Blues")
# img2 = plt. imshow (array1 , cmap =" Blues ", interpolation =" bicubic ")
# interpolation
plt . subplot (2, 2, 3)
plt . imshow ( array3 , cmap ="Wistia")
# img3 = plt. imshow (array1 , cmap =" Wistia ", interpolation =" bilinear ")
    # interpolation
d = np. dstack (( array1 , array2 , array3 )) # stack into a new array
    # the three RGB arrays , using np. dstack ()

print (d. shape ) # check whether the new array has correct size
    # and dimension (30 ,30 ,3)
plt . subplot (2, 2, 4)
plt . imshow (d. astype (np. uint8 ))
plt . show () # show the results


print("##############################################################################################################")

################
##  GEOSPATIAL 11.7 onwards
################
