import re

for i in range(int(input())):
    line = input()
    and_line = re.sub('(?<=\s)&&(?=\s)', 'and', line)
    final = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', and_line)
    print(final)