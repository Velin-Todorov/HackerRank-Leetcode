#!/usr/bin/bash

def countNegatives(grid):

    count = 0
    idx = -1

    for i in range(len(grid)):
        x = list(filter(lambda x: x < 0, grid[i]))
        count += len(x)     
    return count


