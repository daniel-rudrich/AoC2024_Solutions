from collections import defaultdict

with open("9-input.txt") as file:
    line = [line.strip() for line in file.readlines()][0]

# print(line)

blocks = []

file_id = 0
for i, num in enumerate(line):
    if i % 2 == 0:
        # File
        blocks.extend([str(file_id)]*int(num))
        file_id += 1
    else:
        # empty
        blocks.extend(["."]*int(num))

# print("Before compression:  ", ''.join(blocks))

checksum = 0
for j, id in enumerate(blocks):
    if blocks[j] == '.':
        last = '.'
        while last == '.':
            last = blocks.pop()
        if j >= len(blocks):
            break
        blocks[j] = last
    checksum += j * int(blocks[j])

# print("After compression:   ", ''.join(blocks))
print("Part 1 Checksum: ", checksum)

blocks_2 = []

file_id_2 = 0
for i, num in enumerate(line):
    if (int(num) == 0):
        continue
    if i % 2 == 0:
        # File
        blocks_2.append([str(file_id_2)]*int(num))
        file_id_2 += 1
    else:
        # empty
        blocks_2.append(["."]*int(num))

# print("Blocks: ", blocks_2)

for j, block in enumerate(blocks_2):
    if block[0] == '.':
        free_space = len(block)
        pointer = 0
        i = len(blocks_2) - 1
        while free_space > 0 and i > j:
            # print("free space: ", free_space, "j = ", j , "i = ", i)
            if blocks_2[i][0] == '.':
                i -= 1
                continue
            if len(blocks_2[i]) <= free_space:
                for k in range(0, len(blocks_2[i])):
                    blocks_2[j][pointer] = blocks_2[i][k]
                    blocks_2[i][k] = '.'
                    free_space -= 1
                    pointer += 1
            i -= 1

    # print(blocks_2)


# print("Part2 after compression:", ''.join([''.join(x) for x in blocks_2]))
checksum_id = 0
checksum_2 = 0
for block in blocks_2:
    for id in block:
        if id != '.':
            checksum_2 += checksum_id*int(id)
        checksum_id += 1

print("Part 2 Checksum: ", checksum_2)
