elves = [0]
while True:
    try:
        line = input()
    except:
        break

    if line == "":
        elves.append(0)
    else:
        elves[-1] += int(line)

elves.sort()
print(elves[-1] + elves[-2] + elves[-3])
