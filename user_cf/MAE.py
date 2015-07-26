#MAE.py
#encoding:utf8

import math

def MAE(records):
	return sum([abs(rui-pui) for u,i,rui,pui in records])/float(len(records))