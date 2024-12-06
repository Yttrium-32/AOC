stdin = open(0)

nums_1 = []
nums_2 = []

for line in stdin:
    i, j = map(int, line.split())
    nums_1.append(i)
    nums_2.append(j)

nums_1.sort()
nums_2.sort()

total_dist = 0
for i in range(len(nums_1)):
    dist = abs(nums_1[i] - nums_2[i])
    total_dist += dist

print(total_dist)

