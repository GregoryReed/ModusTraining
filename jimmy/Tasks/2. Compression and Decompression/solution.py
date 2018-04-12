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
    count = 0
    index = 0
    for i, char in enumerate(reversed(compressed_string)):
        if char == ']':
            print("delimiter")
            index = i
            count += 1

        if char == '[':
            print('eascape')
            print(compressed_string[index+1: i])



    # openers, closers = [], []
    # depth = 0
    # # find all [] and append location to array
    # for i, char in enumerate(compressed_string):
    #     if char == '[' and :
    #         depth += 1
    #         openers.append(i)
    #
    #     if char == ']':
    #         closers.append(i)
    #
    # print(openers)
    # print(closers)

    # create pairs of
    #

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

    print("All tests Passed!")

def main():

    example = '3[abc]4[ab]c'
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
