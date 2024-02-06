import os
import ogr as ogr
from osgeo import gdal

# Lista de imágenes para fusionar
# List of images to merge
img_list = [r'ruta/a/la/imagen1.tif', r'ruta/a/la/imagen2.tif', r'ruta/a/la/imagen3.tif']

# Ruta de la imagen de salida
# output
out_img = r'ruta/a/la/imagen_fusionada.tif'

# Nombre de la capa de recorte
# crop layer name
cut_layer = r'ruta/a/la/capa_recorte.shp'

# Fusionar las imágenes
# Merge images
gdal.BuildVRT(out_img, img_list)

# Abrir la imagen de salida
# open output
src_ds = gdal.Open(out_img)

# Obtener la proyección de la capa de recorte
# CRS of crop layer
cut_ds = ogr.Open(cut_layer)
cut_lyr = cut_ds.GetLayer()
sr = cut_lyr.GetSpatialRef()

# Crear una imagen de salida recortada
# create images
x_min, x_max, y_min, y_max = cut_lyr.GetExtent()
wkt = sr.ExportToWkt()
dst_ds = gdal.GetDriverByName('GTiff').Create(out_img.replace('.tif', '_cut.tif'), src_ds.RasterXSize, src_ds.RasterYSize, 1, gdal.GDT_Float32)
dst_ds.SetProjection(wkt)
dst_ds.SetGeoTransform((x_min, src_ds.GetGeoTransform()[1], 0, y_max, 0, src_ds.GetGeoTransform()[5]))
gdal.ReprojectImage(src_ds, dst_ds, src_ds.GetProjection(), wkt, gdal.GRA_Bilinear)

# Cerrar los datasets
# closed datasets
src_ds = None
dst_ds = None
cut_ds = None

