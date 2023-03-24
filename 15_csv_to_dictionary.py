from osgeo import ogr , gdal , gdal_array as gdarr
import numpy as np
import os
import csv
import string
import pandas as pd


dataDirectory =r'X:\Scientific computing\Data'
os. chdir ( dataDirectory )

def read_csv_file ( file_path ):
    data = []
    file = open ( file_path )
    csv_reader = csv. reader ( file )
    for row in csv_reader :
        data . append (row)
    return data

csv_file= read_csv_file('customers.csv')
print(csv_file)

dict = {}
for row in csv_file:
    key= row[0]
    value= [row[1], row[2]]
    dict[key]= value
print(dict)
print(dict.keys())
################################################
a_file = open("sample.csv", "w")

writer = csv.writer(a_file)
for key, value in dict.items():
    writer.writerow([key, value])
a_file.close()
#################################################

def store_dict ( dictionary , file_path ):
    file = open ( file_path , "w")
    for key in dictionary :
        file . write ("%s:%i\n" %(key, dictionary[key]))
    file.close ()
store_dict (dict, "abhi_abhi.csv")
#####################################################

a= 18.787
print("%.2f"% a)