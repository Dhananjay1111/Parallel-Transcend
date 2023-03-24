from osgeo import ogr , gdal , gdal_array as gdarr
import numpy as np
import os

#
# Extract a raster subset from the dataset 2014.tif using the boundary of the
# province of Overijssel. Save the results as a new raster with the same projection
# as 2014.tif.

dataDirectory =r'X:\Scientific computing\Data\14_raster-vector_integration_data'
os. chdir ( dataDirectory )


# subset only Overijssel Temperatures
overTemperatureDs = gdal . Warp ('2014_amsterdam.tif', "2014.tif",
    format =" GTiff ", dstSRS ='EPSG:28992',
    cutlineDSName ='NL_provinces.shp',
    cutlineWhere =" NAME_1  = 'Overijssel'",
    dstNodata = -9999 ,
    cropToCutline = True ,
    outputType = gdal . GDT_Float32 )
overTemperatureDs = None

########################################################################################################################
#
# Rasterize ovRoads.geojson and save it as a new Gtiff le with the same
# characteristics as 2014.tif. Ensure that pixel values in this new raster correspond
# with the number of vehicles per hour allowed in each road.

# subset only Overijssel Temperatures to use later as a reference
overTemperatureDs = gdal . Warp ('', "2014.tif",format ="Mem",
dstSRS ='EPSG:28992', cutlineDSName ='NL_provinces.shp',
cutlineWhere =" NAME_1  = 'Overijssel'", dstNodata = -9999 ,
cropToCutline = True , outputType = gdal . GDT_Float32 )
overTempArray = gdarr . DatasetReadAsArray ( overTemperatureDs , 0, 0,
overTemperatureDs . RasterXSize , overTemperatureDs . RasterYSize )

# prepare for Rasterize
memDriver = gdal . GetDriverByName ('GTiff')
roadsRasterDs = memDriver . Create ('roads_cars_per_hour.tif',
overTemperatureDs . RasterXSize ,
overTemperatureDs . RasterYSize ,
1, gdal . GDT_Float32 )
roadsRasterDs . SetProjection ( overTemperatureDs . GetProjection ())
         # set projection
roadsRasterDs . SetGeoTransform ( overTemperatureDs . GetGeoTransform ())
         # set geotransform

# create 1 band and set the nodata value
outband1 = roadsRasterDs . GetRasterBand (1)
outband1 . SetNoDataValue (0)

roadsVectorDs = ogr . Open ("ovRoads.geojson")
roadsLayer = roadsVectorDs . GetLayer ()

# Rasterize A1 road in Overijssel
gdal . RasterizeLayer ( roadsRasterDs , [1] , roadsLayer ,
    options =[ 'ATTRIBUTE = vehic_p_hour'])
outband1 . FlushCache ()
outband1 = None
roadsRasterDs = None

#######################################################################################################################
# #
# # In the lecture, using gdal, ogr and numpy, we were able to answer the question:
# # What are the lowest temperatures experienced in 2014 along motorway A1 in the
# # province of Overijssel?
# # Using similar steps, try to nd what are the highest temperatures felt in 2014
# # along that road in the province of Overijssel.
# # Note: In the lecture, to answer this question we removed values equal to -9999,
# # by using a numpy ltering mechanism:
# # roadsMinTemperature[roadsMinTemperature == -9999] = None
# # In this exercise, you will need to remove all values that are below or equal to
# # 0, using a similar technique.


# subset only Overijssel Temperatures
overTemperatureDs = gdal . Warp ('', "2014.tif",format ="Mem",
    dstSRS ='EPSG:28992',
    cutlineDSName ='NL_provinces.shp',
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

# ########################################################################################################################

#
# Save the highest temperatures experienced in 2014 along the road as a Gtiff
# raster file, in which pixels represent the highest temperature recorded. Ensure
# that this file has the same characteristics as 2014.tif.

# Subset only Overijssel Temperatures
overTemperatureDs = gdal . Warp ('', "2014.tif",
format ="Mem",
dstSRS ='EPSG:28992',
cutlineDSName ='NL_provinces.shp',
cutlineWhere =" NAME_1  = 'Overijssel'",
dstNodata = -9999 ,cropToCutline = True ,
outputType = gdal . GDT_Float32 )
overTempArray = gdarr . DatasetReadAsArray ( overTemperatureDs ,
0, 0, overTemperatureDs . RasterXSize ,
overTemperatureDs . RasterYSize )

# Prepare for Rasterize Road A1
memDriver = gdal . GetDriverByName ('Mem')
roadsRasterDs = memDriver . Create ('', overTemperatureDs .
RasterXSize , overTemperatureDs . RasterYSize ,1,
gdal . GDT_Float32 )
roadsRasterDs . SetProjection ( overTemperatureDs . GetProjection ())
# set projection
roadsRasterDs . SetGeoTransform ( overTemperatureDs . GetGeoTransform ())
# set geotrasform

# create 1 band and set the nodata value
outband1 = roadsRasterDs . GetRasterBand (1)
outband1 . SetNoDataValue (0)

roadsVectorDs = ogr . Open ("ovRoads.geojson")
roadsLayer = roadsVectorDs . GetLayer ()
roadsLayer . SetAttributeFilter ("id = 'A1 '")

# rasterize A1 road in Overijssel
gdal . RasterizeLayer ( roadsRasterDs , [1] , roadsLayer ,
burn_values =[1] , options =[ ' ALL_TOUCHED = TRUE '])
roadsArray = gdarr . DatasetReadAsArray ( roadsRasterDs , 0, 0,
roadsRasterDs . RasterXSize , roadsRasterDs . RasterYSize )

# multiply roads by temperature . The output will be temperatures .
roadsTemperature = roadsArray * overTempArray

# compute lower temperatures
roadsMaxTemperature =np. max ( roadsTemperature , axis =0)

# remove values below 0
roadsMaxTemperature [ roadsMaxTemperature <=0 ] = None

# create the new dataset
gtiffDriver = gdal . GetDriverByName ('Gtiff')
highestTempRoadsDs = gtiffDriver . Create ('roadHighestTemp.tif',
overTemperatureDs . RasterXSize ,
overTemperatureDs . RasterYSize ,
1, gdal . GDT_Float32 )
highestTempRoadsDs . SetProjection ( overTemperatureDs . GetProjection ())
# set projection
highestTempRoadsDs . SetGeoTransform ( overTemperatureDs . GetGeoTransform ())
# set geotransform

# create 1 band and set the nodata value
highestTempRoadsband1 = highestTempRoadsDs . GetRasterBand (1)
highestTempRoadsband1 . SetNoDataValue ( -9999)
# add numpy into the band
highestTempRoadsband1 . WriteArray ( roadsMaxTemperature )

# clean an close the dataset
highestTempRoadsband1 . FlushCache ()
highestTempRoadsDs = None

#######################################################################################################################
