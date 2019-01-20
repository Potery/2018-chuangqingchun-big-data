import sys

f1 = open(sys.argv[1])
f2 = open(sys.argv[2])
fi = open('incx', 'w')
fr = open('rewx', 'w')

for l1 in f1:
    l2 = f2.readline()
    uid1, flag1, s1, e1 = l1.strip().split('|')
    uid2, flag2, s2, e2 = l2.strip().split('|')
    if flag1 != flag2:
        if flag1 == '0':
            fi.write(l2)
        else:
            fr.write(l1)
f1.close()
f2.close()
fi.close()
fr.close()

