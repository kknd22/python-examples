import re

for i in range(int(input())):
    line = input()
    and_line = re.sub('(?<=\s)&&(?=\s)', 'and', line)
    final = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', and_line)
    print(final)



tmp = re.sub('\s\|\| ', ' or ', 'abc || bcd || ghj')
print(tmp)
tmp = re.sub('\s\|\| ', ' or ', 'abc bcd  ghj')
print(tmp)

p = re.compile('(?<=abc-)\w+')
print(type(p))
print(p)

r = p.search('abc-efg-tyu')
print(type(r))
print(r)
print(r.group())

r2=re.search('\w+(?=-e)', 'abc-efg-tyu'  )
print(r2)