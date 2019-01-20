import sys, math


f_rail = open('railway.txt', 'r', encoding='utf8')
lines = f_rail.readlines()
f_rail.close()
def load_route(l):
	l = lines[l]
	x = l.strip('\n').split(':')
	from_s = x[2]
	dest_s = x[4]
	line_id = x[0]
	locs = x[5]
	
	locsl = []
	for loc in locs.split(','):
		x, y = loc.split(' ')
		locsl.append((float(x), float(y)))
	return {'id': line_id,'from': from_s, 'dest': dest_s, 'locs': locsl}

d = {
	'1': [load_route(0),load_route(5)],
	'2': [load_route(1),load_route(6)],
	'3': [load_route(2),load_route(7)],
	'4': [load_route(3),load_route(8)],
	'5': [load_route(4),load_route(9),load_route(14)],
}

def distant(p1, p2):
	return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def distant3(p0, p1, p2):
	a = distant(p1, p2)
	b = distant(p1, p0)
	c = distant(p2, p0)
	cosb = (c ** 2 + a ** 2 - b ** 2) / (2 * a * c)
	cosc = (b ** 2 + a ** 2 - c ** 2) / (2 * a * b)
	if cosb < 0 or cosc < 0:
		return min(b, c)
	return abs((p0[0] - p1[0]) * (p1[1]-p2[1]) - (p1[0]-p2[0])*(p0[1]-p1[1])) / math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def check_point(p, line):
	i = 0
	while i < len(line['locs'])-1:
		if distant3(p, line['locs'][i], line['locs'][i+1]) < 0.025:
			return True
		i += 1
	return False

def check(points, s, e, xid):
	mok_c = 0
	msi = None
	mei = None
	mstr = None
	mdir = None
	s_dis = None
	e_dis = None
	les = d[xid]
	for le in les:
		i = s
		si = None
		ok_c = 0
		endp = le['locs'][-1]
		d1c = 0
		d2c = 0
		ei = None
		last_dis = None
		xxx = 0
		print (le['from'] + '_' + le['dest'], '===========')
		flagxxx = True
		while i <= e:
			if ((i == s) and (distant(points[i], le['locs'][0]) < 0.01)) or check_point(points[i], le):
				
				flagxxx = False
				if not si:
					si = i
				ok_c += 1
				cur_dis = distant(endp, points[i])
				ei = i
				if last_dis:
					if last_dis > cur_dis: # 距终点越来越近
						d1c += 1
					else:
						d2c += 1
				last_dis = cur_dis
			elif flagxxx:
				xxx += 1
			print (i)
			i += 1
		print (le['from'] + '_' + le['dest'], ok_c, xxx)
		if ok_c > 1 and ok_c > (e - s-xxx) / 2 and ok_c > mok_c:
			mok_c = ok_c
			msi = si
			mei = ei
			mstr = le['from'] + '_' + le['dest']
			if d1c < d2c:
				mdir = 1
			else:
				mdir = 2
			s_dis = distant(points[si], le['locs'][0])
			e_dis = distant(points[ei], le['locs'][-1])
	return msi, mei, mdir, s_dis, e_dis, mstr
			
		

fn = sys.argv[1]
f = open(fn)
cnt = 0
for l in f:
	cnt += 1
	uid, locs, count, lines = l.strip().split('\t')
	locs = locs.strip(',').split(',')
	points = []
	for loc in locs:
		t, x, y, no = loc.split('|')
		points.append((float(x), float(y)))
	try:
		ans = ''
		for line in lines.split(','):
			s, e, xid = line.split('|')
			if int(xid) > 0:
				ss, ee, direction, s_dis, e_dis, s_d = check(points, int(s), int(e), xid)
			if ss != None:
				ans = ans + '%s|%s|%s|%d|%s|%f|%f,' % (locs[ss].split('|')[0], locs[ee].split('|')[0], xid, direction, s_d, s_dis, e_dis)
		print (uid + '\t' + ans)
	except:
		print(uid, file=sys.stderr)
	if cnt % 1000 == 0:
		print (cnt, file=sys.stderr)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		