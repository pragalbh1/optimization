#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import numpy as np
Item = namedtuple("Item", ['index', 'value', 'weight'])


def dp_knapsack(items, capacity, item_count):
    """dp based solution."""
    matrix = np.zeros((capacity + 1, item_count + 1))
    for cols in range(1, item_count + 1):
        value = items[cols - 1].value
        weight = items[cols - 1].weight
        for rows in range(1, capacity + 1):
            if rows > weight:
                val = value + matrix[rows - weight][cols - 1]
            else:
                val = 0
            matrix[rows][cols] = max(matrix[rows][cols - 1], val)
    optimal_soln = matrix[capacity][item_count]
    # traceback soln
    # initialise curr_soln as optimal soln

    curr_soln = optimal_soln
    rows = capacity
    include_list = [0] * item_count
    for cols in range(item_count - 1, -1, -1):
        if curr_soln == matrix[rows][cols]:
            include_list[cols] = 0
        else:
            include_list[cols] = 1
            rows = rows - items[cols].weight
            curr_soln = curr_soln - items[cols].value
    # print matrix
    # print include_list
    return int(optimal_soln), include_list


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    # value = 0
    # weight = 0
    # taken = [0] * len(items)

    # # print items
    # # print capacity
    # #dp_knapsack(items, capacity, item_count)

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    # prepare the solution in the specified output format
    value, taken = dp_knapsack(items, capacity, item_count)
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
