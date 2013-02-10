#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

i = 0
for line in sys.stdin:
    tokens = line.split('\t')
    info = tokens[1].split(',')
    pagerank = 1 / float(info[0])
    node = info[1][7:]
    sys.stdout.write("FinalRank:" + str(pagerank) + '\t' + node)
    
    i += 1
    if i == 10:
        break

