#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    #Base case
    if size == 0 or value ==0:
      return 0

    if(size[index-1] > capacity):
      return knapsack_solver(items, capacity)

    else:
      return max(
        val(index-1) + knapsack_solver(items-1, capacity-size), knapsack_solver(items-1, capacity-size)
      )

    pass


if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')