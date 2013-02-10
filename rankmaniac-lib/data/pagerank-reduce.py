#!/usr/bin/env python

import sys

#
# This program simply represents the identity function.
#

cur_node = ""
d = 0.85
sum = 0
for line in sys.stdin:
    tokens = line.split('\t')
    
    if tokens[0] != cur_node:
        if cur_node != "":
            new_pagerank = (1 - d) + d * new_pagerank
            if len(neighbors) != 0:
                sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank + "," + ",".join(neighbors))
            else:
                sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank + '\n')
        cur_node = tokens[0]
        new_pagerank = 0.0
    if ',' in tokens[1]:
        info = tokens[1].split(',')
        old_pagerank = info[0]
        neighbors = info[2:]
    else:
        new_pagerank += float(tokens[1])
new_pagerank = (1 - d) + d * new_pagerank
if len(neighbors) != 0:
    sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank + "," + ",".join(neighbors))
else:
    sys.stdout.write(cur_node + "\t" + str(new_pagerank) + "," + old_pagerank + '\n')