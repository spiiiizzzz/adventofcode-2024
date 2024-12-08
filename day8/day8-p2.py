import itertools

def line_eq(x: int, p1: tuple[int], p2: tuple[int]) -> int:
    return int((x - p1[0])/(p2[0] - p1[0])*(p2[1] - p1[1]) + p1[1])

def is_point_valid(grid: list[str], p, p1, p2) -> bool:
    if p[0] < 0 or p[1] < 0:
        return False
    try:
        if p[1] > len(grid) or p[0] >= len(grid[p[1]]):
            return False
    except IndexError:
        return False
    return True

def main():
    with open("input.txt", "r") as f:
        grid = list(map(str.strip, f.readlines()))

        frequencies = {}

        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                if grid[j][i] != '.':
                    if not grid[j][i] in frequencies.keys():
                        frequencies[grid[j][i]] = []
                    frequencies[grid[j][i]].append((i, j))

        antinodes = set()

        for k, v in frequencies.items():
            for p1, p2 in itertools.combinations(v, 2):
                dist = (abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
                points = set([p1, p2])
                left_most = p1 if p1[0] < p2[0] else p2
                right_most = p1 if p1[0] > p2[0] else p2

                i = 1
                while (left_most[0] - dist[0]*i >= 0):
                    points.add((left_most[0]-dist[0]*i, line_eq(left_most[0]-dist[0]*i, p1, p2)))
                    i += 1
                
                i = 1
                while (right_most[0] + dist[0]*i < len(grid[0])):
                    points.add((right_most[0]+dist[0]*i, line_eq(right_most[0]+dist[0]*i, p1, p2)))
                    i += 1
                        
                for p in points:
                    if is_point_valid(grid, p, p1, p2):
                        antinodes.add(p)

        print(len(antinodes))


if __name__ == "__main__":
    main()