# Recommended over list queue by https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues
from collections import deque 

"""
    path[X][Y] = Z tells us that going from room number X to room number Y, 
    Z bunnies will fit in the corridor
"""
def answer(entrances, exits, path):
    
    visited = []
    discovered = deque(entrances[:])

    # Keep loop running while discovered has elements
    while discovered:
        current_room = discovered.popleft()

