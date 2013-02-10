#!/bin/bash
./data/pagerank-map.py < local_test_data/$1.dta | sort -k 1,1 | ./data/pagerank-reduce.py | ./data/process-map.py | sort -k 1,1 | ./data/process-reduce.py > local_test_results/$1.out