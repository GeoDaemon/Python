#https://gis.stackexchange.com/questions/189590/export-raster-layer-in-python-to-specific-folder 

from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *
import os
import sys

crsDest = QgsCoordinateReferenceSystem(4326)

layers = iface.layerTreeView().selectedLayers()
for layer in layers:
    layer_name=layer.name()
    file_name = r'C:/Users/path/' + layer_name[#:#] + '.tif'
    file_writer = QgsRasterFileWriter(file_name)
    pipe = QgsRasterPipe()
    provider = layer.dataProvider()

    if not pipe.set(provider.clone()):
        print "Cannot set pipe provider"
        continue

    file_writer.writeRaster(
        pipe,
        provider.xSize(),
        provider.ySize(),
        provider.extent(),
        crsDest)
