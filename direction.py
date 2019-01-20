#!/bin/env python3
import sys

with open(sys.argv[1], encoding='utf8') as f:
	for l in f:
		id, ls = l.split('\t')
		lsx = ls.split(',')
		flag = False
		for l in lsx:
			if flag:
				if 'nanjing' not in l:
					print(id)
					break
			elif 'nanjing' in l:
				flag = True
			