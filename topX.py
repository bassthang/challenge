#!/usr/bin/python3

# problems:
#   read input data efficiently
#   compare a line against current top-n efficiently
#   update current top-n efficiently

# Assumption: n is small compared to number of input lines & available RAM. So we can
# store the top-n set in RAM. Operations on the top-n set are reasonably quick.

# Assumption: input data is randomly ordered. If it is strictly, or even mostly increasing,
# our approach may be slow, as we have to update the top-n set too many times.

# One way to improve efficiency would be to:
#   * partition the input data
#   * read each partition in parallel, finding the top-n for that partition
#   * combine the top-n's and find a global top-n
# I would probably implement this in Go, as goroutines make it very easy to do this.

import sys

n = int(sys.argv[1])
infile = sys.argv[2]

# Store the top-n in set, as we don't care about the order until output
topn = set()
# Store the smallest top-n number seperately for quick comparison
smallestn = None

fh = open(infile, "r")

for l in fh.readlines():
    m = int(l.strip())
    if m in topn:
        # Stop me if you've heard this one before ...
        continue
    if smallestn is None:
        # First time?
        smallestn = m
        topn.add(m)
    elif m > smallestn:
        # They all rolled over, and one fell out
        topn.add(m)
        if len(topn) > n:
            topn.remove(smallestn)
        smallestn = min(topn)

print(sorted(topn))