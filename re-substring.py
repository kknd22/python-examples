# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

str=input("enter the string:")
print(f'\n{str}')
sub=input("enter the substring:")
print(f'\n{sub}')

if (len(str)< 1 or len(str)>99):
  print(f'{str} length is not between 0 - 100')
  exit(1)
if (len(sub)<1 or len(sub)>len(str)):
  print(f'{sub} length is not between 0 - {len(str)}')
  exit(2)
r = re.finditer(fr'{sub}', str, flags=)
if r:
    for it in r:
      print(it)
      print(f'({it.start}, {it.end})')
else:
  print (-1, -1)  