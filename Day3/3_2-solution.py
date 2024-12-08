import re

with open("3-input.txt") as file:
    text = file.read().replace("\n",'')

text = text + "do()"
leftover = re.sub("don't\(\).*?do\(\)",'', text)
print("leftover: " +leftover)
regex_string = "mul\((?P<num1>\d{1,3}),(?P<num2>\d{1,3})\)"

x = re.findall(regex_string,leftover)
sum = 0 
for match in x:
    sum += int(match[0])*int(match[1])

print(sum)