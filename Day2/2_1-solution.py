

def Check_Valid(report: str) -> int:
    asc: bool = None
    levels = [int(x) for x in report.split(" ")]
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
    
    isValid: int = Check_Valid(report)
    print(f"{report}: {isValid}")
    valid_count += isValid

print(valid_count)


