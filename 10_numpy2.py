import numpy as np
import matplotlib as plt



def read_one ( path ):
    band = np. loadtxt (path , delimiter =";")
    return band
path_file = r"X:\Scientific computing\Programming_Itc\Exercises\Exercise_11\2014_csv\2014_csv\2014_31.csv"
band = read_one ( path_file )
print (" Shape : ", band . shape )
print (" Size : ", band . size )
print (" Ndim : ", band . ndim )
print ("")
lowest = band .min ()
highest = band .max ()
idx_lowest = np. where ( band == lowest )
idx_highest = np. where ( band == highest )
print (" Indices  of the  lowest   values  ")
print ( idx_lowest )
print ("")
print (" Indices  of the  highest   values  ")
print ( idx_highest )