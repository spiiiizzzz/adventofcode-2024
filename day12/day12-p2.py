# This might be the messiest code i've ever written
# No i'm not gonna comment anything, i don't want anything to do with this anymore

import itertools

def contiguous(a: tuple[int], b: tuple[int]) -> bool:
    return a[1]+1 == b[0] or b[1]+1 == a[0]

def overlapping(a: tuple[int], b: tuple[int]) -> bool:
    return True if len(set(range(a[0], a[1]+1)).intersection(range(b[0], b[1]+1))) > 0 else False

def merge():
    global sides
    to_merge = []
    to_remove = []
    done = False
    while not done:
        to_merge = []
        to_remove = []
        done = True
        for i, j in itertools.combinations(sides, 2):
            if i[0] == j[0] and i[1] == j[1] and (contiguous(i[2], j[2]) or overlapping(i[2], j[2])):
                done = False
                merged = [i[0], i[1], (min(i[2][0], j[2][0]), max(i[2][1], j[2][1]))]
                if not i in to_remove:
                    to_remove.append(i)
                if not j in to_remove:
                    to_remove.append(j)
                if not merged in to_merge:
                    to_merge.append(merged)
        for r in to_remove:
            sides.remove(r)
        for m in to_merge:
            sides.append(m)
    


def adjacent(grid: list[list[str]], p: tuple[int]) -> list[tuple[int, int, str]]:
    res = []
    directions = [(1, 0, 'r'), (0, 1, 'd'), (-1, 0, 'l'), (0, -1, 'u')]
    for d in directions:
        if p[1]+d[1] < len(grid) and p[1]+d[1] >= 0 and p[0] + d[0] < len(grid[p[1]+d[1]]) and p[0] + d[0] >= 0 and grid[p[1]][p[0]] == grid[p[1]+d[1]][p[0]+d[0]]:
            res.append((p[0]+d[0], p[1]+d[1], d[2]))
    return res

sides = []
visited = []
def DFS(grid: list[list[str]], p: tuple[int, int, tuple[bool] | None]) -> int:
    area = 1
    adj = adjacent(grid, (p[0], p[1]))
    fence_up = True
    fence_down = True
    fence_left = True
    fence_right = True
    for v in [i[2] for i in adj]:
        match v:
            case 'u':
                fence_up = False
            case 'd':
                fence_down = False
            case 'l':
                fence_left = False
            case 'r':
                fence_right = False

    # Try not to look at this too hard
    global sides
    for side in sides:
        if side[0] == 'u' and fence_up and side[1] == p[1] and (side[2][0]-1 == p[0] or side[2][1]+1 == p[0]):
            sides[sides.index(side)] = [side[0], side[1], (p[0], side[2][1]) if side[2][0]-1 == p[0] else (side[2][0], p[0])]
            fence_up = False
        elif side[0] == 'd' and fence_down and side[1] == p[1] and (side[2][0]-1 == p[0]-1 or side[2][1]+1 == p[0]):
            sides[sides.index(side)] = [side[0], side[1], (p[0], side[2][1]) if side[2][0]-1 == p[0] else (side[2][0], p[0])]
            fence_down = False
        elif side[0] == 'l' and fence_left and side[1] == p[0] and (side[2][0]-1 == p[1]-1 or side[2][1]+1 == p[1]):
            sides[sides.index(side)] = [side[0], side[1], (p[0], side[2][1]) if side[2][0]-1 == p[1] else (side[2][0], p[1])]
            fence_left = False
        elif side[0] == 'r' and fence_right and side[1] == p[0] and (side[2][0]-1 == p[1]-1 or side[2][1]+1 == p[1]):
            sides[sides.index(side)] = [side[0], side[1], (p[0], side[2][1]) if side[2][0]-1 == p[1] else (side[2][0], p[1])]
            fence_right = False
    
    if fence_up:
        sides.append(['u', p[1], (p[0], p[0])])
    if fence_down:
        sides.append(['d', p[1], (p[0], p[0])])
    if fence_left:
        sides.append(['l', p[0], (p[1], p[1])])
    if fence_right:
        sides.append(['r', p[0], (p[1], p[1])])

    global visited
    for v in adj:
        if not (v[0], v[1]) in visited:
            visited.append((v[0], v[1]))
            res = DFS(grid, (v[0], v[1]))
            area += res
    return area

def main():
    with open("input.txt", "r") as f:
        grid = [list(line) for line in list(map(str.strip, f.readlines()))]

        total = 0
        for j in range(0, len(grid)):
            for i in range(0, len(grid[j])):
                global visited
                global sides
                if not (i, j) in visited:
                    visited.append((i, j))
                    sides = []
                    res = DFS(grid, (i, j))
                    merge()
                    total += res * len(sides)

        print(total)

if __name__ == "__main__":
    main()