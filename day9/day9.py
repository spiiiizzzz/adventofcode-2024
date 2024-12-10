# BEHOLD: LINEAR TIME COMPLEXITY... technically, it still has to unfold the whole thing which isn't really the best
# Could probably avoid that but whatever, it's still more than enough fast

def main():
    with open("input.txt", "r") as f:
        disk_map = list(map(int, list(f.read().strip())))

        blocks = []

        for i in range(0, len(disk_map)):
            if i % 2 == 0:
                for _ in range(0, disk_map[i]):
                    blocks.append(i//2)
            else:
                for _ in range(0, disk_map[i]):
                    blocks.append(".")

        i_left = 0
        i_right = len(blocks) - 1
        checksum = 0

        while i_left <= i_right:
            if blocks[i_left] != '.':
                checksum += i_left*blocks[i_left]
            else:
                checksum += i_left*blocks[i_right]
                i_right -= 1
                while blocks[i_right] == '.':
                    i_right -= 1
            i_left += 1

        print(checksum)

if __name__ == "__main__":
    main()