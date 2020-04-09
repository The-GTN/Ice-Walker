# Imports
from player import *
from cell import *
from grid import *
import sys
import time


# game
def player_mvt(grid,nb_player,direction):
    """
    Move a selected player to a selected direction
    :param grid: (Grid) the grid
    :param nb_player:(int) the number of the choosen player
    :param direction:(str) the direction
    :return: None
    :side effect: change the coordinate of the player
    :CU: (int(player) <= self.get_nb_players-1) and (direction == 'N' or direction == 'S' or direction == 'W' or direction == 'E')
    """
    assert type(grid) == Grid, "Your grid isn't a grid !"
    assert type(nb_player) == int,"Your num of the player has to be an integer !"
    assert nb_player <= grid.get_nb_players(), "Select a valid player !"
    assert direction in 'NnSsWwEe', "Select a valid direction !"
    player = grid.get_player(nb_player)
    x = player.get_x()
    y = player.get_y()
    is_main = player.is_main()
    w = grid.get_width()
    h = grid.get_height()

    cell = grid.get_cell(x,y)

    if direction in 'nN' and y > 0:     # up
        cell.remove_player()
        y -= 1
        cell = grid.get_cell(x,y)
        while y > 0 and not(cell.has_south_wall() or cell.has_player() or grid.state() ):
            if is_main and cell.is_win():
                grid.change_state()
                Player.reset_compt()
            else:
                y -= 1
                cell = grid.get_cell(x,y)
            
        if cell.has_south_wall() or cell.has_player():
            cell = grid.get_cell(x,y+1)
            cell.give_player(player)
            player.set_y(y+1)
            player.set_x(x)
            if grid.state():
                grid.change_state()
        else:
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x)

    elif direction in 'sS' and y < h :   # down
        cell.remove_player()
        while y < h-1 and not(cell.has_south_wall() or cell.has_player() or grid.state() ):
            y += 1
            cell = grid.get_cell(x,y)
            if is_main and cell.is_win():
                grid.change_state()
                Player.reset_compt()
        if cell.has_player():
            cell = grid.get_cell(x,y-1)
            cell.give_player(player)
            player.set_y(y-1)
            player.set_x(x)
            if grid.state():
                grid.change_state()
        else:
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x)

    elif direction in 'eE' and x < w :   # rigth
        cell.remove_player()
        cell = grid.get_cell(x,y)
        while x < w-1 and not(cell.has_east_wall() or cell.has_player() or grid.state() ) :
            x += 1
            cell = grid.get_cell(x,y)
            if is_main and cell.is_win():
                grid.change_state()
                Player.reset_compt()
        if cell.has_player():
            cell = grid.get_cell(x-1,y)
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x-1)
            if grid.state():
                grid.change_state()
        else:
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x)

    elif x > 0 and direction in "wW":                    # left
        cell.remove_player()
        x -= 1
        cell = grid.get_cell(x,y)
        while x > 0 and not(cell.has_east_wall() or cell.has_player() or grid.state() ):
            if is_main and cell.is_win():
                grid.change_state()
                Player.reset_compt()
            else:
                x -= 1
                cell = grid.get_cell(x,y)

        if cell.has_east_wall() or cell.has_player():
            cell = grid.get_cell(x+1,y)
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x+1)
            if grid.state():
                grid.change_state()
        else:
            cell.give_player(player)
            player.set_y(y)
            player.set_x(x)

        
def repl_play(grid):
    """
    Play an Ice Walker party with the grid grid
    :param grid: the grid where we play
    :type grid: Grid
    :return: the game of Ice walker
    """
    assert type(grid) == Grid, "Your grid isn't a grid !"
    abandon = False
    while not(grid.state() or abandon):

        print(grid)
        action = input("Entrer votre mouvement 'num,direction' : ou 'q' (quit)\n")

        if action == 'q':
            abandon = True
            print("Merci d'avoir joué !")

        else:
            try:
                action = action.split(',')
                p,direction = int(action[0]), action[1]
                if p > grid.get_nb_players()-1 or p < 0:
                    print("Veuillez choisir un joueur présent \n ")
                    time.sleep(1)
                if direction not in ['E','S','W','N']:
                    print("Veuillez choisir une direction valide  \n ")
                    time.sleep(1)
                elif 0<=p < grid.get_nb_players():
                    player_mvt(grid,p,direction)
            except (IndexError, ValueError):
                print('Veuillez entrée une commande valide de type:  num,direction  \n ')
                time.sleep(1)
        if grid.state():
            print("Gagné !!")


def usage():
    print('1 arg needed, an existing grid file without .txt')
    from os import listdir
    from os.path import isfile, join
    fichiers = [f for f in listdir('data') if isfile(join('data', f))]
    for fichier in fichiers:
        print(fichier.replace('.txt',''))

def available():
    from os import listdir
    from os.path import isfile, join
    fichiers = [f for f in listdir('data') if isfile(join('data', f))]
    print('You need to select an existing grid. Grids available are:')
    for fichier in fichiers:
        print(fichier.replace('.txt',''))

def main():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            src = 'data/'+sys.argv[1]+'.txt'
            grid = Grid.from_file(src)
            repl_play(grid)
        except:
            available()

if __name__ == '__main__':
    main()
