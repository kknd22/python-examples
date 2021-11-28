import re

txt = "Here is 56 something terribffic"

rtxt = re.findall("[a-m]", txt)
print(rtxt)

rtxt = re.findall("\d", txt)
print(rtxt)

rtxt = re.findall("s.m.", txt)
print(rtxt)

rtxt = re.findall("r{2}", txt)
print(rtxt)
