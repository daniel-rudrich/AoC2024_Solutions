import re

with open("5-example.txt") as file:
    lines = [line.strip() for line in file.readlines()]

rules = {}

updates = []
for line in lines:
    if '|' in line:
        values = line.split('|')
        rules[values[0]] = rules.get(values[0], []) + [values[1]]
    if ',' in line:
        updates.append(line)

res = 0
for k, update in enumerate(updates):
    update = list(reversed(update.split(',')))
    valid = True
    for i, val_i in enumerate(update):
        for j, val_j in enumerate(update):
            if i < j:
                #print(val_j, rules.get(val_i, []))
                if val_j in rules.get(val_i, []):
                    valid = False
    if valid:
        print(k)
        middle = int((len(update)+1)/2)
        res += int(update[middle-1])
        
#print(rules)
#print(updates)
print(res)

