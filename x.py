import sys
import math

def dis(p1, p2):
    p1 = p1.split(' ')
    p2 = p2.split(' ')
    return math.sqrt((float(p1[0])-float(p2[0]))**2 + (float(p1[1]) - float(p2[1])) ** 2)

with open(sys.argv[1]) as f:
    line = f.read().strip()
    locs = line.split(',')
    i = 1
    result = locs[0]
    lp = locs[0]
    xc = 0
    while i < len(locs):
       if dis(lp, locs[i]) > 0.009:
           result += ',' + locs[i]
           lp = locs[i]
           xc += 1
       i += 1 
    print (len(locs), xc)
    print (result)
