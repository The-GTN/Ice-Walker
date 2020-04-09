from cell import *
from player import *
from game import *

class Grid():
    """
    >>> grid = Grid.from_file("grid01.txt")
    >>> grid.get_width()
    16
    >>> grid.get_height()
    16
    >>> grid.get_grid()
    [[1   ,     ,     ,  |  ,     ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,     ], [    ,     ,     ,     ,     ,     ,     ,     ,     ,     ,     ,     ,     ,  |-+,     ,   - ], [    , 2   ,     ,     ,     ,  |-+,     ,     ,     ,   - ,     ,     ,     ,     ,     ,     ], [    ,     ,   - ,     ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,   - ,     ], [  - ,     ,  |  ,     ,     ,     ,     , 3   ,     ,     ,     ,     ,     ,     ,  |  ,     ], [    ,   - ,     ,     ,     ,     ,  |  ,   - ,     ,     ,     ,     , 0   ,     ,     ,     ], [ |  ,     ,     ,     ,     ,     ,     ,   - ,   - ,     ,     ,  |  ,   - ,     ,     ,     ], [    ,     ,     ,     ,     ,     ,  |  ,     ,  |  ,     ,     ,     ,     ,     ,     ,     ], [    ,     ,     ,     ,     ,     ,  |  ,   - ,  |-+,     ,     ,     ,     ,     ,     ,     ], [    ,     ,     ,  |  ,   - ,     ,   - ,     ,     ,     ,     ,     ,  |  ,   - ,     ,     ], [  - ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,     ,     ,     ,     ,     ], [    ,     ,     ,     ,     ,     ,     ,   - ,     ,  |-+,     ,     ,     ,     ,     ,   - ], [    ,   - ,     ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,     ,   - ,     ], [    ,  |  ,     ,     ,     ,     ,     ,     ,     ,     ,   - ,     ,     ,     ,  |  ,     ], [    ,     ,     ,  |-+,     ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,     ], [    ,     ,     ,     ,  |  ,     ,     ,     ,     ,     ,     ,  |  ,     ,     ,     ,     ]]
    >>> grid.get_nb_players()
    4
    >>> grid.inc_nb_players()
    >>> grid.get_nb_players()
    5
    >>> grid.dec_nb_players()
    >>> grid.get_nb_players()
    4
    >>> grid.get_players()
    [Player 0 at coordinate (12,5), Player 1 at coordinate (0,0), Player 2 at coordinate (1,2), Player 3 at coordinate (7,4)]
    >>> grid.get_player(0)
    Player 0 at coordinate (12,5)
    >>> grid.get_walls()
    [(3, 0, 'E'), (9, 0, 'E'), (13, 1, 'E'), (13, 1, 'S'), (15, 1, 'S'), (5, 2, 'E'), (5, 2, 'S'), (9, 2, 'S'), (2, 3, 'S'), (8, 3, 'E'), (14, 3, 'S'), (0, 4, 'S'), (2, 4, 'E'), (14, 4, 'E'), (1, 5, 'S'), (6, 5, 'E'), (7, 5, 'S'), (0, 6, 'E'), (7, 6, 'S'), (8, 6, 'S'), (11, 6, 'E'), (12, 6, 'S'), (6, 7, 'E'), (8, 7, 'E'), (6, 8, 'E'), (7, 8, 'S'), (8, 8, 'S'), (8, 8, 'E'), (3, 9, 'E'), (4, 9, 'S'), (6, 9, 'S'), (12, 9, 'E'), (13, 9, 'S'), (0, 10, 'S'), (5, 10, 'E'), (7, 11, 'S'), (9, 11, 'S'), (9, 11, 'E'), (15, 11, 'S'), (1, 12, 'S'), (7, 12, 'E'), (14, 12, 'S'), (1, 13, 'E'), (10, 13, 'S'), (14, 13, 'E'), (3, 14, 'E'), (3, 14, 'S'), (9, 14, 'E'), (4, 15, 'E'), (11, 15, 'E')]
    >>> grid.get_final()
    (3, 14)
    >>> grid.state()
    False
    >>> grid.change_state()
    >>> grid.state()
    True
    >>> grid.get_cell(12,5)
    0
    >>> grid.change_state()
    >>> grid
    Ice Walker Unfinished with 4 players
    >>> print(grid)
    "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
     |1      |           |           |
     +                               +
     |                           |   |
     +                          -+  -+
     |  2        |                   |
     +          -+     +-            +
     |                 |             |
     +    -+                      -+ +
     |     |        3              | |
     +-                              +
     |             |          0      |
     + +-          +-                +
     | |                     |       |
     +             +-+-+     +-      +
     |             |   |             |
     +             +   +             +
     |             |   |             |
     +             +-+-+             +
     |       |                 |     |
     +       +-  +-            +-    +
     |           |                   |
     +-                              +
     |                   |           |
     +              -+  -+          -+
     |               |               |
     +  -+                        -+ +
     |   |                         | |
     +                   +-          +
     |      X|           |           |
     +      -+                       +
     |         |             |       |
     +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"

    """


    def __init__(self):
        """
        Create a grid
        :return: a new grid
        :rtype: Grid
        :UC: None
        :Example:

        >>> grid = Grid()
        >>> grid.get_width()
        0
        >>> grid.get_height()
        0
        >>> grid.get_grid()
        []
        >>> grid.get_nb_players()
        0
        >>> grid.get_players()
        [None]
        >>> grid.get_walls()
        []
        >>> grid.get_final()
        (None,None)
        >>> grid.state()
        False
        """
        self.__width= 0
        self.__height= 0
        self.__grid = list()
        self.__nb_players = 0
        self.__main_play = None
        self.__other_play = list()
        self.__walls = list()
        self.__final = (None,None)
        self.__is_win = False
        self.__name = ""


    def get_name(self):
        """
        :return: name of the grid
        :rtype: str
        :UC: none
        """
        return self.__name

    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
        """
        return self.__width

    def __set_width(self,width):
        """
        :param width: the width of the grid
        :type width: int
        :return: none
        :side effect: assign the width value of the grid
        :UC: width >= 0
        """
        assert type(width) == int, "width is an integer"
        assert width >= 0, "No negative width !"
        self.__width = width


    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.__height

    def __set_height(self,height):
        """
        :param height: the height of the grid
        :type height: int
        :return: none
        :side effect: assign the height value of the grid
        :UC: height >= 0
        """
        assert type(height) == int, "height is an integer"
        assert height >= 0, "No negative height !"
        self.__height = height


    def get_grid(self):
        """
        :return: the grid
        :rtype: list
        :UC: none
        """
        return self.__grid

    def __set_grid(self,grid):
        """
        :param grid: the grid
        :type grid: list
        :return: None
        :side effect: affect the grid value to the grid
        :UC: None
        """
        assert type(grid) == list, "grid is a list"
        self.__grid = grid

    def get_nb_players(self):
        """
        :return: number of players in the grid
        :rtype: int
        :UC: none
        """
        return self.__nb_players

    def get_players(self):
        """
        :return: the list of the players
        :rtype: list
        :UC: none
        """
        return [self.__main_play]+ self.__other_play
        

    def get_player(self,num):
        """
        :param num: the number relative to the player we want to get
        :type num: int
        :return: the player relative to the number num or Nothing if there no player relative to the number num
        :rtype: Player or None
        :UC: 0<=num<=self.get_nb_players()
        """
        assert type(num) == int, "num of player is an integer"
        assert 0 <= num <= self.get_nb_players()-1, "your player has to exist !"
        player = None
        for player in self.get_players():
            if player.get_num() == num:
                return player

    def get_player_by_coordinate(self,x,y):
        """
        :param x: coordinate x of the possible player
        :type x: int
        :param y: coordinate y of the possible player
        :type y: int
        :return: the player at the cell (x,y), if there a player in this cell
        :rtype: Player or None
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        assert type(x) == type(y) == int, "Coordinates are integers"
        assert 0 <= x < self.get_width(), "Select a correct line !"
        assert 0 <= y < self.get_height(), "Select a correct column !"
        return self.get_cell(x,y).get_player()

    def get_walls(self):
        """
        :return: the list of the walls
        :rtype: list
        :UC: none
        """
        return self.__walls

    def get_final(self):
        """
        :return: the coordinate of the final cell
        :rtype: tuple
        :UC: none
        """
        return self.__final

    def __set_final(self,final):
        """
        :param final: coordinate of the final cell
        :type final: tuple
        :side effect: affect the coordinate of the final cell
        :UC: final[0] >= 0 and final[1] >=0 and final[0] <= self.get_width()-1 and final[1] <= self.get_height()-1
        """
        assert type(final) == tuple, "coordinate is a tuple"
        assert len(final) == 2, "Two coordinates please"
        assert all([type(elem)==int for elem in final])
        assert final[0] >= 0 and final[1] >=0, "No negative coordinate !"
        assert final[0] <= self.get_width()-1 and final[1] <= self.get_height()-1, "No coordinate out of index !"
        self.__final = final

    def state(self):
        """
        :return: True if the game is won, False otherwise
        :rtype: bool
        :UC: none
        """
        return self.__is_win

    def change_state(self):
        """
        :return: None
        :side effect: change the winning state of the grid
        :UC: None
        """
        self.__is_win = not(self.__is_win)

    def get_cell(self,x,y):
        """
        :param x: the x coordinate of the cell to get
        :type x: int
        :param y: the y coordinate of the cell to get
        :type y: int
        :return: the cell of coordinate (x,y)
        :rtype: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        assert type(x) == type(y) == int, "Coordinates are integers"
        assert 0 <= x < self.get_width(), "Select a correct line !"
        assert 0 <= y < self.get_height(), "Select a correct column !"
        return self.__grid[y][x]

    def create_grid(self):
        """
        :return: None
        :side effect: create a new grid according the grid variables
        :UC: None
        """
        #initialisation des cases
        l = list()
        for ligne in range(self.get_height()):
            l.append([Cell() for col in range(self.get_width())])
        #insertion des joueurs
        for player in self.get_players():
            l[player.get_y()][player.get_x()].give_player(player)
        #pose des murs
        for wall in self.get_walls():
            if wall[2] == 'E':
                l[wall[1]][wall[0]].set_east_wall()
            else:
                l[wall[1]][wall[0]].set_south_wall()
        self.__set_grid(l)

    def __repr__(self):
        """
        :return: the grid representation
        :rtype: Grid
        :UC: None
        :Example:
        >>> grid = Grid.from_file("grid01.txt")
        >>> grid
        'Ice Walker Unfinished with 4 players'
        """
        if self.state():
            return "Ice Walker Finished"
        else:
            players = self.get_nb_players()
            if players > 1:
                return "Ice Walker Unfinished with {0} players".format(players)
            else:
                return "Ice Walker Unfinished with {0} player".format(players)

    def __str__(self):
        """
        :return: a string representation of the grid
        :rtype: str
        :UC: None
        :Example:

        >>> grid = Grid.from_file("grid01.txt")
        >>> str(grid)
        '+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
         |1      |           |           |
         +                               +
         |                           |   |
         +                          -+  -+
         |  2        |                   |
         +          -+     +-            +
         |                 |             |
         +    -+                      -+ +
         |     |        3              | |
         +-                              +
         |             |          0      |
         + +-          +-                +
         | |                     |       |
         +             +-+-+     +-      +
         |             |   |             |
         +             +   +             +
         |             |   |             |
         +             +-+-+             +
         |       |                 |     |
         +       +-  +-            +-    +
         |           |                   |
         +-                              +
         |                   |           |
         +              -+  -+          -+
         |               |               |
         +  -+                        -+ +
         |   |                         | |
         +                   +-          +
         |      X|           |           |
         +      -+                       +
         |         |             |       |
         +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+'
        """
        h = self.get_height()
        w = self.get_width()
        final_x,final_y = self.get_final()
        rep_grid = [[' ' for j in range(w*2-1) ] for i in range(h*2-1)]

        for ligne in range(0,h):
            for col in range(0,w):
                cell = self.get_cell(col,ligne)
                if cell.has_player():
                    player = self.get_cell(col,ligne).get_player()
                    rep_grid[ligne*2][col*2] = str(player)
                elif ligne == final_y and col == final_x:
                    rep_grid[ligne*2][col*2] = 'X'
                    cell.set_win()

                if cell.has_south_wall():
                    rep_grid[ligne*2+1][col*2] = '-'

                if cell.has_east_wall():
                    rep_grid[ligne*2][(col*2 +1)] = '|'

                if cell.has_south_wall() and cell.has_east_wall():
                    rep_grid[ligne*2+1][col*2+1] = '+'

                if ligne != 0:
                    cell_above = self.get_cell(col,ligne-1)
                    if cell.has_east_wall() and (cell_above.has_south_wall() or cell_above.has_east_wall()):
                        rep_grid[ligne*2-1][col*2+1] = '+'

                if ligne != h-1:
                    cell_below = self.get_cell(col,ligne+1)
                    if cell.has_south_wall() and cell_below.has_east_wall():
                        rep_grid[ligne*2+1][col*2+1] = '+'

                if col != 0:
                    cell_left = self.get_cell(col-1,ligne)
                    if cell.has_south_wall() and (cell_left.has_south_wall() or cell_left.has_east_wall()):
                        rep_grid[ligne*2+1][col*2-1] = '+'

                if col != w-1:
                    cell_right = self.get_cell(col+1,ligne)
                    if cell_right.has_south_wall() and (cell.has_south_wall() or cell.has_east_wall()):
                        rep_grid[ligne*2+1][col*2+1] = '+'

                if ligne != 0 and col != 0:
                    cell_above = self.get_cell(col,ligne-1)
                    cell_left = self.get_cell(col-1,ligne)
                    if cell_above.has_south_wall() and cell_left.has_east_wall():
                        rep_grid[ligne*2-1][col*2-1] = '+'


        string = '+-'*w + '+\n'
        for i in range(len(rep_grid)):
            if i%2 == 0:
                string += '|'
            else:
                string += '+'
            for j in range(len(rep_grid[0])):
                string += str(rep_grid[i][j])

            if i%2 == 0 :
                string += '|'
            else:
                string += '+'
            string += '\n'
        return string+'+-'*w + '+'


    def from_file(file):
        """
        :param file: the file which we get the grid informations
        :type file: file
        :return: none
        :side effect: affect the grid variables from a file
        :UC: the file respect the subject form
        """
        grid = Grid()
        Player.reset_compt()
        content = list()
        with open(file,"r") as output:
            brut = output.readlines()                      # On suppose que les fichiers sont toujours du même format que grid01.txt
            for line in brut:
                if line[0] != "#":
                    content.append(line.replace("\n",""))
                    
        grid.__name = file

        dimension = content[0].split(",")                 # set des dimensions
        grid.__width = int(dimension[0])
        grid.__height = int(dimension[1])

        coord_final = content[1].split(",")               # Set des coordonées finales
        grid.__final = (int(coord_final[0]),int(coord_final[1]))

        grid.__nb_players = int(content[2])                  # Set du nombre de joueurs

        coord_main = content[3].split(',')                  # Set du joueur principal
        grid.__main_play = Player(int(coord_main[0]),int(coord_main[1]),True)

        for i in range(4,4+grid.__nb_players -1):              # Set les joueurs, les coordonées commencent a partir de la 4e ligne du fichier
            coord_other = content[i].split(",")
            grid.__other_play += [Player(int(coord_other[0]),int(coord_other[1]))]

        for i in range(4+grid.__nb_players-1,len(content)):
            coord_wall = content[i].split(",")
            grid.__walls += [(int(coord_wall[0]),int(coord_wall[1]),coord_wall[2])]

        grid.create_grid()
        return grid