import sys

filename = sys.argv[1]
fb = open('back.e', 'w', encoding='utf8')
f1 = open('1.e', 'w', encoding='utf8')
f = open(filename, 'r', encoding='utf8')

for l in f:
	uid, lines = l.strip('\n').split('\t')
	all_start = None
	last_v = None
	flag = False
	back_f = False
	if lines:
		for line in lines.strip(',').split(','):
			#print (line)
			start_time, end_time, lv = line.split('|')
			
			lv = int(lv)
			if lv == 1:
				all_start = start_time
				last_v = lv
				flag = True
			else:
				if all_start:
					if lv >= last_v:
						last_v = lv
					else:
						if last_v != 5:
							fb.write(uid+'\n')
						flag = False
						break
			print (end_time)
		print (end_time)
		if flag:
			#UID|1|20180111080355|20180111093718
			if last_v == 1:
				mins = int(all_start[0:2]) * 60 + int(all_start[2:4])
				mine = int(end_time[0:2]) * 60 + int(end_time[2:4])
				if mine - mins > 10 and mine - mins < 80: 
					print(uid+'|1|20180111%s|20180111%s' %(all_start, end_time))
				else:
					f1.write(uid + '\t%d\n' %(mine-mins))
			else:
				#print (end_time)
				print(uid+'|1|20180111%s|20180111%s' %(all_start, end_time))
						
f1.close()
fb.close()