with open("1-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

list_a: list[int] = []
list_b: list[int] = []
for line in lines:
    nums = line.split("   ")
    list_a.append(int(nums[0]))
    list_b.append(int(nums[1]))
list_a.sort()
list_b.sort()

distance: int = 0
for i in range(len(list_a)):
    distance += abs(list_a[i] - list_b[i])
print(distance)