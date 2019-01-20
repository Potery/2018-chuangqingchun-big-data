import sys

f = open(sys.argv[1], encoding='utf8')
d = {}
xx = 0
count = 0
for l in f:
    x = l.strip().split('|')
    if x[0] not in d:
        d[x[0]] = []
    longitude = float(x[2])
    latitude = float(x[3])
    if longitude < 122 and longitude > 118.47 and latitude < 32.41414 and latitude > 30.5:
        d[x[0]].append([x[1], x[2], x[3], x[4]])
    else:
        count += 1
    xx += 1
print (count, xx)
f.close()

f = open(sys.argv[2], 'w', encoding='utf8')

for k in d:
    d[k].sort(key=lambda xx: xx[0])
    f.write(k + '\t')
    for lo in d[k]:
        f.write(lo[0]+'|'+lo[1]+'|'+lo[2]+'|'+lo[3]+',')
    f.write('\t' + str(len(d[k])) + '\n')

f.close()
