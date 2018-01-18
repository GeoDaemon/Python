import netCDF4
from netCDF4 import Dataset, stringtochar, chartostring

import random, numpy


nc = Dataset(r'C:\Users\file.nc')
nc


for dimobj in nc.dimensions.values():
	print dimobj
