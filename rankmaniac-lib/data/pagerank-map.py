#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    sys.stdout.write(line)
    tokens = line.split('\t')
    info = tokens[1].split(',')
    pagerank = float(info[0])
    neighbors = info[2:]
    if len(neighbors) == 0:
        sys.stdout.write(tokens[0] + "\t" + str(pagerank) + "\n")
    for n in neighbors:
        sys.stdout.write("NodeId:" + n.strip() + "\t" + str(pagerank / len(neighbors)) + "\n")