def is_safe(l: list[int]) -> bool:
    descending = l[0] > l[1]

    for i in range(0, len(l)-1):
        if descending:
            if l[i] <= l[i+1]:
                return False
        else:
            if l[i] >= l[i+1]:
                return False
        if abs(l[i] - l[i+1]) > 3:
            return False
    
    return True

def main():
    with open("input.txt", "r") as f:
        safe = 0
        for line in f.readlines():
            if is_safe(list(map(int, line.strip().split(" ")))):
                safe += 1
        print(safe)

if __name__ == "__main__":
    main()