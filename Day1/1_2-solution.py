with open("1-input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

list_a: list[int] = []
list_b: list[int] = [9]
for line in lines:
    nums = line.split("   ")
    list_a.append(int(nums[0]))
    list_b.append(int(nums[1]))

score: int = 0
for num in list_a:
    appearance = 0
    appearance += len([x for x in list_b if x == num])
    score += (num*appearance)
print(score)