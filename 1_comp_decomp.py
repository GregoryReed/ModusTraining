#!/usr/bin/env python
# -*- coding: utf-8 -*-


def decompress(source, subs):
    """
    :param source:
    :param subs:
    :return:
    """
    # breaks recursive loop
    if source == '':
        return subs
    # initialise
    num_value = ''
    letters = ''
    lonely = ''
    close_index = len(source) - 1
    open_index = 0
    left_zone = 0
    num = 1
    # finding trailing letters not in compressed string
    if ']' not in source:
        lonely = source
    # counting from left to right
    for i, value in enumerate(source):
        if value == ']':
            close_index = i
            break
    # counting left from inner close bracket until end compressed string num
    for i in range(close_index - 1, -1, -1):
        if source[i] != '[' and left_zone == 0:
            letters = source[i] + letters
        elif source[i] == '[' and left_zone == 0:
            open_index = i
            left_zone += 1
        elif source[i] != '[' and left_zone == 1:
            num_value = source[i:open_index]
            num = int(num_value)
        else:
            break
    # building decompressed string and removing compressed string from source
    num_index = open_index - len(num_value)
    subs = num * (subs + letters) + lonely
    source = source[0:num_index] + source[close_index + 1:]
    return decompress(source, subs)

print(decompress('5[abc]4[ab]c', ''))
print(decompress('2[3[a]b]', ''))
print(decompress('0[abc]', ''))
print(decompress('5[0[a]]abc', ''))
print(decompress('5[1[a]]abc', ''))
print(decompress('10[a]', ''))
print(decompress('2[5[a]ab]', ''))



