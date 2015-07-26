#encoding: utf8
from splitdata import splitdata
from improve_cos import improve_cos
from user_cf import user_cf
from precision_recall import precision,recall
from coverage import coverage
from popularity import popularity
import time
from settings import *

def load_data(name):
    records = [] # key => items
    f = open(name)
    for line in f.read().split():
        record = line.split('::')
        records.append(record)
    return records

users = load_data('ml-1m/users.dat')
ratings = load_data('ml-1m/ratings.dat')
movies = load_data('ml-1m/movies.dat')


k = 5
seed = time.time()
train,test = splitdata(ratings,M,k,seed)

def list_to_dict(rating):
    return {'uid': rating[0],'movieid': rating[1],'rating': rating[2],'time': rating[3]}
 
def convert_train(train):
    for k, ratings in train.iteritems():
        train[k] = [list_to_dict(rating) for rating in ratings]
    return train

print 'improve_cos ...'
W = improve_cos(train)

print 'user_cf ...'
for user in users:
	rank = user_cf(user[0],train,W,K)
	#print rank
print precision(train,test, W, N)
print recall(train,test,W, N)
print coverage(train,test, W, N)
print popularity(train,test,W, N)
