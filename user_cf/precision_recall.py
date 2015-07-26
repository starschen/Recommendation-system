#precision_recall.py
#encoding:utf8

from user_cf import user_cf
from operator import itemgetter
from settings import K

def precision(train,test, W, N):
	hit=0
	all=0
	for user in train.keys():
		if user not in test:
			continue
		tu=[x[1] for x in test[user]]
		rank=user_cf(user,train,W,K)     #getrecommendation(user,N)
		rank = dict(sorted(rank.items(),key=itemgetter(1),reverse=True) [0:N])
		for item,pui in rank.items():
			if item in tu:
				hit+=1
		all+=N
	return hit/(all*1.0)

def recall(train,test,W, N):
	hit=0
	all=0
	for user in train.keys():
		if user not in test:
			continue
		tu=[x[1] for x in test[user]]
		rank=user_cf(user,train,W,K)    #getrecommendation(user,N)
		rank = dict(sorted(rank.items(),key=itemgetter(1),reverse=True) [0:N])
		for item,pui in rank.items():
			if item in tu:
				hit+=1
		all+=len(tu)
	return hit/(all*1.0)
