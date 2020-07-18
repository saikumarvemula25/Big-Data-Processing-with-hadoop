#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd

knndict = {}
dupl = []
'''
for line in sys.stdin:
	#print(line)
 x1,x2 = line.split("\t")
 if x1 not in dupl:
  dupl.append(x1)
  l = list(x2.split(","))
  t1 = l[0:k]
  t = max(set(t1), key = t1.count)
  print('%s' % (t))
'''
for line in sys.stdin:
	c1,c2 = line.split("\t")
	l = list(c2.split(","))
	try:
	   x = knndict[c1]
	   knndict[c1]=x.append(l)
	except KeyError:
	   knndict[c1]=l

for k,v in knndict.items():
	t2 = v.copy()
	t3 = t2[0:8]
	tx = max(set(t3),key = t3.count)
	print(tx,k)
	

