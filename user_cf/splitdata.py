#SplitData.py
#encoding:utf8

import random

def splitdata(data,M,k,seed):
	test={}
	train={}
	random.seed(seed)
	for record in data:
		uid = record[0]
		if random.randint(1,M)==k:
			if uid not in test:
				test[uid] = []                
			test[uid].append(record)
		else:
			if uid not in train:
				train[uid] = []                
			train[uid].append(record)
	return train,test