#
# A bit overengineered maybe
# But whatever, it works quite nicely
#

def distance(a: int, b: int) -> int:
    return abs(a-b)


def get_lists(raw: str) -> tuple[list[int]]:
    list_1 = []
    list_2 = []
    for line in raw:
        (a, b) = line.strip().split('   ')
        list_1.append(int(a))
        list_2.append(int(b))
    list_1.sort()
    list_2.sort()
    return (list_1, list_2)


def main():
    with open("input.txt", "r") as f:
        list_1, list_2 = get_lists(f.readlines())
    total_distance = 0
    for i in range(0, len(list_1)):
        total_distance += distance(list_1[i], list_2[i])
    print(total_distance)


if __name__ == "__main__":
    main()