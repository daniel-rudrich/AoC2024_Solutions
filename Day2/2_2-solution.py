import copy

def Check_Valid_Rec(levels: list[int], asc: bool) -> int:
    for i in range(1,len(levels)):
        diff = abs(levels[i]-levels[i-1])
        if diff > 3 or diff == 0:
            list_left, list_right = copy.deepcopy(levels), copy.deepcopy(levels)
            del list_left[i-1]
            del list_right[i]
            return Check_Valid_Step(list_left) or Check_Valid_Step(list_right)
        if asc:
            if levels[i-1] > levels[i]:
                list_left, list_right = copy.deepcopy(levels), copy.deepcopy(levels)
                del list_left[i-1]
                del list_right[i]
                return Check_Valid_Step(list_left) or Check_Valid_Step(list_right)
        else:
            if levels[i-1] < levels[i]:
                list_left, list_right = copy.deepcopy(levels), copy.deepcopy(levels)
                del list_left[i-1]
                del list_right[i]
                return Check_Valid_Step(list_left) or Check_Valid_Step(list_right)
    return 1

def Check_Valid_Step(levels: list[int]) -> int:
    asc: bool = None
    for i in range(1,len(levels)):
        diff = abs(levels[i]-levels[i-1])
        if diff > 3 or diff == 0:
            return 0
        if asc == None:
            if levels[i] > levels[i-1]:
                asc = True
            else:
                asc = False
        if asc:
            if levels[i-1] > levels[i]:
                return 0
        else:
            if levels[i-1] < levels[i]:
                return 0
    return 1

with open("2-input.txt") as file:
    reports = [line.strip() for line in file.readlines()]

valid_count: int = 0

for report in reports:
    levels: list[int] = [int(x) for x in report.split(" ")]
    isValid: int = Check_Valid_Rec(levels, False) or Check_Valid_Rec(levels, True)
    print(f"{report}: {isValid}")
    valid_count += isValid

print(valid_count)


