import re


def main():
    with open("input.txt", "r") as f:
        raw = f.read()
        total = 0

        start_index = 0
        enabled = True

        while start_index < len(raw):
            if enabled:
                m = re.search("mul\\([0-9]+,[0-9]+\\)|don't\\(\\)", raw[start_index:])
                if m == None:
                    break
                start_index += m.end()
                if m[0][0:3] == "mul":
                    nums = tuple(map(int, m[0][4:-1].split(",")))
                    total += nums[0] * nums[1]
                else:
                    enabled = False
            else:
                m = re.search("do\\(\\)", raw[start_index:])
                if m == None:
                    break
                start_index += m.end()
                enabled = True

        print(total)


if __name__ == "__main__":
    main()