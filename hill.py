
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
    moveCounter = 0
    zeroMoveCounter = 0

    fitness = board.get_fit()
    #print("Fitness: ", fitness)
    while(fitness != 0):
        cleans = 0
        queenPostions = []
        attackingQueens = []
        x = 0
        y = 0
        loopCounter = 0
        #printMap(map)

        while(y < len(map)):
            x = 0
            while(x < len(map[y])):
                if(map[y][x] == 1):

                    queenPostions.append([x,y])
                    i = x
                    j = y
                    
                    moves = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
                    random.shuffle(moves)
                    nextAttackingNumber = board.attackersatposition(i,j)

                    while(nextAttackingNumber != 0):
                        oI = i
                        oJ = j

                        nowMove = []
                        for move in moves:

                                if(nextAttackingNumber == 0):
                                    break
                                findi = i + move[0] 
                                findj = j + move[1] 

                
                                if(findi  < len(map) and findj < len(map) and findi > -1 and findj > -1):

                                    checkValue = board.attackersatposition(findi,findj)
                                    
                                    if(checkValue == 0):
                                        nowMove = move
                                        break

                                    if(checkValue < nextAttackingNumber):

                                        nowMove = move
                                        nextAttackingNumber = checkValue


                        if(len(nowMove) == 0):

                            nowMove = moves[random.randint(0,7)]





                        i += nowMove[0]
                        j += nowMove[1]  

                        if(loopCounter > 300 or zeroMoveCounter >= 10):
                            board = Board(5)
                            loopCounter = 0
                            moveCounter = 0
                            zeroMoveCounter = 0

                            restarts += 1
                        if(moveCounter == 0):
                            zeroMoveCounter += 1

                        if(i  < len(map) and j < len(map) and i > -1 and j > -1):
                            if(map[j][i] != 1):
                                map[oJ][oI] = 0
                                map[j][i] = 1

                                moveCounter += 1

                                board.map = map
        
    
                        else:
                            i = oI
                            j = oJ

                        cleans += 1
                        loopCounter += 1
                        nextAttackingNumber = board.attackersatposition(i,j)

                    loopCounter = 0


         
                x+= 1
            y += 1
        if(cleans == 0):
            break

    board.fitness()

    fitness = board.get_fit()
    print("Running time: ", round((float(time.time() - start_time) * 1000)) , "ms")
    print("# of restarts: ", restarts)

    printMap(map)
    
