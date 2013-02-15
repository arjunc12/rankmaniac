#!/usr/bin/env python

import sys

for line in sys.stdin:
    ## write the line so that we can preserve information about all its 
    ## neighbors as well as preserve its current pagerank, which will soon be 
    ## its previous pagerank
    line = line.strip()
    if ';' not in line:
        line = line + ';11,0'
    sys.stdout.write(line + '\n')
    ## split on the tab delimiter
    tokens = line.split('\t')
    ## the right side of the tab contains comma-separated values
    info = tokens[1].split(';')
    prdata = info[0].split(',')
    rtdata = info[1].split(',')
    ## current pagerank
    pagerank = float(prdata[0])
    ## get the list of neighbors
    neighbors = prdata[2:]
    ## if it has no neighbors then this node doesn't distribute any pagerank 
    ## outward it essentially distributes its pagerank back to itself
    if len(neighbors) == 0:
        sys.stdout.write(tokens[0] + "\t" + str(pagerank) + "\n")
    ## otherwise go through each neighbor
    ## output the neighbor as well as the amount of pagerank that neighbor will 
    ## receive from the current node
    for n in neighbors:
        sys.stdout.write("NodeId:" + n.strip() + "\t" + str(pagerank / \
        len(neighbors)) + "\n")