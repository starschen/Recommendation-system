#improve_cos.py
#encoding:utf8

import math
def improve_cos(train):
	#build inverse table for item_users#
	item_users=dict()
	for u,items in train.items():
		for item in items:
			if item[1] not in item_users:
				item_users[item[1]]=set()
			item_users[item[1]].add(u)


	#calculate co-rated items between users#
	C=dict()
	N=dict()
	for i ,users in item_users.items():
		for u in users:
			if u not in N:
				N[u] = 0
			N[u]+=1
			for v in users:
				if u ==v:
					continue
				if u not in C:
					C[u] = {}
				if v not in C[u]:
					C[u][v] = 0
				C[u][v]+=1

	#calculate finial similarity matrix W
	W=dict()
	for u,related_users in C.items():
		if  u not in W:
			W[u]={}
		for v,cuv in related_users.items():
			W[u][v]=cuv/math.sqrt(N[u]*N[v])
	return W

