from collections import defaultdict

with open("8-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

x_bound = len(lines[0])
y_bound = len(lines)

print(x_bound, y_bound)

# Dict of sign + position
antenna = defaultdict(list)
nodes = []
# 5,2 8,1 => 2,3 11,0
# diff -3 1
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '.':
            continue
        for ant in antenna.get(char, []): 
            diff = (ant[0]-x,ant[1]-y)
            # remove the loop for part 1
            for prod in range(0,x_bound):
                nodes.append((ant[0]+(diff[0]*prod),ant[1]+(diff[1]*prod)))
                nodes.append((x-(diff[0]*prod), y-(diff[1]*prod)))
        antenna[char].append((x,y))


nodes_set = set(nodes)
res = 0
for node in nodes_set:
    if node[0] in range(0, x_bound) and node[1] in range(0, y_bound):
        res += 1

print(res)