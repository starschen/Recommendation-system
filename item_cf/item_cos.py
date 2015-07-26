#item_cos.py
#encoding:utf8

import math
def item_cos(train):
	#build inverse table for item_users#
	item_users=dict()
	for u,items in train.items():
		for item in items:
			if item[1] not in item_users:
				item_users[item[1]]=set()
			item_users[item[1]].add(u)    #pay attention#


	#calculate co-rated items between users#
	C=dict()
	N=dict()
	for u ,items in train.items():
		for i in users:
			if i not in N:
				N[i] = 0
			N[i]+=1
			for j in users:
				if i ==j:
					continue
				if j not in C:
					C[i] = {}
				if v not in C[u]:
					C[i][j] = 0
				C[i][j]+=1

	#calculate finial similarity matrix W
	W=dict()
	for i,related_items in C.items():
		if  i not in W:
			W[u]={}
		for j,cij in related_items.items():
			W[i][j]=cij/math.sqrt(N[i]*N[j])
	return W

def item_cos_iuf(train):
	#build inverse table for item_users#
	item_users=dict()
	for u,items in train.items():
		for item in items:
			if item[1] not in item_users:
				item_users[item[1]]=set()
			item_users[item[1]].add(u)    #pay attention#


	#calculate co-rated items between users#
	C=dict()
	N=dict()
	for u ,items in train.items():
		for i in users:
			if i not in N:
				N[i] = 0
			N[i]+=1
			for j in users:
				if i ==j:
					continue
				if j not in C:
					C[i] = {}
				if v not in C[u]:
					C[i][j] = 0
				C[i][j]+=1/math.log(1+len(items)*1.0)  #improve

	#calculate finial similarity matrix W
	W=dict()
	for i,related_items in C.items():
		if  i not in W:
			W[u]={}
		for j,cij in related_items.items():
			W[i][j]=cij/math.sqrt(N[i]*N[j])
	return W

