import subprocess

def checkProgram(prog):
  r = subprocess.run(['which', prog], capture_output=True, text=True)
  if (r.returncode == 0):
    print("{} is a validate command, located at {}".format(prog, r.stdout))
  else:
    print(f'Sorry {prog} is not a installed')
    print(r.stderr)

p = input("enter a linux command: ") 
checkProgram(p)   
