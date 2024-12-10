def visitable(grid: list[list[int]], e: tuple[int]) -> list[tuple[int]]:
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    res = []
    for d in dirs:
        q = (e[0]+d[0], e[1]+d[1])
        if q[1] < 0 or q[1] >= len(grid) or q[0] < 0 or q[0] >= len(grid[q[1]]):
            continue
        if grid[q[1]][q[0]] == grid[e[1]][e[0]] + 1:
            res.append(q)
    return res
        
nine_reached = []
def DFS(grid:list[list[int]], p: tuple[int]) -> int:
    count = 0
    for q in visitable(grid, p):
        count += DFS(grid, q)
    
    if grid[p[1]][p[0]] == 9 and not p in nine_reached:
        nine_reached.append(p)
        return 1
    else:
        return count


def main():
    with open("input.txt", "r") as f:
        grid = [list(map(int, list(line.strip()))) for line in f.readlines()]
    
        starting_positions = []

        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                if grid[j][i] == 0:
                    starting_positions.append((i, j))

        trail_count = 0
        for p in starting_positions:
            global nine_reached
            nine_reached = []
            trail_count += DFS(grid, p)
        
        print(trail_count)


if __name__ == "__main__":
    main()