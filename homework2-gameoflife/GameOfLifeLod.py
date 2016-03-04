import time
import os
import random
import platform


class GolBoard(object):
    """
    COMPLETE!

    An introduction to python using the game of life as a problem to solve in class.
    Not the most pythonic or succinct solution, but it's not meant to be.

    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by over-population.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    """
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
        """print out width and height.

        prints the values of width and height used for board.

        :return:
            width, height
        """
        return "width:%d height:%d" % (self.width, self.height)

    def make_alive(self, row, col):
        """sets cell to True.

        :description:
                Adds a life to specified location on the board by setting that cell to True.
        :param col:
            Column to add life
        :param row:
            Row to add life
        :returns:
            None
        """
        self.currentGen[col - 1][row - 1] = True

    def hexafy(self, hexme):
        """Computes hex value of string

        :description:
            Takes the binary value of a board computes hex value and creates a single string. Used for faster
            map compares.
        :param:
            none
        :returns:
            hexvalue: a string containing hex values.
        """
        string = ""
        for row in range(self.height):
            for col in range(self.width):
                if hexme[row][col]:
                    string += '1'
                else:
                    string += '0'
        return hex(int(string, 2))

    def compute_nextgen(self):
        """Computes the next generation.

        :description:
            Computes the next generation of board based on liveorDie method. Overwrites the old board with new board.
            Adds new boards to map and checks if they exist or not. Map consists of node and edge. Edge represents the
            future of a board based on the fact that a unique generation can only have one outcome for next generation.

        :param:
            None
        :returns:
            None
        """
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

    def liv_or_die(self, r, c):
        """Calculates whether a cell lives of dies.

        :description:
            Uses % to wrap table edges in the event of search 'falling' off edge. Checks 8 neighbors for values, If cell
            is alive and 2 or 3 neighbors are alive then cell stays alive. If more than 3 neighbors cell dies. If a dead
            cell has exactly 3 neighbors it comes to life.
        :param:
            c - Column to check
        :param:
            r - Row to check
        :returns:
            true or false
        """
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

    def init_gen(self):
        """Creates a game table

        :description:
            Initializes a table with all false values. ie a blank table.
        :param:
            None
        :returns:
            board - 2D list containing False
        """
        # return [[False] * self.width for row in range(self.height)]
        # board = [i for i in range(self.height)]
        # for i in range(self.height):
        #    board[i] = [False for j in range(self.width)]
        #    print board[i][j]
        board = [[False for i in range(self.width)] for j in range(self.height)]
        return board

    def init_randgen(self, density):
        """Creats a game table

        :description:
            Initializes a random generation table. Uses density to approx a spread of random binary values.
        :param:
            density - (how many lives to create)
        :returns:
            gen - 2D list containing False and True
        """
        gen = self.init_gen()

        numberoflives = int(self.width * self.height * density)

        for i in range(numberoflives):
            row = random.randint(0, self.height - 1)
            col = random.randint(0, self.width - 1)
            gen[row][col] = self.random_life()  # ??
        return gen

    def random_life(self):
        """Used by randgen to create random life.

        :description:
            Generates a random life (zero or one) with 50/50 odds
        :param:
            none
        :returns:
            bool - zero or one (alive or dead)
        """
        if random.random() > .5:
            return True
        else:
            return False

    def stringify_world(self):
        """Creates a string version of board

        :description:
            Creates a string version of the 2D list representing our world
        :param:
            none
        :returns:
            string - a string version of board
        """
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
        """debug utility
        """
        for row in self.currentGen:
            print(row)

    def play_game(self):
        """Runs game of life.

        :description:
            Calls next gen with a while loop that is gated by generation. Generation is incremented by nextgen when
            compairing the generations to a map. Calls stringify_world to print board.
        :param:
            None
        :returns:
            None
        """
        while self.generation < 3:
            self.compute_nextgen()
            clear_screen()
            print(self.stringify_world())
            time.sleep(sleep)

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
    rows = 40
    cols = 80
    density = .25
    sleep = .2
    seed = None
    clear_screen()
    b = GolBoard(rows, cols, True, density, 0, seed)
    b.play_game()
