import json

with open('sample-data.json', 'r') as f:
  data = f.read()

table = dict()
database = list()
a = json.loads(data)
n = ["dn", "speed", "delay", "id"]
for j in a["imdata"] :
    for i in n :
        table[i] = j["l1PhysIf"]["attributes"][i]
        database.append(table)

print("Interface Status")
print("==========================================================================")
print ("{:<45} {:<10} {:<8} {:<10}".format(n[0], n[1], n[2], n[3]))
print("------------------------------------------    --------   -------  --------")
for k in database:
    print ("{:<45} {:<10} {:<8} {:<10}".format(k[n[0]], k[n[1]], k[n[2]], k[n[3]]))