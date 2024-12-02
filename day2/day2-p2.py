def is_safe(l: list[int], can_remove: bool = True) -> bool:
    descending = l[0] > l[1]

    removed = False

    for i in range(0, len(l)-1):
        if descending:
            if l[i] <= l[i+1]:
                removed = True
        else:
            if l[i] >= l[i+1]:
                removed = True
        if abs(l[i] - l[i+1]) > 3:
            removed = True

        if removed and can_remove:
            middle_removed = is_safe(l[:i] + l[i+1:], False)
            right_removed = is_safe(l[:i+1] + l[i+2:], False)
            left_removed = is_safe(l[:i-1] + l[i:], False) if i != 0 else False
            if (middle_removed or left_removed or right_removed):
                return True
            else:
                return False
        elif removed:
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