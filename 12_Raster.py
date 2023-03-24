import osgeo.ogr
import os
from osgeo import gdal
from osgeo import gdal_array as gdarr
import matplotlib.pyplot as plt
import numpy as np

dataDirectory =r'X:\Scientific computing\Data'
# change to the data directory
os. chdir ( dataDirectory )

# open datasetclear
raster = gdal . Open ("2014.tif")

# getting driver name
dtype2 = raster.GetDriver().LongName
print (" driver   name :", dtype2 )
print ()

# getting raster size in two dimentions
x = raster . RasterXSize
y = raster . RasterYSize
print ("x  size : ", x, " y  size  ", y)
print ()

#getting meta data
meta = raster.GetMetadata()
print("raster metadata:", meta)
print()

# getting spatial projection
p = raster.GetProjection()
print("projection:", p)
print()

# getting geotransform info
g = raster . GetGeoTransform ()
print("g=", g)
print("g [0]",g[0])
print("g [1]",g[1])
print("g [2]",g[2])
print("g [3]",g[3])
if g is not None :
    print ("top - left  x:", g[0] , " top   left  y:", g [3])
    print ("pixel resolution - size  w-e(pixel width):", g[1] , "pixel resolution - size  n-s(pixel height, negative value):", g [5])
    print (" rotation  x:", g[2] , " rotation  y:", g [4])
    print ()

# getting bands
count = raster . RasterCount
print (" There   are  " + str ( count ) + "  bands ")
print ()

#######################################################################################################################

# Access to band information
# Determining band number 1 information and statistics:

band = raster.GetRasterBand(1)
min_ = band.GetMinimum()
max_ = band.GetMaximum()
print("min value:", min_, "max value", max_)
stats = band.GetStatistics(False, True)
# parameter 1: If TRUE statistics may be computed based on overviews.
# parameter 2: If FALSE statistics will be returned only if it can be done
# without rescanning the raster band
print('stat-', stats[0])
print('stat-', stats[1])
print('stat-', stats[2])
print('stat-', stats[3])
print("min = %.2f max = %.2f mean = %.2f std = %.2f" %
(stats[0], stats[1], stats[2], stats[3])) #.2f is float upto 2 digit after  decimal point
print("no data value:", band.GetNoDataValue())
print("number of overviews:", band.GetOverviewCount())

########################################################################################################################
#Convert from gdal to numpy

#Extraction of an individual pixel / single pixel


band = raster.GetRasterBand(1)
# use 0;0 for the topleft pixel; -1; -1 for the bottomright
xoff = 100 # sort of a starting point
yoff = 150

# use a window size of 1 pixel, this extracts one single pixel
win_xsize = 1 #size of pixel
win_ysize = 1
px = gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)
print(type(px))
print('shape', px.shape)
print('pixelvalue', px[0,0])
# Now it’s a numpyarray. Order is y, x or Rows, Columns

########################################################################################################################

#Extract a subset of one band

band = raster.GetRasterBand(1)
xoff = 0
yoff = 0
win_xsize = 273
win_ysize = 101
# read a single band as a 2D array
px = gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)
print(type(px))
print('shape', px.shape)
print('topleft', px[0,0])
# Now it’s a numpyarray! order is Y, X or Rows, Columns
print('bottomright', px[-1,-1])

########################################################################################################################

#Plot an image subset withmatplotlib

# use 0;0 for the topleft pixel; columns-1; rows-1 for the bottomright
xoff = 0
yoff = 0
win_xsize = 273
win_ysize = 101

px = gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)

#replace nodatavalue by None
px[px == -9999] = None
# or just use band.GetNoDataValue()

plt.imshow(px)
plt.show()

########################################################################################################################

#Extract entire dataset (all bands) as a 3-dim. array

raster = gdal . Open ("2014.tif")
# use 0;0 for the topleft pixel;
xoff = 0
yoff = 0
# window size in pixels
win_xsize = 273
win_ysize = 101
px = gdarr.DatasetReadAsArray(raster, xoff, yoff, win_xsize, win_ysize)
print(type(px))
print('shape', px.shape)
print('topleft', px[0,0,0])
# Now it’s a numpyarray. Order is -Day, y, x or Depth, Rows, Columns
print('bottomright', px[0,-1,-1])
#Now it’s a numpyarray. order is -Day, y, x or Depth, Rows, Columns

########################################################################################################################

#How to save a gdal raster image.
#Example converting from numpy to gdal.

band = raster.GetRasterBand(1)
xoff = 0
yoff = 0
win_xsize = 200
win_ysize = 200
arr= gdarr.BandReadAsArray(band, xoff, yoff, win_xsize, win_ysize)
driver=raster.GetDriver() # Use the same format as the original image
# or
driver = gdal.GetDriverByName('GTiff') # we can choose a diferent format e.g. XYZ
newRaster = driver.Create('2014_day1_subset.tif',arr.shape[1],arr.shape[0], 1, gdal.GDT_Float32)
prj = raster.GetProjection() # definenew raster dataset proj. & geotransform
newRaster.SetProjection(prj)
newRaster.SetGeoTransform(raster.GetGeoTransform())


# We can use the same GT because TL is same
newBand = newRaster.GetRasterBand(1) # get band 1 so we can fill it with data
newBand.WriteArray(arr) # write the array to the band
newBand.SetNoDataValue(-9999) # set a pixel nodata value
newBand.FlushCache() # flush the cache and clean memory
newBand = None
print("Finished!")

########################################################################################################################