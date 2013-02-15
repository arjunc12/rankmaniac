#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    ## split on the tab
    tokens = line.split('\t')
    ## split the right side of the tab on the comma
    info = tokens[1].split(';')
    prdata = info[0].split(',')
    rtdata = info[1].split(',')
    rtdata[1] = str(int(rtdata[1]) + 1);
    ## get the first value on the right side, which is the final pagerank
    pagerank = float(prdata[0])
    ## print the inverse of the pagerank and the page corresponding to the pagerank
    ## print the inverse so that the results are sorted in descending order
    if pagerank > 1:
        sys.stdout.write("0\t" + tokens[0] + ';' + ','.join(prdata) + ';' + \
        ','.join(rtdata) + '\n')
    else:
        sys.stdout.write("1\t" + tokens[0] + ';' + ','.join(prdata) + ';' + \
        ','.join(rtdata) + '\n')

