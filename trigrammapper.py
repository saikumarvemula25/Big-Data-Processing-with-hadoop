#!/usr/bin/env python3
import sys
import re
for line in sys.stdin:
	#line=line.lower()
	#print(line)
	line = line.lower()
	line = line.strip()
	reg = re.compile(r'[^a-zA-Z_$ ]+')
	line = re.sub(reg,"",line)
	words=line.split()
	length = len(words)
	i=0
	y="$"
	#reg=re.compile("[^a-z_'$0-9]+")

	while(i+2<length):

		first=words[i]
		second=words[i+1]
		third=words[i+2]
		i=i+1
		if first=="science" or first=="sea" or first == "fire":
			first="$"
		if second=="science" or second=="sea" or second == "fire":
			second="$"
		if third=="science" or third=="sea" or third == "fire":
			third="$"
		x = first+"_"+second+"_"+third

		#x = x.replace("science","$")  
		#x = x.replace("sea", "$")
		#x = x.replace("fire","$")

		if y in x:
			print('%s\t%s' % (x, 1))
		#print(x)
		
