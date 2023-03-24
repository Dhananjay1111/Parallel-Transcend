import os
import csv
import  math
import string
import osgeo.ogr
import numpy as np
import pandas as pd
from osgeo import gdal
import matplotlib.pyplot as plt
from osgeo import ogr , gdal , gdal_array as gdarr


#########
# Q1   1.1
#########

# As we are interested in only low and high confidence level, we loop over the values 2 and 3 only.
# For that  we need to access the pix_values list which is in form of matrix
# with pix_values[i][j], with 'i' we reach the row and with 'j' we reach the column.
# after accesing the values, we apply condition values != 0 and 1.
# then we insert these new values in empty list sparse_matrix

########
#  1.2
########

pix_values = [[0, 1, 0, 3, 3, 2, 1, 2, 0, 0],
              [0, 0, 0, 2, 0, 1, 0, 1, 3, 0],
             [2, 3, 0, 0, 0, 3, 1, 0, 3, 0],
              [0, 1, 0, 0, 0, 2, 3, 3, 0, 3],
             [1, 0, 0, 1, 0, 3, 1, 1, 1, 2],
              [0, 0, 2, 3, 0, 2, 3, 0, 0, 0],
             [1, 3, 3, 0, 0, 1, 3, 0, 0, 1],
              [2, 0, 1, 2, 0, 2, 0, 0, 0, 1],
             [3, 2, 3, 0, 2, 0, 3, 2, 2, 0]]

rows = 9
column = 10
sparse_matrix = []

for i in range(rows):
    for j in range(column):
        if pix_values[i][j]>1:
            sparse_matrix.append(pix_values[i][j])
print("Low and high values==",sparse_matrix)

###########
#   1.3
###########

rows = 9
column = 10
low_confidence = []
High_confidence = []

for i in range(rows):
    for j in range(column):
        if pix_values[i][j] == 2:
            low_confidence.append(pix_values[i][j])
        elif pix_values[i][j] == 3:
            High_confidence.append(pix_values[i][j])
print("low_confidence==", low_confidence)
print("High_confidence==", High_confidence)

#######################################################################################################################