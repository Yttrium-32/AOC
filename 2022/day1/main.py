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

print(max(elves))
