#!/bin/env python3
import sys

def process(line):
	id, data, c = line.strip().split('\t')
	#print (id)
	data = data.split(',')
	flagx = False
	for d in data:
		xx = d.split('|')
		if flagx:
			if xx[-1] in ['83101', '83202', '83204', '83205', '83211']:
				print(id)
				break
		if xx[-1] == '83201':
			flagx = True


exit_flag = False
if __name__ == '__main__':
	with open(sys.argv[1], encoding='utf8') as f:
		for l in f:
			process(l)

