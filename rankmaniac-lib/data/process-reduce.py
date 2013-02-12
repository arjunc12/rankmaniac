#!/usr/bin/env python

import sys
from collections import defaultdict

d = defaultdict(list)
for line in sys.stdin:
    ## split on the tab
    tokens = line.split('\t')
    ## split the right side of tab on commas
    info = tokens[1].split(',')
    ## the first element of info contains the inverse pagerank
    ## inverse it again to get the final pagerank
    pagerank = float(info[0])
    ## the first 7 characters of the second element have text
    ## the 8th character marks the start of the node number
    node = info[1][7:]
    ## print out the node and its final pagerank
    d[pagerank] += [node]

i = 0
for key in sorted(d, reverse=True):
    for node in d[key]:
        sys.stdout.write("FinalRank:" + str(key) + '\t' + node)
        i += 1
        if i == 10:
            break
    if i == 10:
        break

