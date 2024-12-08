import re

def func1(updates):
    del_ind = []
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
            del_ind.append(k)
    
    for ind in reversed(del_ind):
        del(updates[ind])

def func2(updates, res):
    for update in updates:
        valid = False
        update = list(reversed(update.split(',')))
        while(not valid):    
            valid = True
            for i, val_i in enumerate(update):
                for j, val_j in enumerate(update):
                    if i < j:
                        #print(val_j, rules.get(val_i, []))
                        if val_j in rules.get(val_i, []):
                            update[i], update[j] = update[j], update[i]
                            valid = False
            if valid:

                middle = int((len(update)+1)/2)
                res += int(update[middle-1])
    return res

with open("5-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

rules = {}

updates = []
for line in lines:
    if '|' in line:
        values = line.split('|')
        rules[values[0]] = rules.get(values[0], []) + [values[1]]
    if ',' in line:
        updates.append(line)

func1(updates)
res = 0
res = func2(updates, res)
print(res)


#print(rules)
#print(updates)
#print(res)

