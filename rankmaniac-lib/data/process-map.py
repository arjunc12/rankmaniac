#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

for line in sys.stdin:
    tokens = line.split('\t')
    info = tokens[1].split(',')
    pagerank = float(info[0])
    sys.stdout.write("1\t" + str(1.0/pagerank) + "," + tokens[0] + '\n')

