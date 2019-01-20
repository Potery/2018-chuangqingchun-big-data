import sys

fn = sys.argv[1]

f = open(fn)

def get_min(times):
	try:
		return int(times[8:10]) * 60 + int(times[10:12])
	except:
		print (times)

for l in f:
	uid, f, ss, e = l.strip().split('|')
	if f != '0': #and get_min(e) - get_min(ss) > 300:
		chg = ss[9]
		chs = ss[8]
		
		g = ord(chg) + 3
		if g > ord('9'):
			g -= 10
			s = ord(ss[8]) + 1
			chs = chr(s)
		chg = chr(g)
			
		print (uid + ('|1|%s|%s' %("20180111000000", "20180111000000")))
	else:
		print (l.strip('\n'))