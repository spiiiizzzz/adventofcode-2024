# again, I expected it to be WAYYYYYY slower than it actually was
# It only took 3 seconds on my machine
# in Python of all languages


def sum(nums: list[int], res: int) -> bool:
    s = nums[0] + nums[1]
    if len(nums) == 2:
        if s == res:
            return True
        else:
            return False
    else:
        return sum([s]+nums[2:], res) or mul([s]+nums[2:], res) or or_op([s]+nums[2:], res)

def mul(nums: list[int], res: int) -> bool:
    s = nums[0] * nums[1]
    if len(nums) == 2:
        if s == res:
            return True
        else:
            return False
    else:
        return sum([s]+nums[2:], res) or mul([s]+nums[2:], res) or or_op([s]+nums[2:], res)

def or_op(nums: list[int], res: int) -> bool:
    s = int(str(nums[0]) + str(nums[1]))
    if len(nums) == 2:
        if s == res:
            return True
        else:
            return False
    else:
        return sum([s]+nums[2:], res) or mul([s]+nums[2:], res) or or_op([s]+nums[2:], res)

def is_valid(result: int, nums: list[int]) -> bool:
    return sum(nums, result) or mul(nums, result) or or_op(nums, result)

def main():
    with open("input.txt", "r") as f:
        total = 0

        lines = f.readlines()
        for line in lines:
            result, nums = line.strip().split(": ")
            nums = list(map(int, nums.split(" ")))
            result = int(result)

            if is_valid(result, nums):
                total += result

        print(total)

if __name__ == "__main__":
    main()