import re

def grep(fn, pattern):
  with open(fn, mode='r') as f:
    for line in f:
      if re.match(pattern, line):
        print(line)

p = '^def'
fn = 'fib.py'
grep(fn,p)

import subprocess
def subprocGrep(fn, pattern):
  ret = subprocess.run(['grep', pattern, fn], text=True, capture_output=True)
  print(ret.stdout.strip())

subprocGrep(fn,p)