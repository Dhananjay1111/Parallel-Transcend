from osgeo import ogr
from osgeo import osr
import os

#
# using the ogr library , open file nl_provinces . shp and print the
# following information :
#     driver name
#     data source metadata
#     number of layers

#

dataDirectory =r"X:\Scientific computing\Data\data_OGR"
# change to the data directory
os. chdir ( dataDirectory )
datasource = ogr. Open ("NL_provinces.shp")

# get driver
driverType = datasource . GetDriver (). GetName ()
print (" Driver   name : "+ driverType )

# get metadata
meta = datasource . GetMetadata ()
print (" Raster   metadata :", meta )

# get layer count
layerCount = datasource . GetLayerCount ()
print (" Number  of  layers :", layerCount )

########################################################################################################################

# # With file NL_provinces .shp access the first layer data source using
# # . GetLayer () and print the following information :
# # The number of attribute table fields
# # Iterate over the attribute table fields , and print all their names
# # Layer extents
# # Number of features
# # Spatial reference system
# ##

dataDirectory =r"X:\Scientific computing\Data\data_OGR"
os. chdir ( dataDirectory )

datasource = ogr. Open ("NL_provinces.shp")
layer = datasource . GetLayer (0)
# get the first layer ( shapefile has only 1 layer )

# Layer definition / atribute table fields
layerDefinition = layer . GetLayerDefn ()
fieldCount = layerDefinition . GetFieldCount ()
print ("Number  of  fields : ", fieldCount )
for i in range ( fieldCount ):
    print ("Atribute   field : "+ layerDefinition . GetFieldDefn (i). GetName ())

# Layer extents
layerExtents = layer . GetExtent ()
print("x_min  =  %.2f  x_max  = %.2f  y_min  = %.2f  y_max  = %.2f"%
      ( layerExtents [0] , layerExtents [1] , layerExtents [2] , layerExtents[3]))
# print only 2 decimal digits of float value

# Number of features
layerFeatureNum = layer . GetFeatureCount ()
print ("Number  of  features : ", layerFeatureNum )

# Spatial reference system
layerSRS = layer . GetSpatialRef ()
print ("Spatial   Reference   System  (srs ): ", layerSRS )

# #########################################################################################################################

# Iterate over the features , and print their value for the
# field NAME_1 . You can access such value with the command
# . GetFieldAsString () method inside the loop .


dataDirectory =r"X:\Scientific computing\Data\data_OGR"
os. chdir ( dataDirectory )

datasource = ogr. Open ("NL_provinces.shp")
layer = datasource . GetLayer (0)
# get the first layer ( shapefile has only 1 layer )

for i in range ( layer . GetFeatureCount ()): # iterate the features
    feature = layer . GetFeature (i) #get the feature i
    nameFeature = feature . GetFieldAsString ("NAME_1")
    print ("Iteration  ", i, "feature   NAME_1 : ", nameFeature )

#########################################################################################################################
# #
# With a filter on the layer , using the method . SetAttributeFilter (),
# extract the feature for the province of Overijssel ( mark correct
# spelling ) and print the following for this feature :
# NAME_1 value
# Type of geometry
# Geometry in well - known text format
# Area
# Extent

dataDirectory =r"X:\Scientific computing\Data\data_OGR"
os. chdir ( dataDirectory )

datasource = ogr. Open ("NL_provinces.shp")
layer = datasource . GetLayer (0)
# get the first layer ( shapefile has only 1 layer )

layer . SetAttributeFilter (" NAME_1  = 'Overijssel'")

for feature in layer :
    OverijsselFeature = feature # extract into a variable

# NAME_1 field value
name = OverijsselFeature . GetField ("NAME_1")
print ("Name_1   for  selected   feature : "+ name )

# Type of geometry
OverijsselGeometry = OverijsselFeature . GetGeometryRef ()

# extract the geometry
print ("Type  of  Geometry : "+ OverijsselGeometry . GetGeometryName ())

# Geometry in WKT
print ("Buffer   Geometry  WKT : "+ OverijsselGeometry . ExportToWkt ()) # geometry as text

# Area
area = OverijsselGeometry . Area () # get the area in projection units
print ("Area  is:  %.0f" % ( area ))

