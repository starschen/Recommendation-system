#item_cf.py
#encoding:utf8

from item_cos import item_cos
from operator import itemgetter

def item_cf(train,user_id,W, K):
	rank=dict()
	ru=train[user_id]
	for i,pi in ru.items():
		for j,wj in sorted(W[i].items(),key=itemgetter(1),reverse=True) [0:K]:
			if j in ru:
				continue
			rank[j]+=pi*wj
	return rank

def  item_cf_trans(train,user_id,W, K):
	rank=dict()
	ru=train[user_id]
	for i,pi in ru.items():
		for j,wj in sorted(W[i].items(),key=itemgetter(1),reverse=True) [0:K]:
			if j in ru:
				continue
			rank[j].weight+=pi*wj
			rank[j].reason[i]=pi*wj
	return rank