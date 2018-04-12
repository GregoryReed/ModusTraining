#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Decompress a given string.
    string is defined as a series of compressed digits in the form of
    3[abc] = abcabcabc
   Author: James Burgess (james-burgess.github.io)
"""

import timeit
import re

def expand(block):
    # break chunk into number/string pairs
    block = block.split('[')

    # multiply number by string without trailing ]
    return int(block[0]) * block[1][:-1]

def decompressor(compressed_string):
    """decompress a given string into its full form.
    """

    # find all inner compressions
    block_index = [(m.start(0), m.end(0)) for m in re.finditer(r"\d+\[+\w+]", compressed_string)]

    # work backwards to expand inner compressions
    for block in reversed(block_index):
        compressed_string = compressed_string[:block[0]] + expand(compressed_string[block[0]:block[1]]) + compressed_string[block[1]:]

    # if no compressions left retrun ans else call decompressor again
    return compressed_string if not block_index else decompressor(compressed_string)
        
    


def test():

    # multidigit
    test0 = '10[a]'
    answer = decompressor(test0)
    assert answer == 'aaaaaaaaaa', \
        "answer was %s, not aaaaaaaaaa: " % answer

    # nested
    test1 = '2[3[a]b]'
    answer = decompressor(test1)
    assert answer == 'aaabaaab', \
        "answer was %s, not aaabaaab: " % answer

    # recursive
    test2 = 'long2[chain]withlots3[3[of]chain]1[and2[some2[recursion]]]'
    answer = decompressor(test2)
    assert answer == 'longchainchainwithlotsofofofchainofofofchainofofofchainandsomerecursionrecursionsomerecursionrecursion', \
        "answer was %s, not aaabaaab: " % answer

    # banger
    test3 = '2[2[2[2[2[2[a]b]c]d]e]f]g'
    answer = decompressor(test3)
    assert answer == 'aabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefaabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefg', \
        "answer was %s, not aabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefaabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefg: " % answer

    print("All tests Passed!")

def main():

    example = '3[ab0[grgrgrgrgr]c]4[ab]c'
    # example = '20[3[a]b]'
    # example = 'abc'
    answer = decompressor(example)
    assert answer == 'abcabcabcababababc', \
        "answer was %s, not abcabcabcababababc: " %answer

    t = timeit.Timer(test)
    print(t.timeit(1))


if __name__ == '__main__':
    main()


    test_options = [
            ['1[a2[b]c]', 'abbc'],
            ['3[abc]4[ab]c', 'abcabcabcababababc'],
            ['hithere21[break]', 'hitherebreakbreakbreakbreakbreakbreakbreakbreak'
                                 'breakbreakbreakbreakbreakbreakbreakbreakbreak'
                                 'breakbreakbreakbreak'],
            ['2[2[2[a]b]c]d', 'aabaabcaabaabcd'],
            ['nowordstest', 'nowordstest'],
            ['extra characters', 'extra characters'],
            ['long2[chain]withlots3[3[of]chain]1[and2[some2[recursion]]]',
             'longchainchainwithlotsofofofchainofofofchainofofofchainand'
             'somerecursionrecursionsomerecursionrecursion'],
            ['2[2[2[2[2[2[a]b]c]d]e]f]g', 'aabaabcaabaabcdaabaabcaabaabcdeaabaabca'
                                          'abaabcdaabaabcaabaabcdefaabaabcaabaabcd'
                                          'aabaabcaabaabcdeaabaabcaabaabcdaabaabca'
                                          'abaabcdefg']]
