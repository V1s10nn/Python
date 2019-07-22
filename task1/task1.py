import sys
import argparse as argp
import numpy as np

def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-n', '--name', required=True)
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])


with open(namespace.name) as f:

    a = [float(line.rstrip('\n')) for line in f]

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