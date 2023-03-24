import matplotlib . pyplot as plt

mylist = [1, 2, 3, 4, 3, 7, 3, 9, 1, 4] # create a list with
# 10 numbers of your choice
#plt . plot ( mylist ) # plot the list
plt.plot(mylist, 'o', color='green')
plt.plot(mylist )
plt . title (" This  is the  title ") # add title
plt . grid ( True ) # add grid lines to the plot
plt . xlabel ('this  is a  label  for  the x- axis') # label for x axis
plt . ylabel ('this  is a  label  for  the y- axis ') # label for y axis
plt . show ()

###############################################################################################
#
import matplotlib . pyplot as plt
mylist = [1, 2, 3, 4, 3, 7, 3, 9, 1, 4] # first list
mylist2 = [12 , 2, 7, 11, 8, 1, 3, 4, 9, 2] # second list
plt . plot ( mylist , ":", color ="g", linewidth =3) # plot the first list
# with a dotted line style , color it green . Add line - width .
plt . plot ( mylist2 , "--", color ="#FFA51F") # plot the second list
# with a dashed line style , color it orange
plt . show ()

#################################################################################################
import numpy as np
import matplotlib . pyplot as plt
random_list1 = np. random . randint (0, 25, 100) # create a random
# list of 100 integer numbers between 0 and 25
random_list2 = np. random . randint (0, 25, 100) # create a random
# list of 100 integer numbers between 0 and 25
random_list3 = np. random . randint (0, 25, 100) # create a random
# list of 100 integer numbers between 0 and 25
random_list4 = np. random . randint (0, 25, 100) # create a random
# list of 100 integer numbers between 0 and 25
plt . subplot (2, 2, 1) # this function uses three integers , here our
# subplot will be in a 2x2 plot , at position 1,
# which is top left .
plt . plot ( random_list1 , color ="c", linewidth =0.2)
plt . subplot (2, 2, 2) # in a 2x2 position 2 is top right
plt . plot ( random_list2 , color ="#D538FF", linewidth =1)
plt . subplot (2, 2, 3) # in a 2x2 position 3 is bottom left
plt . plot ( random_list3 , color =(232/255 ,71/255 ,31/255) , linewidth =0.5)
plt . subplot (2, 2, 4) # in a 2x2 position 4 is bottom right
plt . plot ( random_list4 , color ="black" , linewidth =2)
plt . show ()

#########################################################################################################

import numpy as np
xlinspace = np. linspace (0, 10,20)
random_list = np. random . randint (0, 25, 20)
print(random_list)
plt. plot ( xlinspace , random_list )
plt.show()

########################################################################################################

import numpy as np
import matplotlib . pyplot as plt
labels = [" John ", " Peter ", " Alice ", " Kate ", " David "]
# create a list of strings
ages = [22 , 25, 26, 23, 22] # create a list of numbers
x = np. linspace (20 ,30 ,5) # create an artificial x- axis
plt . plot (x, ages , "o") # plot your artificial axis and

# the ages list , use a circle marker
plt . xticks (x, labels , rotation ="30") # representation of x- axis .
# rotate the labels
plt . grid ( True ) # add grid lines
plt . title (" The age of my  classmates ") # add title
plt . xlabel ("classmates") # label for x- axis
plt . ylabel ("age") # label for y- axis
plt . show ()

###############################################################################################################

import numpy as np
import matplotlib . pyplot as plt
labels = [" John ", " Peter ", " Alice ", " Kate ", " David "]
# create a list of strings
ages = [22 , 25, 26, 23, 22] # list of ages
heights = [185 , 190 , 170 , 165 , 175] # list of heights in cm
xlinspace = np. linspace (1 ,200 ,5) # create an artificial x- axis
plt . plot ( xlinspace , ages , label ="Ages") # plot your artificial axis
# and the ages list , use a different marker
plt . xticks ( xlinspace , labels , rotation ="45") # representation of
# x- axis ; rotate the labels
plt . plot ( xlinspace , heights , label ="Heights") # plot your
# artificial axis and the heights list , use a different marker
plt . grid () # add grid lines
plt . title (" The age and  height  of my  classmates ") # add title
plt . xlabel ("classmates") # label for x- axis
plt . ylabel ("age and  height") # label for y- axis
plt . legend ( loc="upper right")
plt . show ()

#################################################################################################################