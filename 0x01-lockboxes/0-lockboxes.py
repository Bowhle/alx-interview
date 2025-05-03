#!/usr/bin/python3
"""
Module for canUnlockAll function
"""

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    :param boxes: list of lists, where each sublist contains keys to other boxes
    :return: True if all boxes can be opened, else False
    """
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)
    return all(opened)