# Feature extents
env = OverijsselGeometry . GetEnvelope () # get the envelope ( bbox )
print ("Feature   extent :  x_min  = %.2f  x_max  = %.2f  y_min  = %.2f y_max  = %.2f"
       % (env [0] , env [1] , env [2] , env [3]))

########################################################################################################################

#
# Access the feature geometry of Overijssel province and then create
# a buffer of 5 ,000 meters for this province . Print its geometry in WKT
# and also as a JSON object .

##

dataDirectory =r"X:\Scientific computing\Data\data_OGR"
os. chdir ( dataDirectory )

datasource = ogr. Open ("NL_provinces.shp")
layer = datasource . GetLayer (0)
# get the first layer ( shapefile has only 1 layer )

layer . SetAttributeFilter (" NAME_1  = 'Overijssel'")

for feature in layer :
    OverijsselFeature = feature # extract into a variable

OverijsselGeometry = OverijsselFeature . GetGeometryRef ()
# extract the geometry

# Create a buffer of 5000 m
OverijsselBuffer = OverijsselGeometry . Buffer (5000)

# Geometry in WKT
print ("Buffer   Geometry  WKT : "+ OverijsselBuffer . ExportToWkt ())
# geometry as text

print ("Buffer   Geometry   Json  : "+ OverijsselBuffer . ExportToJson ())
# geometry as json

#######################################################################################################################
#Save the calculated buffer as a new shapefile , and name it properly

# set up the shapefile driver
driver = ogr. GetDriverByName ("ESRI Shapefile")
# create the data source
data_source = driver . CreateDataSource ("OverijsselBuffer.shp")

# create the spatial reference , EPSG 28992
srs = osr. SpatialReference ()
srs . ImportFromEPSG (28992)

# create the layer
layer = data_source . CreateLayer (" province_buffer ", srs , ogr. wkbPolygon )
layer = data_source . CreateLayer (" OverijsselBuffer ", srs , ogr. wkbPolygon )

# Add fields and create one field called Name
field_name = ogr. FieldDefn ("Name", ogr. OFTString )
field_name . SetWidth (24)
layer . CreateField ( field_name )

# Add one more field called Area with type real
field_area = ogr. FieldDefn (" Area ", ogr. OFTReal )
field_area . SetWidth (32)
field_area . SetPrecision (2) # added line to set precision
layer . CreateField ( field_area )
feature = ogr. Feature ( layer . GetLayerDefn ())
feature . SetField (" Name ", "Overijssel Buffer")
feature . SetField (" Area ", OverijsselBuffer.Area ())
feature . SetGeometry ( OverijsselBuffer )
layer . CreateFeature ( feature )
feature = None # dereference the feature
data_source = None # save and close the data source

########################################################################################################################

#Extract the feature geometry of Drenthe province , and with the
# previous buffer from the Overijssel geometry , check whether this it
# intersects Drenthe . If they do , calculate the intersection geometry ,
# and save it too as a new shapefile

dataDirectory =r"X:\Scientific computing\Data\data_OGR"
os. chdir ( dataDirectory )

datasource = ogr. Open ("NL_provinces.shp")
layer = datasource . GetLayer (0)
# get the first layer ( shapefile has only 1 layer )

layer . SetAttributeFilter (" NAME_1  = 'Overijssel'")
for feature in layer :
    OverijsselFeature = feature # extract into a variable
    OverijsselGeometry = OverijsselFeature . GetGeometryRef ()

# Create a buffer of 5000 m
OverijsselBuffer = OverijsselGeometry . Buffer (5000)

# Get feature ’s geometry for Drenthe
layer . SetAttributeFilter (" NAME_1  = 'Drenthe'")

for feature in layer :
    DrentheFeature = feature # extract into a variable
    DrentheGeometry = DrentheFeature . GetGeometryRef ()

# Check if Overijssel buffer intersects with Drenthe geometry
if OverijsselBuffer . Intersects ( DrentheGeometry ):
    DOIntersection = OverijsselBuffer . Intersection ( DrentheGeometry )

# Calculate intersection geometry
print ("Geometry   WKT : "+ DOIntersection . ExportToWkt ())

# Save intersection as shp
from osgeo import osr

