import matplotlib.pyplot as plt
import numpy as np
from plot_data import plot_data


# Control the settings of the DFS algorithm:
# Load comma-separated .txt file with values 0 (wall), 1 (Empty), 2 (start), or 3(Goal)
filename = 'maze3.txt'  # maze1: tree, maze2: lattice, maze3: empty maze
visual_delay = 0.1      # Visualisation delay in seconds (must be positive)
if visual_delay <= 0:
    raise Exception("Visualisation delay must be positive")


# New exception type to break from loop
class Found(Exception):
    pass


# The Node of every Tree element
class Node:
    def __init__(self, loc: list[2], parent: int):
        self.location = loc
        self.parent = parent


def check(loc, limits):
    """
    Returns True if a certain location should be searched:
    1) belongs in the maze
    2) it is of importance (Goal or Empty Node)
    otherwise return False
    :param loc: the location checked on the maze
    :param limits: the size of the maze
    :return: True if the Node should be searched, else False
    """
    if (loc >= 0).all() and (loc < limits).all():
        if (maze[loc[0], loc[1]] == np.array([3, 1])).any():
            return True
    return False


def search(loc, par):
    """
    Searches the Node after it has been checked successfully.
    Creates the Node in the Tree list.
    The Node can only be Empty or the Goal because it has been checked.
    Changes its state to Searched if its Empty and updates the map afterwards
    :param loc: the location of the Node searched
    :param par: the parent of this Node
    :return: True if it is the Goal, otherwise False
    """
    Tree.append(Node(loc, par))
    if maze[loc[0], loc[1]] == 3:
        return True
    else:
        maze[loc[0], loc[1]] = 4
        plot_data(maze, visual_delay)
        return False


# Load the maze
maze = np.loadtxt(filename, delimiter=',')
maze_size = list(maze.shape)
# Initialize the Tree and find the first Node
Tree = []
start = np.where(maze == 2)
start = [start[0][0], start[1][0]]
Tree.append(Node(start, None))
# Initialize variables needed for the loop
pointer = 0
i = 0
movement = np.array([[-1, 0], [0, -1], [1, 0], [0, 1]])

try:
    # Infinite loop of searching
    while True:
        # Circle through all nearby Nodes in maze
        while i < len(movement):
            # Check if Node is important
            if check(Tree[pointer].location + movement[i], maze_size):
                # Create and Search important Node
                if search(Tree[pointer].location + movement[i], pointer):
                    # This Node is the Goal, exit the infinite loop
                    path = list(Tree[pointer].location + movement[i])
                    raise Found
                else:
                    # This Node is not the Goal,
                    # start from this Node next loop(DFS)
                    i = 0
                    pointer = len(Tree) - 1
                    continue
            i += 1
        # Found a dead end, backtrack
        pointer = Tree[pointer].parent
        i = 0
        # A message in case there are no more Nodes to be searched
        if pointer is None:
            print("Cannot find the Goal :(")
            break
except Found:
    print("Found the Goal")

# Backtrack using the parent variable
# and save the path in a list
while Tree[pointer].parent is not None:
    locat = Tree[pointer].location
    path.append([locat[0], locat[1]])
    maze[locat[0], locat[1]] = 5
    plot_data(maze, visual_delay)
    pointer = Tree[pointer].parent
plt.show()
