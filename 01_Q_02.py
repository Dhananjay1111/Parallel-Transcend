import os
import csv
import  math
import string
import osgeo.ogr
import numpy as np
import pandas as pd
from osgeo import osr
from osgeo import gdal
import matplotlib.pyplot as plt
from osgeo import ogr , gdal , gdal_array as gdarr

##
# Dhananjay Umalkar
##

#####
# Q2 (2.1)
# Area = 0 (it is anon-surface geometry type)
#####

dataDirectory =r'X:\Scientific computing\Data\14_raster-vector_integration_data'
os. chdir ( dataDirectory )


roadsVectorDs = ogr . Open ("ovRoads.geojson")
roadsLayer = roadsVectorDs . GetLayer (0)
roadsLayer . SetAttributeFilter ("id = 'A1'")

for feature in roadsLayer :
    OverijsselFeature = feature
    # extract into a variable

OverijsselGeometry = OverijsselFeature . GetGeometryRef ()
    # extract the geometry

# Create a buffer of 1000 m
OverijsselBuffer = OverijsselGeometry . Buffer (1000)

print(OverijsselBuffer)

# Area
area = OverijsselGeometry . Area () # get the area in projection units
print ("Area  is:  %.0f" % ( area ))

######################################################################################################################

####
# 2.2
####


# set up the shapefile driver
driver = ogr. GetDriverByName ("ESRI Shapefile")
# create the data source
data_source = driver . CreateDataSource ("Buffer.shp")

# create the spatial reference , EPSG 28992
srs = osr. SpatialReference ()
srs . ImportFromEPSG (28992)

# create the layer
layer = data_source . CreateLayer (" OverijsselBuffer ", srs , ogr. wkbPolygon )

# Add fields and create one field called Name
field_name = ogr. FieldDefn ("Name", ogr. OFTString )
field_name . SetWidth (24)
layer . CreateField ( field_name )

# Add one more field called Area with type real
field_area = ogr. FieldDefn ("Area", ogr. OFTReal )
field_area . SetWidth (32)
field_area . SetPrecision (2) # added line to set precision
layer . CreateField ( field_area )
feature = ogr. Feature ( layer . GetLayerDefn ())
feature . SetField ("Name", "Overijssel Buffer")
feature . SetField ("Area", OverijsselBuffer.Area ())
feature . SetGeometry ( OverijsselBuffer )
layer . CreateFeature ( feature )
feature = None # dereference the feature
data_source = None # save and close the data source

########################################################################################################################

#######
# 2.3
#######

#################################
# Highest temperature = 33.46942
# Lowest temperature  = 33.452934
#################################

# whole Buffer.shp is of Overijssel province, So no need to specify NAME_1


# subset only Overijssel Temperatures
overTemperatureDs = gdal . Warp ('', "2014.tif",format ="Mem",
    dstSRS ='EPSG:28992',
    cutlineDSName ='Buffer.shp',
    cutlineWhere =" NAME_1  = 'Overijssel'",
dstNodata = -9999 , cropToCutline = True , outputType = gdal . GDT_Float32 )
overTempArray = gdarr . DatasetReadAsArray ( overTemperatureDs , 0, 0,
overTemperatureDs . RasterXSize , overTemperatureDs . RasterYSize )

# prepare for Rasterize Road A1
memDriver = gdal . GetDriverByName ('Mem')
roadsRasterDs = memDriver . Create ('', overTemperatureDs . RasterXSize ,
overTemperatureDs . RasterYSize ,1, gdal . GDT_Float32 )
roadsRasterDs . SetProjection ( overTemperatureDs . GetProjection ())
       # set projection

roadsRasterDs . SetGeoTransform ( overTemperatureDs . GetGeoTransform ())
       # set geotransform

# create 1 band and set the nodata value
outband1 = roadsRasterDs . GetRasterBand (1)
outband1 . SetNoDataValue (0)
roadsVectorDs = ogr . Open ("ovRoads.geojson")
roadsLayer = roadsVectorDs . GetLayer ()
roadsLayer . SetAttributeFilter ("id = 'A1'")

# rasterize A1 road in Overijssel
gdal . RasterizeLayer ( roadsRasterDs , [1] , roadsLayer , burn_values =[1] ,
options =[ ' ALL_TOUCHED = TRUE '])
roadsArray = gdarr . DatasetReadAsArray ( roadsRasterDs , 0, 0,
roadsRasterDs . RasterXSize , roadsRasterDs . RasterYSize )

overTemperatureDs = None
roadsVectorDs = None
roadsRasterDs = None
print ('A1  road   shape :', roadsArray . shape )
print ('Overijssel   temperature   shape :', overTempArray . shape )

# multiply roads by temperature . The output will be temperatures .
roadsTemperature = roadsArray * overTempArray
print ('A1  road   temperatures   shape :', roadsTemperature . shape )

# compute highest temperatures
roadsMaxTemperature =np. max ( roadsTemperature , axis =0)
print ('A1  highest   temperatures   shape ', roadsMaxTemperature . shape )

# removing
roadsMaxTemperature [ roadsMaxTemperature <=0 ] = None
minLowerTemp =np. nanmin ( roadsMaxTemperature )
maxLowerTemp =np. nanmax ( roadsMaxTemperature )
print ('Highest   temperatures   recorded  in  2014  in A1 in  Overijssel are   between :',minLowerTemp ,'  and  ', maxLowerTemp )

################################################################################################################################