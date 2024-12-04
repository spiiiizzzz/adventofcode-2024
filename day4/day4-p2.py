def check_for_match(matrix: list[str], coords: tuple[int]) -> bool:
    if coords[1]-1 < 0 or coords[0]-1 < 0:
        return False

    try:
        diag1 = matrix[coords[1]-1][coords[0]-1] + matrix[coords[1]][coords[0]] + matrix[coords[1]+1][coords[0]+1]
        diag2 = matrix[coords[1]-1][coords[0]+1] + matrix[coords[1]][coords[0]] + matrix[coords[1]+1][coords[0]-1]
    except IndexError:
        return False

    if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
        return True
    else:
        return False


def main():
    with open("input.txt", "r") as f:
        matrix = list(map(str.strip, f.readlines()))
        total = 0
        for j in range(0, len(matrix)):
            for i in range(0, len(matrix[j])):
                if matrix[j][i] == "A":
                    total += check_for_match(matrix, (i, j))
        print(total)

if __name__ == "__main__":
    main()