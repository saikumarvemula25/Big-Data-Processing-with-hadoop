#!/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
import os

train=pd.read_csv('/home/cse587/Downloads/Train.csv')
#test=pd.read_csv('/home/cse587/Downloads/Test.csv')

count = 0
X = train.iloc[:,0:train.shape[1]-1]
for line in sys.stdin:
 if count == 0:
  count = count+1
  continue
 #print(line)
 l = line.split(",")
 l2 = [float(i) for i in l]
 row = pd.Series(l2)
 row = row.values.reshape(1,row.shape[0])
 t = np.tile(row,(X.shape[0],1))
 x1 = np.sqrt(np.sum((X-t)**2,1))
 x1=x1.to_frame()
 x1['Label'] =train.iloc[:,train.shape[1]-1:train.shape[1]] 
 x1['edistance'] = x1[0]
 adddist1 = x1.sort_values('edistance')
 t1 = adddist1['Label'].tolist()
 print('%s\t%s' % (count, t1))
 count = count+1



