#giniindex.py
#encoding:utf8

def GiniIndex(p):
	j=1
	n=len(p)
	G=0
	for item,weight in sorted(p.items(),key=itemgetter(1)):
		G+=(2*j-n-1)*weight
	return G/float(n-1)