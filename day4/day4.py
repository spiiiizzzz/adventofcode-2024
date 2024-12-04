def check_for_match(matrix: list[str], coords: tuple[int]) -> int:
    directions = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    total = 0

    for direction in directions:
        valid = True
        for i in range(0, len("XMAS")):
            try:
                # Python accepts negative number indexes as "count from the end of the string"
                # which of course messes up the counting, so this check needs to be here
                if coords[1]+direction[1]*i < 0 or coords[0]+direction[0]*i < 0:
                    valid = False
                    break
                if not (matrix[coords[1]+direction[1]*i][coords[0]+direction[0]*i] == "XMAS"[i]):
                    valid = False
                    break
            except IndexError:
                valid = False
                break
        if valid:
            # Used this for debug
            # tmp = list(map(str.lower, matrix))
            # for i in range(0, len("XMAS")):
            #     tmp[coords[1]+direction[1]*i] = "".join(tmp[coords[1]+direction[1]*i][:coords[0]+direction[0]*i] + tmp[coords[1]+direction[1]*i][coords[0]+direction[0]*i].capitalize() + tmp[coords[1]+direction[1]*i][coords[0]+direction[0]*i+1:])
            # print("=======================")
            # for line in tmp:
            #     print(line)
            # print("=======================")
            total += 1

    return total

def main():
    with open("input.txt", "r") as f:
        matrix = list(map(str.strip, f.readlines()))
        total = 0
        for j in range(0, len(matrix)):
            for i in range(0, len(matrix[j])):
                if matrix[j][i] == "X":
                    total += check_for_match(matrix, (i, j))
        print(total)

if __name__ == "__main__":
    main()