import re

stdin = open(0)

lines = ""
for line in stdin:
    lines += " "
    lines += line[:-1]

active_matches = re.findall(r"do\(\).*?don't\(\)", lines)

first_active_group = re.search(r"^.*?don't\(\)", lines)
if first_active_group:
    active_matches.append(first_active_group.group(0))

# last_active_group = re.search(r".*do\(\)(.*)$", lines)
# if last_active_group:
    # active_matches.append(last_active_group.group(1))

for i in active_matches:
    print(i, "\n")

sum = 0
for match in active_matches:

    print(f"{match=}")
    m = re.findall(r"mul\(\d+\,\d+\)", match)
    print(f"{m=}")

    for expr in m:
        nums = expr[4:][:-1]
        print(f"{expr=}")
        n1, n2 = map(int, nums.split(","))
        print(f"{n1=}, {n2=}")
        sum += n1 * n2
    print()

print(sum)

