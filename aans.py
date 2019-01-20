import sys

fa = open(sys.argv[1])
f = open(sys.argv[2])
d = {}
for l in f:
	x = l.strip().split('|')
	d[x[0]] = l
	
f.close()

for l in fa:
	x = l.split('\t')
	if x[0] in d:
		print (d[x[0]].strip())
	else:
		print (x[0]+'|0|0|0')