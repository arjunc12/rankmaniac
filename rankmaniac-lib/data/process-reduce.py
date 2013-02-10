#!/usr/bin/env python

import sys

i = 0
for line in sys.stdin:
    ## split on the tab
    tokens = line.split('\t')
    ## split the right side of tab on commas
    info = tokens[1].split(',')
    ## the first element of info contains the inverse pagerank
    ## inverse it again to get the final pagerank
    pagerank = 1 / float(info[0])
    ## the first 7 characters of the second element have text
    ## the 8th character marks the start of the node number
    node = info[1][7:]
    ## print out the node and its final pagerank
    sys.stdout.write("FinalRank:" + str(pagerank) + '\t' + node)
    
    ## increment the counter
    ## mapreduce sorts in ascending order by inverse pagerank
    ## which is equivalent to sorting by pagerank in descending order
    ## thus the first ten values correspond to the top ten values
    i += 1
    if i == 10:
        break

