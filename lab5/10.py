from posixpath import split
import re
pattern = '[A-Z][a-z]+'
results = re.findall(pattern, input())
results = [i.lower() for i in results]
print(*results, sep = "_")