# set up the shapefile driver
driver = ogr. GetDriverByName (" ESRI   Shapefile ")
# create the data source
data_source = driver . CreateDataSource ("DOIntersection.shp")

# create the spatial reference , EPSG 28992
srs = osr. SpatialReference ()
srs . ImportFromEPSG (28992)

# create the layer
layer = data_source . CreateLayer (" DOIntersection ", srs , ogr. wkbPolygon )

# Add fields and create one field called Name
field_name = ogr. FieldDefn (" Name ", ogr. OFTString )
field_name . SetWidth (24)
layer . CreateField ( field_name )

# Add one more field called Area with type real
field_area = ogr. FieldDefn (" Area ", ogr. OFTReal )
field_area . SetWidth (32)
field_area . SetPrecision (2) # added line to set precision
layer . CreateField ( field_area )
feature = ogr. Feature ( layer . GetLayerDefn ())
feature . SetField (" Name ", "DO  Intersection")
feature . SetField (" Area ", DOIntersection . Area ())
feature . SetGeometry ( DOIntersection )
layer . CreateFeature ( feature )
feature = None # dereference the feature
data_source = None # save and close the data source

##########################################################################################################################

# Open two datasets ( Texel_Polygons .shp and Texel_Points .shp)
# print their respective number of features and spatial reference
# identifiers .

#

dataDirectory =r"X:\Scientific computing\Data\data_OGR"

# Change data directory
os. chdir ( dataDirectory )
PointsDataset = ogr. Open ("Texel_Points.shp")
PolygonsDataset = ogr. Open ("Texel_Polygons.shp")

# Get layer
PointsLayer = PointsDataset . GetLayer (0)
PolygonsLayer = PolygonsDataset . GetLayer (0)

# Point features Count and CRS
print ("Point   Features  -  Number  of  features : ",
PointsLayer . GetFeatureCount ())
print ("Point   Features  -  Coordinate   system  is: ",
PointsLayer . GetSpatialRef ())

# Polygon features Count and CRS
print ("Polygon   Features  -  Number  of  features : ",
PolygonsLayer . GetFeatureCount ())
print ("Polygon   Features  -  Coordinate   system  is: ",
PolygonsLayer . GetSpatialRef ())

########################################################################################################################

# Fetch the 25 th point feature and the 2nd polygon feature from the
# vector layers and then print their geometry .
# Calculate the distance between the point and polygon features

##
# Get 25 th point Feature and Geometry
PointsFeature = PointsLayer . GetFeature (24)
PointsGeometry = PointsFeature . GetGeometryRef ()
# Get 2nd polygon Feature and Geometry
PolygonsFeature = PolygonsLayer . GetFeature (1)
PolygonsGeometry = PolygonsFeature . GetGeometryRef ()
# Print both geometries
print ( PointsGeometry )
print ( PolygonsGeometry )
# Calculate distance
Distance = PointsGeometry . Distance ( PolygonsGeometry )
print ('%.0f' % Distance )
##

#######################################################################################################################

#
# Use a for loop to iterate over the polygon layer and print field
# ’Hoofdgroep ’ ( Main group .)
#
##

PolygonsDataset = ogr. Open ("Texel_Polygons.shp")

# Get layer
PolygonsLayer = PolygonsDataset . GetLayer (0)
for feature in PolygonsLayer :
    print ( feature . GetField ('Hoofdgroep'))

#######################################################################################################################


# Using the 25 th point used in Exercise 9, calculate distances between
# this point and each land use feature on the island of Texel

##
print("##### last one")
PointsDataset = ogr. Open ("Texel_Points.shp")
PolygonsDataset = ogr. Open ("Texel_Polygons.shp")

# Get layer
PointsLayer = PointsDataset . GetLayer (0)
PolygonsLayer = PolygonsDataset . GetLayer (0)

# Get 25 th point Feature and Geometry
PointsFeature = PointsLayer . GetFeature (24)
PointsGeometry = PointsFeature . GetGeometryRef ()

for feature in PolygonsLayer :
    print ( feature . GetField ('Hoofdgroep'))
    HoofdgroepGeometry = feature . GetGeometryRef ()
    Distance = PointsGeometry . Distance ( HoofdgroepGeometry )
    print ('%.0f' % Distance )

########################################################################################################################