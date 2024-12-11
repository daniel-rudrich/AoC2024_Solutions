from collections import defaultdict

with open("10-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

# print(line)

trailheads = []

x_bound = len(lines[0])
y_bound = len(lines)

for i, line in enumerate(lines):
    for j, num in enumerate(line):
        if num == '0':
            trailheads.append((i, j))

print("Part2: Trailheads: ", trailheads)


def step(pos: tuple[int, int]) -> int:
    score = 0
    x, y = pos[0], pos[1]
    curr_val = int(lines[x][y])
    if curr_val == 9:
        return 1
    # Check each direction
    if x + 1 < x_bound:
        if int(lines[x+1][y]) == curr_val + 1:
            score += step((x+1, y))
    if x - 1 >= 0:
        if int(lines[x-1][y]) == curr_val + 1:
            score += step((x-1, y))
    if y + 1 < y_bound:
        if int(lines[x][y+1]) == curr_val + 1:
            score += step((x, y+1))
    if y - 1 >= 0:
        if int(lines[x][y-1]) == curr_val + 1:
            score += step((x, y-1))
    return score


scores = 0
for trailhead in trailheads:
    score = step(trailhead)
    scores += score


print("Part 2: ", scores)
