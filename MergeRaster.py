import os
from osgeo import gdal

input_folder = input('Ingrese ruta donde se encuentran los tif a unir')
output_file = input('Ingrese ruta donde se guardaran los tif unidos')


def merge_orthomosaics(input_folder, output_file):
    tif_files = [f for f in os.listdir(input_folder) if f.endswith('.tif')]
    mosaic_list =[gdal.Open(os.path.join(input_folder, tif)) for tif in tif_files]

    mosaic = gdal.Composite(output_file, mosaic_list)
    
    for m in mosaic_list:
        m = None
    

merge_orthomosaics(input_folder, output_file)    