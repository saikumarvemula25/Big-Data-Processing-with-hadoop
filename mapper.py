#!/usr/bin/env python3
import sys
import re

for line in sys.stdin:
 line = line.lower()
 line = line.strip()
 reg=re.compile(r'[^a-z ]+')
 line = re.sub(reg,"",line) 
 words = line.split()
 for word in words:
  #x = re.sub(reg,"",word) 
  print('%s\t%s' % (word, "1"))



