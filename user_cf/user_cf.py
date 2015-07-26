#user_cf.py
#encoding:utf8

from improve_cos import improve_cos
from operator import itemgetter
def user_cf(user,train,W, K):
	rank=dict()
	if user not in train:
		return rank
	interacted_items=[x[1] for x in train[user]]
	for v,wuv in sorted(W[user].items(),key=itemgetter(1),reverse=True) [0:K]:
		for i in [x[1] for x in train[v]]:
			if i in interacted_items:
				#we should filter items user interacted before
				continue
			if i not in rank:
				rank[i] = 0
			rank[i]+=wuv
	return rank