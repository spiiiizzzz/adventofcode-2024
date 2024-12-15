# i predict that the code will be very messy
def get_robot_pos(grid: list[list[str]]) -> tuple[int]:
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[j][i] == '@':
                return (i, j)
    raise ValueError

def move(grid: list[list[str]], coords: tuple[int], direction: str) -> list[list[str]]:
    destination = None
    match direction:
        case "^":
            destination = (coords[0], coords[1]-1)
        case "v":
            destination = (coords[0], coords[1]+1)
        case "<":
            destination = (coords[0]-1, coords[1])
        case ">":
            destination = (coords[0]+1, coords[1])

    if grid[coords[1]][coords[0]] == '#':
        return grid
    if grid[coords[1]][coords[0]] == '@' or grid[coords[1]][coords[0]] == 'O':
        if grid[destination[1]][destination[0]] == '.':
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            return grid
        if grid[destination[1]][destination[0]] == 'O':
            grid = move(grid, destination, direction)
            if grid[destination[1]][destination[0]] == 'O':
                return grid
            else:
                grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
                grid[coords[1]][coords[0]] = '.'
                return grid
        if grid[destination[1]][destination[0]] == '#':
            return grid

def get_objects_score(grid: list[list[str]]) -> int:
    res = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[j][i] == 'O':
                res += j*100 + i
    return res

def main():
    with open("input.txt", "r") as f:
        raw =  f.readlines()
        
        index = raw.index("\n")

        grid = [list(line) for line in raw[:index]]

        sequence = []
        sequence = [list(line.strip()) for line in raw[index+1:]]
        sequence = "".join(sum(sequence, []))

        robot = get_robot_pos(grid)

        for instruction in sequence:
            old_pos = robot
            grid = move(grid, robot, instruction)
            new_pos = get_robot_pos(grid)
            if old_pos != new_pos:
                robot = new_pos

        print(get_objects_score(grid))


if __name__ == "__main__":
    main()