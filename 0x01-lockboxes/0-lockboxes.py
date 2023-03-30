#!/usr/bin/python3
"""Script that will unlock list of lists"""


def canUnlockAll(boxes):
    """Create a list to keep track of opened boxes"""
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True

    keys = [0]
    while keys:
        box_num = keys.pop()
        for key in boxes[box_num]:
            if not opened_boxes[key]:
                opened_boxes[key] = True
                keys.append(key)

    return all(opened_boxes)
