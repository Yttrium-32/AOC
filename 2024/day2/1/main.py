stdin = open(0)

levels = []
for line in stdin:
    levels.append(list(map(int, line.split())))

safe_count = 0
for level in levels:

    inc, dec = False, False
    i, j = 0, 1
    if level[i] > level[j]:
        dec = True
    else:
        inc = True

    print(f"{level=}")

    while j < len(level):
        is_safe = True
        if level[i] == level[j]:
            is_safe = False
            break
        if abs(level[i] - level[j]) > 3:
            is_safe = False
            break
        if dec and level[i] < level[j]:
            is_safe = False
            break
        if inc and level[i] > level[j]:
            is_safe = False
            break

        i += 1
        j += 1

    if is_safe:
        safe_count += 1
        print("safe")
    else:
        print("unsafe")
    print()

print(safe_count)

