import re

def get_nums(lst: list[str]):
    num_names = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    num_pttrn = re.compile(r"one|two|three|four|five|six|seven|eight|nine|[0-9]")
    nums = ""

    if len(nums) > 2:
        nums = nums[0] + nums[-1]
    elif len(nums) == 1:
        nums = nums*2

    return nums


def main():
    stdin = open(0)

    num_list: list[int] = []

    for line in stdin:
        try:
            inp_string_lst = list(line)
        except Exception as e:
            print(f"err: {e}")

        nums = get_nums(inp_string_lst)
        print(nums)
        num_list.append(nums)

    sum: int = 0
    for num in num_list:
        sum += int(num)

    print(sum)

if __name__ == "__main__":
    main()
