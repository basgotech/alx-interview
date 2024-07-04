#!/usr/bin/python3

""" Check if all lockboxes can be unlocked """


def canUnlockAll(boxes):
    """
    - Determines if all the boxes can be opened.
    - boxes: a list of lists where each
    - sublist contains keys to other boxes.
    - True if all boxes can be opened, else False.
    """

    can_Unlock_All = False
    keys_get = {0: True}
    get_len_box = len(boxes)
    while(True):

        key_len = len(keys_get)

        for x in range(len(boxes)):
            if boxes[x] and keys_get.get(x, False):
                for y in boxes[x]:
                    if y < get_len_box:
                        keys_get[y] = True
                    boxes[x] = None

        if not(len(keys_get) > key_len):
            break

    if key_len == len(boxes):
        can_Unlock_All = True

    return can_Unlock_All
