import sys

fn = sys.argv[1]

def delt(et, st):
    em = int(et[8:10])*60 + int(et[10:12])
    sm = int(st[8:10])*60 + int(st[10:12])
    return em - sm

f = open(fn)
for l in f:
    uid, flag, st, et = l.strip().split('|')
    if flag == '1':
        try:
            print (delt(et, st))
        except:
            print( et, st)
