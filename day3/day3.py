import re


def main():
    with open("input.txt", "r") as f:
        raw = f.read()
        total = 0
        matches = re.findall("mul\\([0-9]+,[0-9]+\\)", raw)
        for m in matches:
            nums = tuple(map(int, m[4:-1].split(",")))
            total += nums[0] * nums[1]
        print(total)


if __name__ == "__main__":
    main()