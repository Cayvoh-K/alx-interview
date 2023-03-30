#!/usr/bin/python3
"""Script that will unlock list of lists"""


def canUnlockAll(boxes):
    """Create a list to keep track of opened boxes"""
    opened_boxes = [False] * len(boxes)
    opened_boxes[0] = True

    available_keys = boxes[0]

    while available_keys:
        key = available_keys.pop(0)
        if not opened_boxes[key]:
            opened_boxes[key] = True
            available_keys.extend(boxes[key])

    return all(opened_boxes)
