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
        if char != 'A':
            continue
        if 0 < j < len(row) - 1 and 0 < i < len(matrix) - 1:
            if matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S':
                if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    xmas_count += 1
                if matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    xmas_count += 1
            if matrix[i-1][j-1] == 'S' and matrix[i+1][j+1] == 'M':
                if matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S':
                    xmas_count += 1
                if matrix[i-1][j+1] == 'S' and matrix[i+1][j-1] == 'M':
                    xmas_count += 1
            
        
print(xmas_count)
#print(text)