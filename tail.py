'''
Basic tail command implementation
Usage:

tail.py filename numlines

'''

import sys
import linecache

print ("here it is")
if len(sys.argv) !=3:
    print ('Usage: tail.py <file> <nlines>')
    sys.exit(1)

# filename and number of lines requested
fname, nlines = sys.argv[1:]
nlines = int(nlines)

# count the total number of lines
tot_lines = len(open(fname).readlines())

# use line cache module to read the lines
for i in range(tot_lines - nlines + 1, tot_lines+1):
    print (linecache.getline(sys.argv[1],i))