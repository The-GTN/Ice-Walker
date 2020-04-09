from multiprocessing import Queue
from game import player_mvt
from grid import *
import copy

def resolution(grid):
    """
    Give the resolution of the grid of Ice Walker
    :param grid: the grid of Ice Walker
    :type grid: Grid
    :return: the resolution of the grid
    :rtype: str
    :UC: None
    :Examples:
    >>> grid = Grid.from_file("grid01.txt")
    >>> resolution(grid)
    
    """
    assert type(grid) == Grid,"Your grid jas to be a grid..."
    print(grid)
    queue = Queue()
    visited = {}
    final = grid.get_final()
    players = grid.get_players()
    config = list()
    for player in players:
        config.append( (player.get_x(),player.get_y()) )
        
    init = copy.copy(config)

    queue.put(tuple(config))
    visited[tuple(config)] = None
    solved = False

    while not(queue.empty()) and not solved:
        s = queue.get()
        for sp in moves(grid,s):
            if sp not in visited:
                if sp[0] == final:
                    solved = True
                    solution = sp
                visited[sp] = s
                queue.put(sp)
    
    print(final)
    if solved:
        liste = [solution]
        trace = visited[sp]
        while trace !=  None:
            liste = [trace] + liste
            trace = visited[trace]
        
        chemin = str()
        for couple in range(len(liste)-1):
            for play in range(len(liste[couple])):
                if  liste[couple][play] !=  liste[couple+1][play]:
                    chemin +=  str( liste[couple][play])+ '->'+str( liste[couple+1][play])
                    if couple != len(liste)-2:
                        chemin += ','
        return chemin
                    

def moves(grid,config):        # la grille et la liste des positions des players
    """
    Return the possible plays of the players in the grid grid
    :param grid: the grid of Ice Walker
    :type grid: Grid
    :param config: list of positions of the players in the grid
    :type config: list
    :return: the possible plays of the players in the grid
    :rtype: tuple
    :UC: the config is true
    
    :Example:
    >>> grid = Grid.from_file("data/grid01.txt")
    >>> moves(a,[(12,5),(0,0),(1,2),(7,4)])
    (((15, 5), (0, 0), (1, 2), (7, 4)), ((7, 5), (0, 0), (1, 2), (7, 4)), ((12, 0), (0, 0), (1, 2), (7, 4)), ((12, 6), (0, 0), (1, 2), (7, 4)), ((12, 5), (3, 0), (1, 2), (7, 4)), ((12, 5), (0, 4), (1, 2), (7, 4)), ((12, 5), (0, 0), (5, 2), (7, 4)), ((12, 5), (0, 0), (0, 2), (7, 4)), ((12, 5), (0, 0), (1, 0), (7, 4)), ((12, 5), (0, 0), (1, 5), (7, 4)), ((12, 5), (0, 0), (1, 2), (14, 4)), ((12, 5), (0, 0), (1, 2), (3, 4)), ((12, 5), (0, 0), (1, 2), (7, 0)), ((12, 5), (0, 0), (1, 2), (7, 5)))
    """
    assert type(grid) == Grid, "Your grid has to be a grid !"
    assert type(config) == list, "Your config is a list here"
    try:
        mouvements = ['E','W','N','S']
        tu_mouv = tuple()
        new_config = copy.copy(list(config))
        grid_test =  copy.deepcopy(grid)                 #permet de faire une copie sans pb de liens entre les grilles

        for player in grid_test.get_players():      # replace les joueurs a la bonne place suivant config
            change_config( grid_test, player, config[player.get_num()] )

        for player in range(len(config)):
            play = config[player]
            init = (play[0],play[1])
            for direction in mouvements:
                player_mvt(grid_test, player ,direction)
                play2 =  grid_test.get_player(player)

                if init != (play2.get_x(),play2.get_y()):

                    new_config[player] = (play2.get_x(),play2.get_y())
                    tu_mouv += ((tuple(new_config)),)

                new_config = copy.copy(list(config))
                grid_test = copy.deepcopy(grid)

                for p in grid_test.get_players():      # replace les joueurs a la bonne place suivant config
                    change_config(grid_test, p, config[p.get_num()] )
                    
        return tu_mouv                            # liste de config possibles
    except:
        return "Your config is false..."


def change_config(grid,player,config):
    """
    Move the player to the new config, new coordinate in the grid
    :param grid: the grid of Ice Walker
    :type grid: Grid
    :param player: the player we want to move
    :type player: Player
    :param config: the new config
    :type config: tuple
    :UC: New config has to be possible
    """
    try:
        x,y = player.get_x(),player.get_y()
        cell = grid.get_cell(x,y)
        cell.remove_player()
        player.set_x(config[0])
        player.set_y(config[1])
        cell2 = grid.get_cell(config[0],config[1])
        cell2.give_player(player)
    except:
        return "Your config isn't possible !"

'''
ex:
>>> grid1 = Grid.from_file('data/gridTest.txt')
>>> config = list()
>>> for player in grid1.get_players():
        config.append((player.get_x(),player.get_y()))
>>> print(config)
((3, 2), (9, 3))
>>> print(moves2(grid1,config))
[((9, 2), (9, 3)), [(0, 2), (9, 3)], [(3, 0), (9, 3)], [(3, 3), (9, 3)], [(3, 2), (9, 0)], [(3, 2), (9, 9)]]
'''

"""
queue = Queue()          queue
visited = {}             dict
queue.put(config)        ajoute config
visited[config] = None   config est la base donc pas de déplacement avant
solved = False           pas encore résolut normalement
while not queue.empty() and not solved:         tant qu'il reste des mouvs possibles et que pas de resolution
    s = queue.get()                      on prend le premier element de la Queue
    for sp in self.moves(s):             pour tout les mouvements possibles a partir de cet config
        if sp not in visited:            si il n'as pas été visitées
            if self.is_solved(sp):       si gagant --> fini
                solved = True
                solution = sp
            visited[sp] = s              dictionnaire des deplacements
            queue.put(sp)                on rajoute le mouv dans la queue
"""
