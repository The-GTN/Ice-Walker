class Player():
    """
    >>> player = Player(0,2,True)
    >>> player2 = Player(0,3)
    >>> player.is_main()
    True
    >>> player2.is_main()
    False
    >>> player.get_x()
    0
    >>> player.set_x(3)
    >>> player.get_x()
    3
    >>> player.get_y()
    2
    >>> player.set_y(1)
    >>> player.get_y()
    1
    >>> player.get_num()
    0
    >>> str(player)
    '0'
    >>> Player.reset_compt()
    >>> Player(0,0)
    Player 0 at coordinate (0,0)
    >>> player
    Player 0 at coordinate (3,1)
    """
    __compt = -1
    def __init__(self,x,y,main=False):
        """
        Create a Player of number num and of coordinate (x,y)
        :param x: coordinate x of the player
        :type x: int
        :param y: coordinate y of the player
        :type y: int
        :param main: [optional] True if the player is the main player, False otherwise
        :type main: bool
        :return: a new Player of coordinate x,y, of number num, and is the main player if main
        :rtype: Player
        :UC: x >= 0 and y >= 0 and num >= 0
        :Example:

        >>> player = Player(0,2,True)
        >>> player2 = Player(0,3)
        >>> player.is_main()
        True
        >>> player2.is_main()
        False
        >>> player.get_x()
        0
        >>> player.set_x(3)
        >>> player.get_x()
        3
        >>> player.get_y()
        2
        >>> player.set_y(1)
        >>> player.get_y()
        1
        >>> player.get_num()
        0
        >>> str(player)
        '0'
        >>> player
        Player 0 at coordinate (3,1)
        """
        assert type(x) == type(y) == int, "Your coordinates have to be integers !"
        assert type(main) == bool, "Main or not, it's a closed question !"
        assert x >= 0, "No negative x coordinate !"
        assert y >= 0, "No negative y coordinate !"
        Player. __compt += 1
        self.__num = Player.__compt
        self.__x = x
        self.__y = y
        self.__is_main = main

    def __str__(self):
        """
        :return: a string representation of the player
        :rtype: str
        :UC: None
        :Example:

        >>> player = Player(0,0,1)
        >>> str(player)
        '1'
        """
        return str(self.__num)

    def __repr__(self):
        """
        :return: the player representation
        :rtype: Player
        :UC: None
        :Example:
        >>> player = Player(0,0,0)
        >>> player
        'Player 0 at coordinate (0,0)'
        """
        return 'Player {} at coordinate ({},{})'.format(self.__num,self.__x,self.__y)

    def is_main(self):
        """
        :return: True if the player is the main player, False otherwise
        :rtype: bool
        :UC: none
        """
        return self.__is_main

    def get_x(self):
        """
        :return: the coordinate x of the player
        :rtype: int
        :UC: None
        """
        return self.__x

    def get_y(self):
        """
        :return: the coordinate y of the player
        :rtype: int
        :UC: None
        """
        return self.__y

    def get_num(self):
        """
        :return: the number of the player
        :rtype: int
        :UC: None
        """
        return self.__num

    def set_x(self,x):
        """
        :param x: coordinate x we want to set to the player
        :type x: int
        :return: None
        :side effect: affect the x coordinate to the player
        :UC: x >=0
        """
        assert type(x) == int, "coordinate are integer..."
        assert x>=0, "No negative x coordinate !"
        self.__x = x

    def set_y(self,y):
        """
        :param y: coordinate y we want to set to the player
        :type y: int
        :return: None
        :side effect: affect the y coordinate to the player
        :UC: y >=0
        """
        assert type(y) == int, "coordinate are integer..."
        assert y>=0, "No negative y coordinate !"
        self.__y = y

    def reset_compt():
        """
        Reset the number of players
        """
        Player.__compt = -1
