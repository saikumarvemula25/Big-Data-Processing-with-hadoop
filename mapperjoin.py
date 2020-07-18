#!/usr/bin/python3

import sys
import io
import re
from csv import reader


'''
with open('/home/cse587/Desktop/join1.csv','r',encoding= "ISO-8859-1") as f:
	print(f.read())

l=sys.stdin
prin
t(l)

f = pd.read_csv('/home/cse587/Desktop/join1.csv')
print(f)
'''
#sys.stdin.reconfigure(encoding='utf-8')
for line in reader(sys.stdin):
    #line = line.decode("utf-8","strict")
    #line = line.strip()
    #new = line.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)")
    #print(line)
   
    #line = line.split(",")
    
    id1 = "-1"
    name = "-1"
    salary = "-1"
    country = "-1"
    code = "-1"



    if len(line) ==4:
        id1 = line[0]
        salary = line[1]
        country = line[2]
        code = line[3]

    else:
        id1 = line[0]
        name = line[1]


    print('%s\t%s\t%s\t%s\t%s' % (id1, name, salary, country, code))
    




