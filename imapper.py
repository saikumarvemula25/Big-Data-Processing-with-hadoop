#!/usr/bin/env python3

from sys import stdin
import re
import os

for line in stdin:
 line = line.lower()
 reg=re.compile(r'[^a-z ]+')
 line = re.sub(reg,"",line) 
 doc_id = os.environ['map_input_file']
 doc_id = re.findall(r'\w+', doc_id)[-2]
 words = re.findall(r'\w+', line.strip())
 for word in words:
  print("%s\t%s" % (word.lower(), doc_id))
