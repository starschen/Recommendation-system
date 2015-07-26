#RMSE.py
#encoding:utf8

import math
def RMSE(records):
	return  math.sqrt(sum([(rui-pui)*(rui-pui) for u,i,rui,pui, in records])/float(len(records)))