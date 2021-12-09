import re

with open('test-data/and-or.txt', 'r') as f:
    for line in f:
        print(re.sub(r'(?<=\s)&&|\|\|(?=\s)', lambda x: 'and' if x.group(0) == '&&' else 'or', line))
