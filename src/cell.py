from player import Player

class Cell():
    """
    >>> cell = Cell()
    >>> cell.has_east_wall()
    False
    >>> cell.set_east_wall()
    >>> cell.has_east_wall()
    True
    >>> cell.has_south_wall()
    False
    >>> cell.set_south_wall()
    >>> cell.has_south_wall()
    True
    >>> cell.has_player()
    False
    >>> cell.give_player(Player(0,0))
    >>> cell.get_player()
    Player 0 at coordinate (0,0)
    >>> cell.is_win()
    False
    >>> cell.set_win()
    >>> cell.is_win()
    True
    """

    def __init__(self):
        """
        Create a new cell
        :return: a new Cell
        :rtype: Cell
        :UC: None
        :Example:

        >>> cell = Cell()
        >>> cell.has_east_wall()
        False
        >>> cell.has_south_wall()
        False
        >>> cell.has_player()
        False
        >>> cell.get_player()
        None
        >>> cell.is_win()
        False
        """
        self.__east_wall = False
        self.__south_wall = False
        self.__has_player = False
        self.__player = None
        self.__win = False

    def __str__(self):
        """
        :return: a string representation of the Cell
        :rtype: str
        :UC: None
        :Example:

        >>> cell = Cell()
        >>> from player import Player
        >>> player = Player(0,0)
        >>> cell.give_player(player)
        >>> cell.set_east_wall()
        >>> cell.set_south_wall()
        >>> str(cell)
        '0|\n-+'
        """
        perso = " "
        east = " "
        south = " "
        plus = " "
        if self.has_player():
            perso = str(self.get_player())
        if self.has_east_wall():
            east = "|"
        if self.has_south_wall():
            south = "-"
        if self.has_east_wall() and self.has_south_wall():
            plus = "+"
        return perso+east+south+plus


    def __repr__(self):
        """
        :return: representation of the Cell
        :rtype: Cell
        :UC: None
        :Example:

        >>> cell = Cell()
        >>> from player import Player
        >>> player = Player(0,0)
        >>> cell.give_player(player)
        >>> cell.set_east_wall()
        >>> cell.set_south_wall()
        >>> cell
        '0|\n-+'
        """
        perso = " "
        east = " "
        south = " "
        plus = " "
        if self.has_player():
            perso = str(self.get_player())
        if self.has_east_wall():
            east = "|"
        if self.has_south_wall():
            south = "-"
        if self.has_east_wall() and self.has_south_wall():
            plus = "+"
        return perso+east+south+plus



    def has_player(self):
        """
        :return: True if there is a player in the cell, False otherwise
        :rtype: bool
        :UC: none
        """
        return self.__has_player

    def has_east_wall(self):
        """
        :return: True if the cell has an east wall, False otherwise
        :rtype: bool
        :UC: none
        """
        return self.__east_wall

    def set_east_wall(self):
        """
        :return: None
        :side effect: set an east wall to the cell
        :UC: None
        """
        self.__east_wall = True

    def set_south_wall(self):
        """
        :return: None
        :side effect: set a south wall to the cell
        :UC: None
        """
        self.__south_wall = True

    def has_south_wall(self):
        """
        :return: True if the cell has a south wall, False otherwise
        :rtype: bool
        :UC: none
        """
        return self.__south_wall

    def give_player(self,player):
        """
        :param player: the player we want to give to the cell
        :type player: Player
        :return: None
        :UC: None
        """
        assert type(player) == Player, "We only give player to a case !"
        self.__has_player = True
        self.__player = player

    def get_player(self):
        """
        :return: the player of the Cell or nothing if the cell is empty
        :rtype: Player
        :UC: None
        """
        return self.__player

    def remove_player(self):
        """
        :return: None
        :side effect: remove the player of the cell
        :UC: None
        """
        self.__has_player = False
        self.__player = None

    def is_win(self):
        """
        :return: True if it's the winning cell, false otherwise
        :rtype: bool
        :UC: None
        """
        return self.__win

    def set_win(self):
        """
        :return: None
        :side effect: make cell become the winning Cell
        :UC: None
        """
        self.__win = True
