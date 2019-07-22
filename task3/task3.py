import sys
import argparse as argp

def createParser ():
    parser = argp.ArgumentParser()
    parser.add_argument ('-n', '--name', required=True)
    return parser

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

path = namespace.name

with open(path+"/cash1.txt") as f1:

    a1 = [float(line.rstrip('\n')) for line in f1]

with open(path+"/cash2.txt") as f2:

    a2 = [float(line.rstrip('\n')) for line in f2]

with open(path+"/cash3.txt") as f3:

    a3 = [float(line.rstrip('\n')) for line in f3]

with open(path+"/cash4.txt") as f4:

    a4 = [float(line.rstrip('\n')) for line in f4]

with open(path+"/cash5.txt") as f5:

    a5 = [float(line.rstrip('\n')) for line in f5]


b = [a1,a2,a3,a4,a5]

c = [sum(i) for i in zip(*b)]

print(c.index(max(c)) + 1)