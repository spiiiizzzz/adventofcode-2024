# first part was actually quite easy
# but i have no idea where to start for part 2
import re

def move_bot(robot: list[list[int]], grid_size: list[int]) -> list[list[int]]:
    return [[(robot[0][0]+robot[1][0])%grid_size[0], (robot[0][1]+robot[1][1])%grid_size[1]], robot[1]]


def condition(grid: list[list[str]]) -> bool:

    ## Tree should look like this
    #....................bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.......................b..........................
    #b...................b.............................b.................................................b
    #..b.................b.............................b......b...........................................
    #....................b.............................b..................................................
    #....................b.............................b..........................................b.......
    #................b...b..............b..............b..................................................
    #.b..................b.............bbb.............b..................................................
    #....................b............bbbbb............b........................................b.........
    #.......b............b...........bbbbbbb...........b..................................................
    #....................b..........bbbbbbbbb..........b....b....................................b........
    #....................b............bbbbb............b..................................................
    #......b........b....b...........bbbbbbb...........b..................................................
    #....................b..........bbbbbbbbb..........b.............................b....................
    #....................b.........bbbbbbbbbbb.........b..........................................b.......
    #....................b........bbbbbbbbbbbbb........b..................................................
    #..................b.b..........bbbbbbbbb..........b..................................................
    #....................b.........bbbbbbbbbbb.........b.....b.......................................b....
    #....................b........bbbbbbbbbbbbb........b..................................b...............
    #....................b.......bbbbbbbbbbbbbbb.......b..................................................
    #....................b......bbbbbbbbbbbbbbbbb......b..................................................
    #....................b........bbbbbbbbbbbbb........b..................................................
    #....................b.......bbbbbbbbbbbbbbb.......b..................................................
    #.................b..b......bbbbbbbbbbbbbbbbb......b..................................................
    #....................b.....bbbbbbbbbbbbbbbbbbb.....b..................................................
    #..........b.........b....bbbbbbbbbbbbbbbbbbbbb....b.........................................b........
    #................b...b.............bbb.............b...........................b.................b....
    #....................b.............bbb.............b..........b.......................................
    #....................b.............bbb.............b......b...........................................
    #....................b.............................b............................................b.....
    #....................b.............................b..................................................
    #....................b.............................b..................................................
    #....................b.............................b.............................b....................
    #....................bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb.........b.................b......................

    for row in grid:
        if re.search('b....bbbbbbbbbbbbbbbbbbbbb....b', "".join(row)) != None:
            return True
    return False


def main():
    with open("input.txt", "r") as f:
        grid_size = [101, 103]
        quadrants = [[0, 0], [0, 0]]

        robots = []
        for line in f.readlines():
            pos_str, speed_str = line.strip().split(" ")
            pos = list(map(int, pos_str[2:].split(",")))
            speed = list(map(int, speed_str[2:].split(",")))

            robots.append([pos,speed])
        
        # testing to actually see this christmas tree
        counter = 0
        i = ''
        while True:
            counter += 1
            if i == 'q':
                break

            grid = []
            for _ in range(0, grid_size[1]):
                grid.append([])

            for y in range(0, grid_size[1]):
                for _ in range(0, grid_size[0]):
                    grid[y].append('.')

            for i in range(0, len(robots)):
                robots[i] = move_bot(robots[i], grid_size)
                grid[robots[i][0][1]][robots[i][0][0]] = 'b'

            if condition(grid):
                for row in grid:
                    print("".join(row))
                print(counter)
                i = input()


if __name__ == "__main__":
    main()