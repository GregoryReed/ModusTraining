#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Decompress a given string.
    string is defined as a series of compressed digits in the form of
    3[abc] = abcabcabc
   Author: James Burgess (james-burgess.github.io)
"""

import timeit


def decompressor(compressed_string):
    """decompress a given string into its full form.
    """
    for char in compressed_string:
        if char.isdigit():
            print (char)

def test():
    pass

def main():

    example = '3[abc]4[ab]c'
    answer = decompressor(example)
    assert answer == 'abcabcabcababababc', \
        "answer was %s, not abcabcabcababababc: " %answer

    t = timeit.Timer(test)
    print(t.timeit(1))


if __name__ == '__main__':
    main()
