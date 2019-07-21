with open(input('Select File: ')) as f:

    a = [float(line.rstrip('\n')) for line in f]

import numpy as np
p = round(np.percentile(a,90),2)
m = round(np.percentile(a,50),2)
maxl = round(max(a),2)
minl = round(min(a),2)
me = round(np.mean(a),2)

print(p)
print(m)
print(maxl)
print(minl)
print(me)