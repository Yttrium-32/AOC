stdin = open(0)

nums_1 = []
nums_2 = []

for line in stdin:
    i, j = map(int, line.split())
    nums_1.append(i)
    nums_2.append(j)

sim_score = 0

nums_2_freq = {}

for i in nums_2:
    try:
        nums_2_freq[i] += 1
    except KeyError:
        nums_2_freq[i] = 1

for i in nums_1:
    sim_score += i * (nums_2_freq[i] if i in nums_2_freq else 0)

print(sim_score)

