#!/usr/bin/python3
"""function that checks if all boxes can be unlocked"""


def canUnlockAll(boxes):
    """checks if all boxes can be unloacked
    returns true or false"""
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    return len(keys) == len(boxes)
