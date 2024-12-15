# this one's way messier

def expand(grid: list[list[str]]) -> list[list[str]]:
    res = []
    for line in grid:
        l = []
        for c in line:
            match c:
                case '@':
                    l.append('@')
                    l.append('.')
                case '.':
                    l.append('.')
                    l.append('.')
                case 'O':
                    l.append('[')
                    l.append(']')
                case '#':
                    l.append('#')
                    l.append('#')
        res.append(l)
    return res

def get_robot_pos(grid: list[list[str]]) -> tuple[int]:
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[j][i] == '@':
                return (i, j)
    raise ValueError

def can_move(grid: list[list[str]], coords: tuple[int], direction: str) -> bool:
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
        return False
    if grid[coords[1]][coords[0]] == '.':
        return True
    if grid[coords[1]][coords[0]] == '[':
        if direction == '^' or direction == 'v':
            i_can_move = can_move(grid, destination, direction)
            grid[coords[1]][coords[0]] = 'W'
            brother_can_move = can_move(grid, (coords[0]+1, coords[1]), direction)
            grid[coords[1]][coords[0]] = '['
            return i_can_move and brother_can_move
        else:
            return can_move(grid, destination, direction)
    if grid[coords[1]][coords[0]] == ']':
        if direction == '^' or direction == 'v':
            i_can_move = can_move(grid, destination, direction)
            grid[coords[1]][coords[0]] = 'W'
            brother_can_move = can_move(grid, (coords[0]-1, coords[1]), direction)
            grid[coords[1]][coords[0]] = ']'
            return i_can_move and brother_can_move
        else:
            return can_move(grid, destination, direction)
    if grid[coords[1]][coords[0]] == 'W':
        return True
    

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

    if grid[coords[1]][coords[0]] == '.':
        return grid
    if grid[coords[1]][coords[0]] == '#':
        return grid
    if grid[coords[1]][coords[0]] == '@':
        if grid[destination[1]][destination[0]] == '.':
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            return grid
        if grid[destination[1]][destination[0]] == '[' or grid[destination[1]][destination[0]] == ']':
            grid = move(grid, destination, direction)
            if grid[destination[1]][destination[0]] != '.':
                return grid
            else:
                grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
                grid[coords[1]][coords[0]] = '.'
                return grid
        if grid[destination[1]][destination[0]] == '#':
            return grid
    if grid[coords[1]][coords[0]] == '[':
        if grid[coords[1]][coords[0]+1] == '.': # brother has already moved
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            return grid
        if can_move(grid, coords, direction):
            grid = move(grid, destination, direction)
            if direction == '^' or direction == 'v':
                grid = move(grid, (destination[0]+1, destination[1]), direction)
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            if direction == '^' or direction == 'v':
                grid[destination[1]][destination[0]+1] = grid[coords[1]][coords[0]+1]
                grid[coords[1]][coords[0]+1] = '.'
            return grid
        else:
            return grid
    if grid[coords[1]][coords[0]] == ']':
        if grid[coords[1]][coords[0]-1] == '.': # brother has already moved
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            return grid
        if can_move(grid, coords, direction):
            grid = move(grid, destination, direction)
            if direction == '^' or direction == 'v':
                grid = move(grid, (destination[0]-1, destination[1]), direction)
            grid[destination[1]][destination[0]] = grid[coords[1]][coords[0]]
            grid[coords[1]][coords[0]] = '.'
            if direction == '^' or direction == 'v':
                grid[destination[1]][destination[0]-1] = grid[coords[1]][coords[0]-1]
                grid[coords[1]][coords[0]-1] = '.'
            return grid
        else:
            return grid
        


def get_objects_score(grid: list[list[str]]) -> int:
    res = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[j])):
            if grid[j][i] == '[':
                res += j*100 + i
    return res

def main():
    with open("input.txt", "r") as f:
        raw =  f.readlines()
        
        index = raw.index("\n")

        grid = [list(line) for line in raw[:index]]
        grid = expand(grid)

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