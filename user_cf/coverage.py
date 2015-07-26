#coverage.py
#encoding:utf8

from user_cf import user_cf
from operator import itemgetter
from settings import K

def coverage(train,test,W, N):
    recommend_items=set()
    all_items=set()
    for user in train.keys():
        for item in train[user]:
            all_items.add(item[1])
        rank=user_cf(user,train,W,K)   #getrecommendation(user,N)
        rank = dict(sorted(rank.items(),key=itemgetter(1),reverse=True) [0:N])
        for item in rank.keys():
            recommend_items.add(item)
    return len(recommend_items)/(len(all_items)*1.0)
