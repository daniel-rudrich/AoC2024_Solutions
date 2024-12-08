import re

with open("4-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

matrix: list[list[int]] =  [[0]] * len(lines)

for index, line in enumerate(lines):
    matrix[index] = [x for x in line]

xmas_count = 0
print(matrix)
for i, row in enumerate(matrix):
    for j, char in enumerate(row):
        if char != 'X':
            continue
        # horizontal
        if j >= 3:
        # left
            if (row[j-3] + row[j-2] + row[j-1] + char) == "SAMX":
                xmas_count += 1
            if i < len(matrix) - 3:
                if(matrix[i][j] + matrix[i+1][j-1] + matrix[i+2][j-2] + matrix[i+3][j-3] == "XMAS"):
                    xmas_count += 1 
            if i >= 3:
                if(matrix[i][j] + matrix[i-1][j-1] + matrix[i-2][j-2] + matrix[i-3][j-3] == "XMAS"):
                    xmas_count += 1
        if j < len(row) - 3:
        # right
            if (char + row[j+1] + row[j+2] + row[j+3]) == "XMAS":
                xmas_count += 1
            if i < len(matrix) - 3:
                if(matrix[i][j] + matrix[i+1][j+1] + matrix[i+2][j+2] + matrix[i+3][j+3] == "XMAS"):
                    xmas_count += 1 
            if i >= 3:
                if(matrix[i][j] + matrix[i-1][j+1] + matrix[i-2][j+2] + matrix[i-3][j+3] == "XMAS"):
                    xmas_count += 1   
        # vertical
        if i >= 3:
            # down
            print(i)
            if(matrix[i-3][j] + matrix[i-2][j] + matrix[i-1][j] + matrix[i][j] == "SAMX"):
                xmas_count += 1
        if i < len(matrix) -3:
            if(matrix[i][j] + matrix[i+1][j] + matrix[i+2][j] + matrix[i+3][j] == "XMAS"):
                xmas_count += 1
            
        
print(xmas_count)
#print(text)