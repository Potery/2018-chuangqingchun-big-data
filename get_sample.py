#!/usr/bin/env python3

import sys
import random
if len(sys.argv) == 1:
    exit(-1)
elif len(sys.argv) == 2:
    n = int(sys.argv[1])
    f = sys.stdin
elif len(sys.argv) == 3:
    f = open(sys.argv[1], encoding='utf8')
    n = int(sys.argv[2])

lines = f.readlines()
choosed_id = []
if n > len(lines): n = len(lines)

while len(choosed_id) < n:
    randx = random.randint(0, n - 1)
    if randx not in choosed_id:
        choosed_id.append(randx)
for idx in choosed_id:
    print (lines[idx].strip())

