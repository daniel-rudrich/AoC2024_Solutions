import re

direction = "up"
done = False
loop = 0
with open("6-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]



matrix: list[list[int]] =  [[0]] * len(lines)
matrix_valid = {}
#print(matrix_valid)
# Find the guard
for index, line in enumerate(lines):
    matrix[index] = [x for x in line]
#print(matrix)
pos = (0,0)


for i, row in enumerate(matrix):
    for j, column in enumerate(matrix):
        if matrix[i][j] == "^":
            pos = (i,j)

start_pos = pos
def checkin(position):
    global matrix
    return position[0] >= 0 and position[1] >= 0 and position[0] < len(matrix[0]) and position[1] < len(matrix)

def step():
    global pos
    global direction
    if direction == "up":
        tmp = (pos[0]-1,pos[1])
        if checkin(tmp):
            if matrix[tmp[0]][tmp[1]] == '#':
                direction = "right"
                return
    if direction == "down":
        tmp = (pos[0]+1,pos[1])
        if checkin(tmp):
            if matrix[tmp[0]][tmp[1]] == '#':
                direction = "left"
                return
    if direction == "left":
        tmp = (pos[0],pos[1]-1)
        if checkin(tmp):
            if matrix[tmp[0]][tmp[1]] == '#':
                direction = "up"
                return
    if direction == "right":
        tmp = (pos[0],pos[1]+1)
        if checkin(tmp):
            if matrix[tmp[0]][tmp[1]] == '#':
                direction = "down"
                return
    pos = tmp

while checkin(pos):
    matrix_valid[pos] = 0
    step()

blocker = {}
end_loop = False
def step2(mat):
    global pos
    global direction
    global end_loop
    global loop
    tmp = (0,0)
    if direction == "up":
        tmp = (pos[0]-1,pos[1])
        if checkin(tmp):
            if mat[tmp[0]][tmp[1]] == '#':
                if blocker.get(tmp, 0) == 1:
                    loop += 1
                    end_loop = True
                else:
                    blocker[tmp] = 1
                direction = "right"
                return
    if direction == "down":
        tmp = (pos[0]+1,pos[1])
        if checkin(tmp):
            if mat[tmp[0]][tmp[1]] == '#':
                if blocker.get(tmp, 0) == 1:
                    loop += 1
                    end_loop = True
                else:
                    blocker[tmp] = 1
                direction = "left"
                return
    if direction == "left":
        tmp = (pos[0],pos[1]-1)
        if checkin(tmp):
            if mat[tmp[0]][tmp[1]] == '#':
                if blocker.get(tmp, 0) == 1:
                    loop += 1
                    end_loop = True
                else:
                    blocker[tmp] = 1
                direction = "up"
                return
    if direction == "right":
        tmp = (pos[0],pos[1]+1)
        if checkin(tmp):
            if mat[tmp[0]][tmp[1]] == '#':
                if blocker.get(tmp, 0) == 1:
                    loop += 1
                    end_loop = True
                else:
                    blocker[tmp] = 1
                direction = "down"
                return
    pos = tmp

matrix_valid.pop(start_pos)
pos = start_pos
for entry in matrix_valid:
    new_list = matrix.copy()
    if entry == start_pos:
        continue
    new_list[entry[0]][entry[1]] = '#'
    while checkin(pos) and not end_loop:
        step2(new_list)
    pos = start_pos
    blocker = {}
    end_loop = False
    

print(loop)

