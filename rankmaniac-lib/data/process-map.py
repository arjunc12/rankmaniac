#!/usr/bin/env python

import sys

for line in sys.stdin:
    ## split on the tab
    tokens = line.split('\t')
    ## split the right side of the tab on the comma
    info = tokens[1].split(',')
    ## get the first value on the right side, which is the final pagerank
    pagerank = float(info[0])
    ## print the inverse of the pagerank and the page corresponding to the pagerank
    ## print the inverse so that the results are sorted in descending order
    sys.stdout.write("1\t" + str(1.0/pagerank) + "," + tokens[0] + '\n')

