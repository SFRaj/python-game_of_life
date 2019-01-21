#! /usr/bin/env python3
# coding: utf-8
# with contributions from : antsalamatheuse chez gmail point com
"""
a script for simulating and visualising Conways' Game of Life
"""
import numpy as np
import matplotlib.pyplot as plt


def neighbors(mat, i, j):
    """
    given a matrix mat and indexes i, j return the indexes of all mat[i, j] neighbors
    thus excluding negative and out of range indexes
    """
    imax, jmax = mat.shape
    valid_neighbors = []
    possible_neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1),
                          (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
    for neighbor in possible_neighbors:
        if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] < imax and neighbor[1] < jmax:
            valid_neighbors.append(neighbor)
    return valid_neighbors

def neighbors_alive(mat, i, j):
    """
    the number of alive neighbors of a cell [i, j]
    """
    alive = 0
    for (i, j) in neighbors(mat, i, j):
        if mat[i][j] == 1:
            alive += 1
    return alive

def nextgen_cell(mat, i, j):
    """
    the status (dead or alive) of a cell A[i, j] in the next generation
    """
    if neighbors_alive(mat, i, j) == 3:
        nextgen = 1
    if neighbors_alive(mat, i, j) == 2:
        nextgen = mat[i][j]
    if neighbors_alive(mat, i, j) < 2 or neighbors_alive(mat, i, j) > 3:
        nextgen = 0
    return nextgen

def nextgen_matrix(mat):
    """
    computes the next generation
    """
    imax, jmax = mat.shape
    next_mat = np.zeros((imax, jmax))
    for i in range(imax):
        for j in range(jmax):
            next_mat[i][j] = nextgen_cell(mat, i, j)
    return next_mat.astype(int)

def visualize(config, nsteps):
    """
    visualise the evolution of config matrix in nsteps time
    """
    generations = []
    for i in range(nsteps):
        generations.append(config)
        config = nextgen_matrix(config)

    for config in generations:
        plt.matshow(config, fignum=0)
        plt.pause(0.5) # pause in seconds

    plt.show()

def main():
    """
    main function with example of initial configuration
    """
    config = np.array([[0, 0, 1, 0],
                       [1, 0, 0, 1],
                       [1, 0, 0, 1],
                       [1, 0, 0, 1]])
    visualize(config, 40)

if __name__ == "__main__":
    main()
