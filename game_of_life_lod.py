import time
import os
import random
import platform

"""
NOT COMPLETE!

An introduction to python using the game of life as a problem to solve in class.
Not the most pythonic or succinct solution, but it's not meant to be.

Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by over-population.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""


class GolBoard(object):
    def __init__(self, rows=20, cols=20, populate=False, density=.25, generation=0, seed=None):
        random.seed(seed)
        self.generation = generation
        self.genMap = {}
        self.edge = []
        self.width = cols
        self.height = rows

        if populate:
            self.currentGen = self.init_randgen(density)
        else:
            self.currentGen = self.init_gen()

    def __str__(self):
        return "width:%d height:%d" % (self.width, self.height)

    """
    @function: makeAlive
    @description: Adds a life to specified location
    @param: int x - Column to add life
    @param: int y - Row to add life
    @returns: None
    """

    def make_alive(self, row, col):
        self.currentGen[col - 1][row - 1] = True

    """
    @function: hexafy
    @description: Computes hex value of a board
    @param: none
    @returns: hexvalue
    """

    def hexafy(self, hexme):
        string = ""
        for row in range(self.height):
            for col in range(self.width):
                if hexme[row][col]:
                    string += '1'
                else:
                    string += '0'
        return hex(int(string, 2))

    """
    @function: computeNextGen
    @description: Computes the next generation our cellular automata
    @param: None
    @returns: None
    """

    def compute_nextgen(self):
        nextgen = self.init_gen()
        nextedge = []
        self.edge = []
        for row in range(self.height):
            for col in range(self.width):
                nextgen[row][col] = self.liv_or_die(row, col)

        hexnextgen = self.hexafy(nextgen)
        hexcurrent = self.hexafy(self.currentGen)

        nextedge.append(hexnextgen)
        nextedge.append(hexcurrent)

        if hexnextgen in self.genMap:
            if self.genMap[hexnextgen] == nextedge:
                self.generation += 1
        self.edge.append(hexcurrent)
        self.edge.append(hexnextgen)
        self.genMap = {hexcurrent: self.edge}

        self.currentGen = nextgen

    """
    @function: liveOrDie
    @description: Calculates whether a cell lives or dies based on Game of Life rules
    @param: int x - Column to check
    @param: int y - Row to check
    @returns: Int : 0 = nothing changes , -1 = dies , 1 = birth
    """

    def liv_or_die(self, r, c):
        neighbors = []
        alive = self.currentGen[r][c]

        # using % we can wrap the edges of the table. example assume a 5 x 5 table -1 % 5 is 4 0 % 5 is 0 and
        # 5 % 5 is 0 with this there is no need for complex if else chains to find an edge.

        neighbors.append(self.currentGen[(r - 1) % self.height][(c - 1) % self.width])  # upper left
        neighbors.append(self.currentGen[r][(c - 1) % self.width])  # upper middle
        neighbors.append(self.currentGen[(r + 1) % self.height][(c - 1) % self.width])  # upper right
        neighbors.append(self.currentGen[(r + 1) % self.height][c])  # right
        neighbors.append(self.currentGen[(r - 1) % self.height][c])  # left
        neighbors.append(self.currentGen[(r - 1) % self.height][(c + 1) % self.width])  # bottom left
        neighbors.append(self.currentGen[r][(c + 1) % self.width])  # bottom middle
        neighbors.append(self.currentGen[(r + 1) % self.height][(c + 1) % self.width])  # bottom right

        count = neighbors.count(True)

        if alive:
            if count == 2 or count == 3:
                return True
            else:
                return False
        else:
            if count == 3:
                return True
            else:
                return False

    """
    @function: initGen
    @description: Initializes a single generation
    @param: None
    @returns: list - 2D list containing False
    """

    def init_gen(self):
        # return [[False] * self.width for row in range(self.height)]
        # board = [i for i in range(self.height)]
        # for i in range(self.height):
        #    board[i] = [False for j in range(self.width)]
        #    print board[i][j]
        board = [[False for i in range(self.width)] for j in range(self.height)]
        return board

    """
    @function: initRandGen
    @description: Initializes a random generation
    @param: float - density (how many lives to create)
    @returns: list - 2D list containing False and True
    """

    def init_randgen(self, density):
        gen = self.init_gen()

        numberoflives = int(self.width * self.height * density)

        for i in range(numberoflives):
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            gen[row][col] = self.random_life()  # ??
        return gen

    """
    @function: randomLife
    @description: Generates a random life (zero or one)
    @param: none
    @returns: bool - zero or one (alive or dead)
    """

    def random_life(self):
        if random.random() > .5:
            return True
        else:
            return False

    """
    @function: stringifyWorld
    @description: Creates a string version of the 2D list representing our world
    @param: none
    @returns: string - a string version
    """

    def stringify_world(self):
        string = "\n\n"
        for row in self.currentGen:
            for cell in row:
                if not cell:
                    string += ' .'
                else:
                    string += ' O'
            string += "\n"
        return string

    def print_debug(self):
        for row in self.currentGen:
            print(row)
    """
    @function: playgame
    @description: runs a game of life
    @param: None
    @returns: None
    """
    def play_game(self):
            while self.generation < 3:
                self.compute_nextgen()
                clear_screen()
                print(self.stringify_world())
                time.sleep(sleep)

"""
@function: clearScreen
@description: Clears the terminal screen
@param: None
@returns: None
"""


def clear_screen():
    if platform.system() == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')


def print_list(mylist):
    string = ""
    for rows in range(len(mylist)):
        for cols in range(len(mylist)):
            string += "%d " % (mylist[rows][cols])
        string += "\n"
    print(string)

if __name__ == '__main__':
    rows = 20
    cols = 30
    density = .25
    sleep = .2
    clear_screen()
    b = GolBoard(rows, cols, True, density, 0, 42)
    b.play_game()
