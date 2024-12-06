import re

stdin = open(0)

sum = 0
for line in stdin:

    matches = re.findall(r"mul\(\d+\,\d+\)", line)

    for expr in matches:
        nums = expr[4:][:-1]
        print(f"{expr=}")
        n1, n2 = map(int, nums.split(","))
        print(n1, n2)
        print()
        sum += n1 * n2

print(sum)

