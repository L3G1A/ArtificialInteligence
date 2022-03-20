
from board import Board
import numpy as np
import time
import random


def printMap(map):
    for i in map:
        for j in i:
            if(j == 1):
                print('1 ', end='')
            if(j == 0):
                print('- ', end='')
            if(j == 2):
                print('* ', end='')
        print('')


if __name__ == '__main__':
    start_time = time.time()

    board = Board(5)
    map = board.get_map()

    restarts = 0
    board.fitness()
    tempboard = board
    fitness = board.get_fit()
    #print("Fitness: ", fitness)
    while(fitness != 0):
        cleans = 0
        queenPostions = []
        attackingQueens = []
        x = 0
        y = 0
        #printMap(map)

        while(y < len(map)):
            x = 0
            while(x < len(map[y])):

                if(map[y][x] == 1):

                    queenPostions.append([x,y])
                    i = x
                    j = y
                    
                    moves = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

                    while(board.attackersatposition(i,j) != 0):
                        #print("Attackers: ", board.attackersatposition(i,j))
                        oI = i
                        oJ = j
                        i += moves[random.randint(0,7)][0]
                        j += moves[random.randint(0,7)][1]

                        if(i  < len(map) and j < len(map) and i > -1 and j > -1):
                            if(map[j][i] != 1):
                                map[oJ][oI] = 0
                                map[j][i] = 1
                                if(j == oJ and i == oI):
                                    board = Board(5)

                                board.map = map

                        else:
                            i = oI
                            j = oJ
                        #printMap(map)  
                        cleans += 1
                    #print(cleans)
                    #print("Position: (", i , ', ', j, ')', "Attackers: ", board.attackersatposition(i,j))
        
                x+= 1
            y += 1
        if(cleans == 0):
            break
        #print(queenPostions)
        #print(attackingQueens)
    board.fitness()

    fitness = board.get_fit()
    #print("Fitness: ", fitness)
    print("Running time: ", round((float(time.time() - start_time) * 1000)) , "ms")
    print("# of restart: ", restarts)
    printMap(map)
    
