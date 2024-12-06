stdin = open(0)

num_list: list[int] = []

for line in stdin:
    try:
        inp_string_lst = list(line)
    except Exception as e:
        print(f"err: {e}")

    nums = ""
    for char in inp_string_lst:
        if char.isdigit():
            nums += char
    print(f"{inp_string_lst=}")
    print(f"{nums=}")

    if len(nums) > 2:
        nums = nums[0] + nums[-1]
    elif len(nums) == 1:
        nums = nums*2


    print(nums)
    num_list.append(nums)

sum: int = 0
for num in num_list:
    sum += int(num)

print(sum)

    
