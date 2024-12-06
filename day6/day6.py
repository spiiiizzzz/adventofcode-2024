def guard_start(grid: list[str]) -> tuple[int]:
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[j][i] == "^":
                return (i, j)

def position_valid(grid: list[str], pos: tuple[int]) -> bool:
    if pos[1] >= len(grid) or pos[1] < 0:
        return False
    if pos[0] >= len(grid[pos[1]]) or pos[0] < 0:
        return False
    return True

def position_occupied(grid: list[str], pos: tuple[int]) -> bool:
    if not position_valid(grid, pos):
        return False
    if grid[pos[1]][pos[0]] == "#":
        return True
    else:
        return False

def main():
    with open("input.txt", "r") as f:
        grid = list(map(str.strip, f.readlines()))

        guard_pos = guard_start(grid)
        direction = "up"
        visited = set()

        while position_valid(grid, guard_pos):
            visited.add(guard_pos)
            match direction:
                case "up":
                    if position_occupied(grid, (guard_pos[0], guard_pos[1]-1)):
                        direction = "right"
                    else:
                        guard_pos = (guard_pos[0], guard_pos[1]-1)
                case "down":
                    if position_occupied(grid, (guard_pos[0], guard_pos[1]+1)):
                        direction = "left"
                    else:
                        guard_pos = (guard_pos[0], guard_pos[1]+1)
                case "left":
                    if position_occupied(grid, (guard_pos[0]-1, guard_pos[1])):
                        direction = "up"
                    else:
                        guard_pos = (guard_pos[0]-1, guard_pos[1])
                case "right":
                    if position_occupied(grid, (guard_pos[0]+1, guard_pos[1])):
                        direction = "down"
                    else:
                        guard_pos = (guard_pos[0]+1, guard_pos[1])

        print(len(visited))

if __name__ == "__main__":
    main()