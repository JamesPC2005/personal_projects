# Purpose
This program is designed to take a ascii maze from maze.txt with walls composed of "#" characters and empty spaces made of " ". The program returns the solution.

## For example:
If you give the input of:
```python
    #####I#####
    # #   #   #
    # # # # # #
    #   # # # #
    # ### # # #
    # #     # #
    ### ##### #
    #   #   # #
    # ### # # #
    #   # #   #
    #####O#####
```

The output will be:
```python
    Maze solved!
    #####X#####
    # #  X#XXX#
    # # #X#X#X#
    #   #X#X#X#
    # ###X#X#X#
    # #  XXX#X#
    ### #####X#
    #   #XXX#X#
    # ###X#X#X#
    #   #X#XXX#
    #####O#####
```

# Note:
Maze.txt and the maze_solver must be located in the same directory, and you must be in that directory in order for Maze_Solver to be able to locate maze.txt
