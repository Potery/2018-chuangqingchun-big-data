import sys

fn = sys.argv[1]

f = open(fn)

def get_min(times):
	return int(times[8:10]) * 60 + int(times[10:12])



for l in f:
	try:
		uid, lines = l.strip('\n').split('\t')
	except:
		continue
	if lines:
		cur_i = 0
		sf = False
		for line in lines.strip(',').split(','):
			st, et, xid, direction, s_d, s_dis, e_dis = line.split('|')
			if (xid == '1' or xid =='2') and direction == '2':
				cur_i = int(xid)
				sf = True
				stime = st
				etime = et
			else:
				if sf:
					if int(xid) < cur_i:
						break
					etime = et
		if sf:
			#print (uid)
			print ("%s|1|%s|%s" % (uid, stime, etime))
		
		