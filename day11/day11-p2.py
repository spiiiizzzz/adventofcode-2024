## gave me some problems, but functools came to the rescue :)

from functools import cache

@cache
def blink(i: int, blink_count: int) -> int:
    if blink_count == 0:
        return 1
    elif i == 0:
        return blink(1, blink_count-1)
    elif len(str(i)) % 2 == 0:
        return blink(int(str(i)[:len(str(i))//2]), blink_count-1) + blink(int(str(i)[len(str(i))//2:]), blink_count-1)
    else:
        return blink(i*2024, blink_count-1)

def main():
    with open("input.txt", "r") as f:
        stones = list(map(int, f.read().strip().split(" ")))

        total = 0
        for i in stones:
            total += blink(i, 75)

        print(total)




if __name__ == "__main__":
    main()