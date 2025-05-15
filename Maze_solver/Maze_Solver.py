def move(y_pos: int, x_pos: int, maze: list[list[str]]) -> bool:
    
    if maze[y_pos+1][x_pos] == 'O':
        maze[y_pos][x_pos] = 'X'
        return True  # exit found

    maze[y_pos][x_pos] = 'X'

    # check down
    if y_pos < len(maze) - 1 and maze[y_pos + 1][x_pos] == ' ':
        if move(y_pos + 1, x_pos, maze):
            return True

    # check up
    if y_pos > 0 and maze[y_pos - 1][x_pos] == ' ':
        if move(y_pos - 1, x_pos, maze):
            return True

    # check left
    if x_pos > 0 and maze[y_pos][x_pos - 1] == ' ':
        if move(y_pos, x_pos - 1, maze):
            return True
        
    # check right
    if x_pos < len(maze[0]) - 1 and maze[y_pos][x_pos + 1] == ' ':
        if move(y_pos, x_pos + 1, maze):  
            return True

    
    maze[y_pos][x_pos] = '#'  # mark as dead end

    return False

def main():
    Filename = 'maze.txt'
    try:
        with open(Filename) as f:
            maze = [list(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"File '{Filename}' not found.")
        return

    # find the start
    start_found = False
    for i in range(len(maze[0])):
        if maze[0][i] == 'I':
            x_pos = i
            y_pos = 0
            start_found = True
            break

    if not start_found:
        print("No starting position 'I' found.")
        return

    if move(y_pos, x_pos, maze):  # if exit is found
        print("Maze solved!")
    else:
        print("No solution found.")

    #setup "clean" maze

    with open(Filename) as f:
        maze2 = [list(line.strip()) for line in f]

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'X':
                maze2[i][j] = maze[i][j]

    # print the maze with the path marked
    for row in maze2:
        print("".join(row))

if __name__ == "__main__":
    main()
