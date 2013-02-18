#!/usr/bin/env python

import sys
from collections import defaultdict

d = defaultdict(list)
buffer1 = '';
buffer2 = '';
buffer3 = '';
lines = 0;

for line in sys.stdin:
    line = line.strip();
    ## split on the tab
    tokens = line.split('\t')
    if tokens[0] == '0':
        info = tokens[1].split(';')
        prdata = info[1].split(',')
        pagerank = float(prdata[0])
        d[pagerank] += [tokens[1]]
    else:
        info = tokens[1].split(';')
        buffer2 += info[0] + '\t' + info[1] + ';' + info[2] + '\n'

i = 0
done = False
for key in sorted(d, reverse=True):
    for node in d[key]:
        info = node.split(';')
        prdata = info[1].split(',')
        rtdata = info[2].split(',')
        nnode = info[0][7:]
        if (int(rtdata[0]) == i + 1 and i < 10) or (int(rtdata[1]) >= 15):
            buffer3 += "FinalRank:" + str(key) + '\t' + nnode + '\n'
            lines += 1
            if lines == 10:
                sys.stdout.write(buffer3)
                done = True
                break
        rtdata[0] = str(min(i + 1, 11))
        i += 1
        buffer1 += info[0] + '\t' + ','.join(prdata) + ';' + ','.join(rtdata) + '\n'

if not done:
    sys.stdout.write(buffer1 + buffer2)
