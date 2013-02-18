#!/usr/bin/env python

import sys

cur_node = ""
d = 0.85
sum = 0
for line in sys.stdin:
    line = line.strip()
    ## split on the tab delimiter
    tokens = line.split('\t')
    
    ## the results of map are grouped by node
    ## i.e. we have a bunch of key value pairs in which the key is the
    ## node to which pagerank is being added and each value represents
    ## an amount of pagerank to be redistributed to the node with which
    ## it is associated
    ## the grouping means we can keep a running total and stop adding once
    ## we hit a node different from the previous node then we have reached
    ## a new group and can emit the sum of all the values of the previous
    ## group, which represents the new pagerank of the previous node-key
    
    ## check if we have reached a new node key
    if tokens[0] != cur_node:
        ## check if this is the first node
        ## if it is, start a running total
        ## otherwise print the previous running total
        if cur_node != "":
            new_pagerank = (1 - d) + d * new_pagerank
            if len(neighbors) != 0:
                sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + \
                old_pagerank + "," + ",".join(neighbors) + ';' + \
                ','.join(data) + '\n')
            else:
                sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + \
                old_pagerank + ';' + ','.join(data) + '\n')
        cur_node = tokens[0]
        new_pagerank = 0.0
    ## check if this is the info node as opposed to a node-pagerank pair
    if ',' in tokens[1]:
        info = tokens[1].split(';')
        prdata = info[0].split(',')
        old_pagerank = prdata[0]
        neighbors = prdata[2:]
        data = info[1].split(',')
    ## otherwise redistribute the pagerank
    else:
        new_pagerank += float(tokens[1])
## apply damping factor to the pagerank
new_pagerank = (1 - d) + d * new_pagerank
if len(neighbors) != 0:
    sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank \
    + "," + ",".join(neighbors)+ ';' + ','.join(data) + '\n')
else:
    sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank \
    + ';' + ','.join(data) + '\n')