import sys

fn = sys.argv[1]


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
	if point[0] > 120.61 and point[0] <= 121.46:
		ans += '苏州-上海,'
	return ans

def test_pointv(point):
	ans = -1
	if point[0] <= 118.76:
		return 0
	if point[0] > 118.76 and point[0] < 119.44: # 南京-镇江
		ans = 1
	if point[0] > 119.4 and point[0] < 120: # 镇江-常州
		if ans == 1:
			return 1.5
		ans = 2
	if point[0] > 119.95 and point[0] < 120.48: # 常州-无锡
		if ans == 2:
			return 2.5
		ans = 3
	if point[0] > 120.29 and point[0] < 120.66:
		if ans == 3:
			return 3.5
		ans = 4
	if point[0] > 120.61 and point[0] <= 121.46:
		if ans == 4:
			return 4.5
		return 5
	if point[0] > 121.46:
		return 0
	return ans


debug = True
debug = False
cnt = 0

f = open(fn)
fb = open('badc', 'w')
for l in f:
	#cnt += 1
	flag =False
	uid, locs, count = l.strip('\n').split('\t')
	if locs:
		locs = locs.strip(',').split(',')
		d = []
		for loc in locs:
			t, x, y, no = loc.split('|')
			p = (float(x), float(y))
			a = test_point(p)
			if no not in d:
				d.append(no)
		if len(d) < 2:
			if not debug:
				fb.write(uid + '\n')
		else:
			nc = 0
			vc = 0
			for loc in locs:
				t, x, y, no = loc.split('|')
				p = (float(x), float(y))
				a = test_point(p)
				if a == '':
					nc += 1
				else:
					vc += 1
			if nc > vc and vc < 4:
				if not debug:
					fb.write(uid + '\n')
			else:
				t, x, y, no = locs[0].split('|')
				p = (float(x), float(y))
				last_v = test_pointv(p)
				x_starti = None
				s_i = -1
				if last_v != 0: s_i = 0
				i = 1
				ans = []
				r_flag = False
				flagxxx = False
				while i < len(locs):
					t, x, y, no = locs[i].split('|')
					p = (float(x), float(y))
					cur_v = test_pointv(p)
					if s_i != -1:
						
						if last_v == cur_v:
							if x_starti:
								x_starti = None
						elif abs(last_v - cur_v) < 1:
							if int(last_v) != last_v:
								last_v = cur_v
							elif not x_starti:
								x_starti = i
						else:
							if int(last_v) == last_v:
								a = '%d|%d|%d' %(s_i, i-1, last_v)
								if last_v == 1:
									flagxxx = True
								if a not in ans:
									ans.append(a)
								else:
									r_flag = True
							else:
								a = '%d|%d|%d' %(s_i, i-1, (last_v+cur_v) / 2)
								if (last_v+cur_v) / 2:
									flagxxx = True
								if a not in ans:
									ans.append(a)
								else:
									r_flag = True
							if x_starti and not r_flag:
								i = x_starti - 1
								s_i = x_starti
								last_v = cur_v
							else:
								s_i = -1
								i -= 1
								r_flag = False
					else:
						if cur_v != 0:
							s_i = i
							last_v = cur_v
					i += 1

					
				if s_i != -1:
					if int(last_v) == last_v:
						a = '%d|%d|%d' %(s_i, i-1, last_v)
						if last_v == 1:
							flagxxx = True
						if a not in ans:
							ans.append(a)
					else:
						a = '%d|%d|%d' %(s_i, i-1, (last_v+cur_v) / 2)
						if (last_v+cur_v) / 2:
							flagxxx = True
						if a not in ans:
							ans.append(a)
				if flagxxx:
					if len(ans) == 0:
						if not debug:
							fb.write(uid+'\n')
					else:
						ans_s = ans[0]
						i = 1
						while i < len(ans):
							ans_s += ','+ans[i]
							i += 1
						print (l.strip() + '\t' + ans_s)
				else:
					fb.write(uid+'\n')
					
	else:
		if not debug:
			fb.write(uid + '\n')
	#if cnt % 1000 == 0:
	#	print ('cnt=', cnt, file=sys.stderr)

fb.close()
			
			