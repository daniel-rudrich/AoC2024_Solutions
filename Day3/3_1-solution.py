import re

with open("3-input.txt") as file:
    text = file.read()

#print(text)
regex_string = "mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)"

x = re.findall(regex_string,text)
sum = 0 
for match in x:
    sum += int(match[0])*int(match[1])

print(sum)