import re

import re
f = open("document.xml", 'r')
pattern = re.compile('o:gfxdata="(.+?)"')
results = ()
for l in f:
   results = pattern.findall(l) 

strings = []
if results:
    for item in results:
        strings.append(''.join(item.split('&#xA;')))

for i in strings:
    print(i)

f = open("zips.txt", 'r')
stringLine = []
for l in f:
    tmp = l.split('&#xA;')
    tmp = ''.join(tmp).strip()
    stringLine.append(tmp)

for i in stringLine:
    print(i)
