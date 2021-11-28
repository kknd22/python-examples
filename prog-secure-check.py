import subprocess
import re

def checkSecureProgram(prog):
  pattern = '\w'
  if not re.match(pattern, prog):
    print(f'Sorry {prog} is NOT a valid command')
    exit(1)
  
  r = subprocess.run(['which', prog], capture_output=True, text=True)
  if (r.returncode == 0):
    print("{} is a validate command, located at {}".format(prog, r.stdout))
  else:
    print(f'Sorry {prog} is not a installed')
    print(r.stderr)

p = input("enter a linux command: ") 
checkSecureProgram(p)   
