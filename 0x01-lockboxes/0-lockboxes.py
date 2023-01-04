#!/usr/bin/python3
"""
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

"""

def canUnlockAll(boxes):
    """Check if all boxes can be opened"""
    lent = len(boxes)
    b = [0]
    for i in b:
        for j in boxes[i]:
            if j not in b:
                if j < lent:
                    b.append(j)
    if (len(b) == lent):
        return True
    else:
        return False 