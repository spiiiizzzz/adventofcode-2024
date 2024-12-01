def presence_score(n: int, l: list[int]) -> int:
    presence = 0
    for i in l:
        if n == i:
            presence += n
    return presence


def get_lists(raw: str) -> tuple[list[int]]:
    list_1 = []
    list_2 = []
    for line in raw:
        (a, b) = line.strip().split('   ')
        list_1.append(int(a))
        list_2.append(int(b))
    return (list_1, list_2)


def main():
    with open("input.txt", "r") as f:
        list_1, list_2 = get_lists(f.readlines())
    similarity = 0
    for i in range(0, len(list_1)):
        similarity += presence_score(list_1[i], list_2)
    print(similarity)


if __name__ == "__main__":
    main()