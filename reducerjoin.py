#!/usr/bin/python3

import sys

empdetails_dict ={}
emp_dict={}
for line in sys.stdin:
    line = line.strip()
    id1, name, salary, country, code = line.split('\t')

    #print('%s\t%s\t%s'% (id1, name, salary))
 

    if name =="-1":
    	empdetails_dict[id1] = [salary,country,code]
    #empdetails_dict[id1] = [salary,country]

    else:
        emp_dict[id1] = [name]

for id2 in empdetails_dict.keys():
    id3 = id2
    tx = emp_dict[id3]
    name = tx[0]
    salary = empdetails_dict[id2][0]
    country = empdetails_dict[id2][1]
    code = empdetails_dict[id2][2]

    print('%s\t%s\t%s\t%s\t%s'% (id2, name, salary,country,code))



