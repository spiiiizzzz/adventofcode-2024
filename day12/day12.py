# Flood-fill let's gooooooo
def adjacent(grid: list[list[str]], p: tuple[int]) -> list[tuple[int]]:
    res = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in directions:
        if p[1]+d[1] < len(grid) and p[1]+d[1] >= 0 and p[0] + d[0] < len(grid[p[1]+d[1]]) and p[0] + d[0] >= 0 and grid[p[1]][p[0]] == grid[p[1]+d[1]][p[0]+d[0]]:
            res.append((p[0]+d[0], p[1]+d[1]))
    return res

visited = []
def DFS(grid: list[list[str]], p: tuple[int]) -> tuple[int]:
    area = 1
    adj = adjacent(grid, p)
    perimeter = 4 - len(adj)
    global visited
    for v in adj:
        if not v in visited:
            visited.append(v)
            res = DFS(grid, v)
            area += res[0]
            perimeter += res[1]
    return (area, perimeter)

def main():
    with open("input.txt", "r") as f:
        grid = [list(line) for line in list(map(str.strip, f.readlines()))]

        total = 0
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                global visited
                if not (i, j) in visited:
                    visited.append((i, j))
                    res = DFS(grid, (i, j))
                    total += res[0]*res[1]

        print(total)

if __name__ == "__main__":
    main()