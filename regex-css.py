import re

with open ('test-data/regex-css.data') as f:
    flag = False
    for line in f:

        if not flag:
            if re.search('{', line):
                flag = True
            continue
        else:
            if re.search('}', line):
                flag = False
                continue
            r = re.findall(r'#[A-Fa-f0-9]{3,6}', line)
            for c in r:
                print(c)
