def main():
    with open("input.txt", "r") as f:
        grid_size = [101, 103]
        quadrants = [[0, 0], [0, 0]]

        for line in f.readlines():
            pos_str, speed_str = line.strip().split(" ")
            pos = list(map(int, pos_str[2:].split(",")))
            speed = list(map(int, speed_str[2:].split(",")))
            robot  = [[(pos[0]+speed[0]*100)%grid_size[0], (pos[1]+speed[1]*100)%grid_size[1]], speed]
            if robot[0][1] == grid_size[1]//2 or robot[0][0] == grid_size[0]//2:
                continue
            i = 1 if robot[0][1] > grid_size[1]/2 else 0
            j = 1 if robot[0][0] > grid_size[0]/2 else 0
            quadrants[i][j] += 1
        
        print(quadrants[0][0] * quadrants[0][1] * quadrants[1][0] * quadrants[1][1])

if __name__ == "__main__":
    main()