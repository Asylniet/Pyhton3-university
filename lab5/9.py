import re

str = 'BruceWayneIsBatman'
words = re.findall('[A-Z][a-z]*', str)
for i in words :
    print(i, end = " ")
