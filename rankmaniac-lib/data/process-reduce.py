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
        ## split the right side of tab on commas
        info = tokens[1].split(';')
        prdata = info[1].split(',')
        ## the first element of info contains the inverse pagerank
        ## inverse it again to get the final pagerank
        pagerank = float(prdata[0])
        ## print out the node and its final pagerank
        d[pagerank] += [tokens[1]]
    else:
        info = tokens[1].split(';')
        buffer2 += info[0] + '\t' + info[1] + ';' + info[2] + '\n'

i = 0
done = False
for key in sorted(d, reverse=True):
    for node in d[key]:
        ## split the right side of tab on commas
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
