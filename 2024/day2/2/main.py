def is_safe(level: list[int]) -> bool:

    inc, dec = False, False
    i, j = 0, 1
    if level[i] > level[j]:
        dec = True
    else:
        inc = True


    is_safe = True
    while j < len(level):
        found_unsafe = level[i] == level[j] \
                or abs(level[i] - level[j]) > 3 \
                or dec and level[i] < level[j] \
                or inc and level[i] > level[j]

        if found_unsafe:
            is_safe = False
            break
        i += 1
        j += 1

    if is_safe:
        return True
    else:
        return False

stdin = open(0)

levels = []
for line in stdin:
    levels.append(list(map(int, line.split())))

safe_count = 0
for level in levels:
    print(f"{level=}")

    if is_safe(level):
        safe_count += 1
        print("safe\n")
    else:
        for idx in range(len(level)):
            new_level = level[:idx] + level[idx+1:]
            print(f"{new_level=}")
            if is_safe(new_level):
                safe_count += 1
                print("safe\n")
                break
        else:
            print("unsafe\n")


print(safe_count)

