import netCDF4
from netCDF4 import Dataset, stringtochar, chartostring

import random, numpy


nc = Dataset(r'C:\Users\ariverar\Downloads\maiac_A_20160127_2040_v2_normalized.nc')
nc


for dimobj in nc.dimensions.values():
	print dimobj
