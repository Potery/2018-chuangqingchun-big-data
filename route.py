import sys
import math

filename = sys.argv[1]
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
	'南京-镇江': [load_route(0),load_route(5)],
	'镇江-常州': [load_route(1),load_route(6)],
	'常州-无锡': [load_route(2),load_route(7)],
	'无锡-苏州': [load_route(3),load_route(8)],
	'苏州-上海': [load_route(4),load_route(9),load_route(14)],
}



def test_point(point):
	ans = ''
	if point[0] > 118.76 and point[0] < 119.44: # 南京-镇江
		ans += '南京-镇江,'
	if point[0] > 119.4 and point[0] < 120: # 镇江-常州
		ans += '镇江-常州,'
	if point[0] > 119.95 and point[0] < 120.48: # 常州-无锡
		ans += '常州-无锡,'
	if point[0] > 120.29 and point[0] < 120.66:
		ans += '无锡-苏州,'
	if point[0] > 120.61 and point[0] < 121.46:
		ans += '苏州-上海,'
	return ans

def get_tpv(point):
	if point[0] < 118:
		return -100
	if point[0] > 118.76 and point[0] < 119.44: # 南京-镇江
		return 1
	if point[0] > 119.4 and point[0] < 120: # 镇江-常州
		return 2
	if point[0] > 119.95 and point[0] < 120.48: # 常州-无锡
		return 3
	if point[0] > 120.29 and point[0] < 120.66:
		return 4
	if point[0] > 120.61 and point[0] < 121.46:
		return 5
	return 100

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

def check_point(point):
	tp = test_point(point)
	ans = ''
	bound_flag = False
	if len(tp.split(',')) > 2:
		bound_flag = True
	for lname in tp.split(','):
		if lname:
			for line in d[lname]:
				ans += point_in_line(point, line)
	return ans, bound_flag, ans.strip(','), get_tpv(point)
	
def point_in_line(point, line):
	i = 0
	while i < len(line['locs'])-1:
		if distant3(point, line['locs'][i], line['locs'][i+1]) < 0.008:
			return line['from'] + '-' + line['dest'] + '_'
		i += 1
	return ''
	
	
	
	
f = open(filename)
for l in f:
	x = l.strip('\n').split('\t')
	if int(x[2]) < 2: # bad data
		continue
	locs = x[1].strip(',').split(',')
	uid = x[0]
	nlocs = ''
	last_ans = None 
	last_tpv = None
	for loc in locs:
		# 20180111001430|121.8975|30.8975|83101,
		t, x, y, lid = loc.split('|')
		ans, bound_flag, ansx, tpv = check_point((float(x),float(y)))
		#print (ans, bound_flag, ansx, last_ans, (bound_flag or last_ans and ansx != last_ans))
		if bound_flag or last_tpv and abs(last_tpv - tpv) > 0:
			bf = 1
		else:
			bf = 0
		last_ans = ans
		last_tpv = tpv
		nlocs += "%s|%s|%d," % (t[8:], ans, bf)
	print (uid + '\t' + nlocs)
