# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 09:49:43 2020

@author: Amr.Rizq
"""
import time
import os
import matplotlib.pyplot as plt
from matplotlib import colors

f = open("pattern.txt", "r")

if f.mode == 'r':
    f1 = f.readlines()
    w = int(f1[0])
    grid1 = [[0 for x in range(w)] for y in range(w)]

    for i in range(1, w):
        line = f1[i]
        j = 0

        for char in line:
            if char == '0' or char == '1':
                grid1[i][j] = int(char)
                j += 1

grid2 = [[0 for x in range(w)] for y in range(w)]


def sumNeighbors(grid, x, y):
    sum = 0

    if x-1 > -1:
        if y-1 > -1:
            sum += grid[x-1][y-1]

        if y+1 <= len(grid)-1:
            sum += grid[x-1][y+1]

        sum += grid[x-1][y]

    if y-1 > -1:
        sum += grid[x][y-1]

    if y+1 <= len(grid)-1:
        sum += grid[x][y+1]

    if x+1 <= len(grid)-1:
        if y-1 > -1:
            sum += grid[x+1][y-1]

        if y+1 <= len(grid)-1:
            sum += grid[x+1][y+1]

        sum += grid[x+1][y]

    return sum


def computeGrid(startingGrid, endingGrid):
    for x in range(0, len(startingGrid)):
        for y in range(0, len(startingGrid)):
            sum = sumNeighbors(startingGrid, x, y)

            if startingGrid[x][y] == 0:  # Means dead cell
                if sum == 3:
                    endingGrid[x][y] = 1
                else:
                    endingGrid[x][y] = 0
            else:
                if sum == 2 or sum == 3:
                    endingGrid[x][y] = 1
                else:
                    endingGrid[x][y] = 0


def displayGrid(grid):
    printArray = [[0 for x in range(len(grid)-6)] for y in range(len(grid)-6)]

    for x in range(3, len(grid)-3):
        for y in range(3, len(grid)-3):
            printArray[x-3][y-3] = grid[x][y]

    cmap = colors.ListedColormap(['Blue', 'red'])
    plt.figure(figsize=(4, 4))
    plt.pcolor(printArray[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.show()


direction = True
displayGrid(grid1)

while True:
    if direction == True:
        computeGrid(grid1, grid2)
        displayGrid(grid2)
    else:
        computeGrid(grid2, grid1)
        displayGrid(grid1)

    direction = not direction
    time.sleep(0.1)
