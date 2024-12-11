## problems seems deceptively simple
## I fear part 2

def blink(l: list[int]) -> list[int]:
    new = []
    for i in l:
        if i == 0:
            new.append(1)
        elif len(str(i)) % 2 == 0:
            new.append(int(str(i)[:len(str(i))//2]))
            new.append(int(str(i)[len(str(i))//2:]))
        else:
            new.append(i*2024)
    return new


def main():
    with open("input.txt", "r") as f:
        stones = list(map(int, f.read().strip().split(" ")))

        for _ in range(0, 25):
            stones = blink(stones)

        print(len(stones))




if __name__ == "__main__":
    main()