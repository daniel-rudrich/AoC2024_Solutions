import sys

sys.set_int_max_str_digits(100000000)
with open("7-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

res1 = 0
part1 = []
for index, line in enumerate(lines):
    test_value = int(line.split(":")[0])
    values = line.split(" ")[1:]
    poss_values = [int(values[0])]
    for value in values[1:]:
        new_poss_values = []
        for pos_val in poss_values:
            if int(pos_val) * int(value) <= test_value:
                new_poss_values.append(int(pos_val)*int(value))
            if int(pos_val) + int(value) <= test_value:
                new_poss_values.append(int(pos_val)+int(value))
        poss_values = new_poss_values
    if test_value in poss_values:
        part1.append(index)
        res1 += int(test_value)

print(res1)

res2 = 0
for j, line_j in enumerate(lines):
    if j in part1:
        continue
    test_value = int(line_j.split(":")[0])
    values = line_j.split(" ")[1:]
    poss_values = [values[0]]
    for value in values[1:]:
        new_poss_values = []
        for pos_val in poss_values:
            if int(pos_val) * int(value) <= test_value:
                new_poss_values.append(int(pos_val)*int(value))
            if int(pos_val) + int(value) <= test_value:
                new_poss_values.append(int(pos_val)+int(value))
            if int(str(pos_val) + value) <= test_value:
                new_poss_values.append(int(str(pos_val) + value))
        poss_values = new_poss_values
    if test_value in poss_values:
        res2 += int(test_value)

print(res2)

print(res1+res2)