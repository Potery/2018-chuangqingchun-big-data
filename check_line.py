import sys

filename = sys.argv[1]

f = open(filename, 'r', encoding='utf8')



def get_line_v(linestr):
	if '镇江' in linestr:
		if '南京' in linestr:
			return 1
		if '常州' in linestr:
			return 2
	if '常州' in linestr and '无锡' in linestr:
		return 3
	if '无锡' in linestr and '苏州' in linestr:
		return 4
	if '苏州' in linestr and '上海' in linestr:
		return 5
	raise Exception('unkonw line' + linestr)


for l in f:
	uid, locs = l.strip('\n').split('\t')
	linesx = []
	in_line = False
	gap_count = 0
	in_line_count = 0
	start_time = None
	last_timea = None
	last_not_in = False
	for loc in locs.split(','):
		if not loc:
			continue
		timestr, lines, bf = loc.split('|')
		if lines == '':
			if in_line: #不在任何线路上的点
				if bf == '1':
					if in_line_count > 2 or in_line_count >= gap_count:
						linesx.append([start_time, last_time, last_val])
					in_line_count = 0
					gap_count = 0
					in_line = False
				else:
					gap_count += 1
		else: 
			x_in_line = True
			x_conincident = False
			cur_vals = []
			for line in lines.split('_'):
				if not line: continue
				cur_val = get_line_v(line)
				if in_line:
					if cur_val == last_val: # 只要有一个点在原线路上就认为该点还在原线路上
						x_conincident = True
				if cur_val not in cur_vals: 
					cur_vals.append(cur_val)
			if not in_line:
				start_time = timestr
				in_line = True
				in_line_count += 1
				last_val = cur_val
			else:
				if x_conincident: # 仍保持原线路
					in_line_count += 1
					
				if not x_conincident or bf == '1': # 线路变化, 或者再临界点上
					if bf == 1:
						end_time = last_time
					else:
						end_time = timestr
					#print (last_val,  in_line_count, gap_count)
					if in_line_count > 2 or in_line_count >= gap_count:
						linesx.append([start_time, end_time, last_val])
					
					in_line_count = 1
					gap_count = 0
					start_time = timestr
					last_val = cur_val
					last_timea = timestr
			last_time = timestr
	if bf == 1:
		end_time = last_timea
	else:
		end_time = timestr
	if in_line_count > 2 or in_line_count > gap_count:
		linesx.append([start_time, end_time, last_val])
	ans = uid + '\t'
	for l in linesx:
		ans += '%s|%s|%d,' % (l[0], l[1], l[2])
	print (ans)
		
					
				
					
					
					
					
					
						
						