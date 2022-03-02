import json

with open('sample-data.json', 'r') as f:
  data = f.read()

table = dict()
database = list()
a = json.loads(data)
n = input().split()
for j in a["imdata"] :
    for i in n :
        table[i] = j["l1PhysIf"]["attributes"][i]
        database.append(table)

print("Interface Status")
print("==========================================================================")

for i in n :
    x = len(database[0][i])
    print(f"{i:<{x}}", end = "\t")

print()

for i in n :
    if len(i) < len(database[0][i]) :
        for j in range(len(database[0][i])) :
            print("-", end = "")
        print("", end = "\t")
    else :
        for j in range(len(i)) :
            print("-", end = "")
        print("", end = "\t")

print()

for i in database:
    for j in n :
        print(i[j], end = "\t")

    print()