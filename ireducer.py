#!/usr/bin/python3

from sys import stdin
import re

index = {}

for line in stdin:
 word, doc_id = line.split('\t')
 index.setdefault(word, "")
 if doc_id not in index[word]:
  index[word] = index[word]+","+doc_id
for word1 in index:
 print('%s\t%s' % (word1, index[word1]))

