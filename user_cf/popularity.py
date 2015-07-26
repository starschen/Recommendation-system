#popularity.py
#encoding:utf8

from user_cf import user_cf
import math
K = 5
def popularity(train,test, W, N):
    item_popularity=dict()
    for user,items in train.items():
        for item in items:
            if item[1] not in item_popularity:
                item_popularity[item[1]]=0
            item_popularity[item[1]]+=1
    ret=0
    n=0
    for user in train.keys():
        rank=user_cf(user,train,W,K) #getrecommendation(user,N)
        for item in rank.keys():
            ret+=math.log(1+item_popularity[item])
            n+=1
    ret/=n*1.0
    return ret