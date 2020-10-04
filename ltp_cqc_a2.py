# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.

    def __init__(self, symbol, row, col):
        """(Rat, str, int, int) -> NoneType

        A rat with a symbol representing the rat and its current row & column position.

        >>> emily = Rat('E', 1, 1)
        >>> emily.symbol
        E
        >>> emily.row
        1
        >>> emily.col
        1

        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def set_location(self, new_row, new_col):
        """(Rat, int, int) -> NoneType

        Change a rat's location to a defined row and column.

        >>> emily = Rat('E',1,1)
        >>> emily.set_location(2,2)
        >>> emily.row
        2
        >>> emily.col
        2
        """

        self.row = new_row
        self.col = new_col
    
        
    def eat_sprout(self):
        """(Rat) -> NoneType

        Add one to the rats value of num_sprouts_eaten.

        >>> emily = Rat('E', 1, 1)
        >>> emily.eat_sprout()
        >>> emily.num_sprouts_eaten
        >>> 1
        """
        
        self.num_sprouts_eaten = self.num_sprouts_eaten + 1

    def __str__(self):
        """(Rat) -> str

        Return a string representation of the Rat.

        >>> emily = Rat('E',1,2)
        >>> print(emily)
        E at (1, 2) ate 0 sprouts.

        """
        text = "{0} at ({1}, {2}) ate {3} sprouts."
        return text.format(self.symbol, self.row,self.col, self.num_sprouts_eaten)

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.
    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType

        A Maze with a maze representing the contents of the maze, and two rats in the maze.

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
           ['#', '.', '.', '.', '.', '.', '#'], 
           ['#', '.', '#', '#', '#', '.', '#'], 
           ['#', '.', '.', '@', '#', '.', '#'], 
           ['#', '@', '#', '.', '@', '.', '#'], 
           ['#', '#', '#', '#', '#', '#', '#']], 
           Rat('J', 1, 1),
           Rat('P', 1, 4))
        >>> maze_1.maze
        [['#', '#', '#', '#', '#', '#', '#'], 
        ['#', '.', '.', '.', '.', '.', '#'], 
        ['#', '.', '#', '#', '#', '.', '#'], 
        ['#', '.', '.', '@', '#', '.', '#'], 
        ['#', '@', '#', '.', '@', '.', '#'], 
        ['#', '#', '#', '#', '#', '#', '#']]
        >>> maze_1.rat_1
        J at (1,1) ate 0 sprouts.
        >>> maze_1.rat_2
        P at (1,4) ate 0 sprouts.

        """
        
        Maze.maze = maze
        Maze.rat_1 = rat_1
        Maze.rat_2 = rat_2
        count_sprouts = 0
        for i in range(len(Maze.maze)):
            for j in range(len(Maze.maze[i])):
                if Maze.maze[i][j] == SPROUT:
                    count_sprouts = count_sprouts + 1
                
        Maze.num_sprouts_left = count_sprouts

        if Maze.maze[rat_1.row][rat_1.col] == HALL:
            Maze.maze[rat_1.row][rat_1.col] = rat_1.symbol
        if Maze.maze[rat_2.row][rat_2.col] == HALL:
            Maze.maze[rat_2.row][rat_2.col] = rat_2.symbol

    def is_wall(self, row, col):
        """(Maze, int, int) -> bool

        Return True if and only if there is a wall at the given row and column of the maze.

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
           ['#', '.', '.', '.', '.', '.', '#'], 
           ['#', '.', '#', '#', '#', '.', '#'], 
           ['#', '.', '.', '@', '#', '.', '#'], 
           ['#', '@', '#', '.', '@', '.', '#'], 
           ['#', '#', '#', '#', '#', '#', '#']], 
           Rat('J', 1, 1),
           Rat('P', 1, 4))
        >>> maze_1.is_wall(2, 2)
        True
        >>> maze_1.is_wall(1,1)
        False
        """

        return Maze.maze[row][col] == WALL

    def get_character(self, row, col):
        """(Maze, int, int) -> str

        Return the character in the maze at the given row and column

        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
           ['#', '.', '.', '.', '.', '.', '#'], 
           ['#', '.', '#', '#', '#', '.', '#'], 
           ['#', 'P', '.', '@', '#', '.', '#'], 
           ['#', '@', '#', '.', '@', '.', '#'], 
           ['#', '#', '#', '#', '#', '#', '#']], 
           Rat('J', 1, 1),
           Rat('P', 1, 4))
        >>> maze_1.get_character(2,2)
        #
        >>> maze_1.get_character(1,1)
        .
        >>> maze_1.get_character(3,1)
        P
        """

        return Maze.maze[row][col]

    def move(self, rat, dir_1, dir_2):
        """(Maze, Rat, int, int) -> bool

        Move rat_1 to a new location based on dir_1 and dir_2. Do not move if new location is a wall.
        Eat sprout if new location is a sprout. Return true if new location is not a wall.
        
        >>> maze_1 = Maze([['#', '#', '#', '#', '#', '#', '#'], 
           ['#', '.', '.', '.', '.', '.', '#'], 
           ['#', '.', '#', '#', '#', '.', '#'], 
           ['#', 'P', '.', '@', '#', '.', '#'], 
           ['#', '@', '#', '.', '@', '.', '#'], 
           ['#', '#', '#', '#', '#', '#', '#']], 
           Rat('J', 1, 1),
           Rat('P', 1, 4))
        >>> Maze.move(rat_2, UP, NO_CHANGE)
        True
        >>> rat_2.num_sprouts_eaten
        1
        """

        current_row = rat.row
        current_col = rat.col

        new_row = current_row + dir_1
        new_col = current_col + dir_2

        if Maze.maze[new_row][new_col] == WALL:
            return False
        elif Maze.maze[new_row][new_col] == SPROUT:
            rat.eat_sprout()
            Maze.num_sprouts_left = Maze.num_sprouts_left - 1
        Maze.maze[new_row][new_col] = rat.symbol
        rat.set_location(new_row, new_col)
        if Maze.rat_1.row == current_row and Maze.rat_1.col == current_col:
            Maze.maze[current_row][current_col] = Maze.rat_1.symbol
        elif Maze.rat_2.row == current_row and Maze.rat_2.col == current_col:
            Maze.maze[current_row][current_col] = Maze.rat_2.symbol
        else:
            Maze.maze[current_row][current_col] = HALL
        return True

    def __str__(self):
        """(Maze) -> str

        Format Maze like a string.
        """

        text = ''
        for i in range(len(Maze.maze)):
            if i == len(Maze.maze) - 1:
                text = text + str(Maze.maze[i])
            else: text = text + str(Maze.maze[i]) + '\n'
        text = text + "\n" + str(Maze.rat_1)
        text = text + "\n" + str(Maze.rat_2)
        return text
                    
                    
                    
    
    
        
      
        

