#cos_similarity.py
#encoding:utf8

import math
def cos_similarity(train):
	w=dict()
	for u in train.keys():
		for v in train.keys():
			if u==v:
				continue
			w[u][v]=len(train[u]&train[v])
			w[u][v]/=math.sqrt(len(train[u])*len(train[v])*1.0)
	return w