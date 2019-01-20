import sys
import math
#from station import distant3


filename = sys.argv[1]
out_filename = sys.argv[2]

def distant3(p0, p1, p2):
	return abs((p0[0] - p1[0]) * (p1[1]-p2[1]) - (p1[0]-p2[0])*(p0[1]-p1[1])) / math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def in_a_line(p1, p2, p3):
    x, y = p1.split(' ')
    p1 = (float(x), float(y))
    x, y = p2.split(' ')
    p2 = (float(x), float(y))
    x, y = p3.split(' ')
    p3 = (float(x), float(y))
    return distant3(p3, p1, p2) < 0.003


f = open(filename, encoding='utf8')

with open(out_filename, 'w', encoding='utf8') as wf:
    for l in f:
        l = l.strip()
        if l:
            x = l.strip().split(':')
            locs = x[-1].split(',')
            last_index = 0
            #strx = '%s:%s:%s:%s:%s:' % (x[0], x[1], x[2], x[3], x[4])
            strx = '%s:%s:%s:' % (x[0], x[1], x[2])#, x[3], x[4])
            strx += locs[0] + ',' + locs[1]
            cur_i = 1
            next_i = 2
            coun = 0
            while next_i < len(locs):
                if not in_a_line(locs[last_index], locs[cur_i], locs[next_i]):
                    strx += ',' + locs[next_i]
                    last_index = cur_i
                    cur_i = next_i
                    coun += 1
                next_i += 1
            if cur_i != len(locs) - 1:
                strx += ',' + locs[-1]
            wf.write(strx + '\n')
            print('%d of %d' % (coun, len(locs)))
f.close()

'''
24 of 1297
19 of 1160
9 of 768
7 of 519
17 of 594
16 of 666
9 of 544
14 of 469
5 of 258
26 of 534
1 of 35
20 of 495
11 of 352
6 of 293
26 of 1074
6 of 147
20 of 495
11 of 352
6 of 293
18 of 1065
6 of 147
20 of 495
11 of 352
6 of 293
26 of 1074
sxw@sxw-MS-7A33:~/Work/ctyun/qddx$ python3 simplify_road.py d/freeway.txt freeway.txt
Traceback (most recent call last):
  File "simplify_road.py", line 29, in <module>
    locs = x[5].split(',')
IndexError: list index out of range
sxw@sxw-MS-7A33:~/Work/ctyun/qddx$ python3 simplify_road.py d/freeway.txt freeway.txt
21 of 1086
16 of 741
20 of 1039
10 of 346
25 of 1337
18 of 682
14 of 855
22 of 1106
10 of 346
25 of 1337
18 of 682
14 of 855
52 of 2802
'''