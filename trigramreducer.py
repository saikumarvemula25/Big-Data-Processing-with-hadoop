#!/usr/bin/env python3
import sys
import operator
 

trigramcount = {}
 

for line in sys.stdin:

    line = line.strip()
 

    word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    try:
        trigramcount[word] = trigramcount[word]+count
    except KeyError:
        trigramcount[word] = count
sorted_d =dict(sorted(trigramcount.items(),key=operator.itemgetter(1), reverse=True)[:10])
 
# write the tuples to stdout
# Note: they are unsorted
#for word in trigramcount.keys():
print('%s'% (sorted_d))

	

