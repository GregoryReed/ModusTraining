#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import timeit


def decompress(tight_object):
    """ Pull out inner compressions, expand, re-insert and repeat by applying
    recursion to the new string.
    :param tight_object: string
    :return tight_object: string
    """
    # Find num / value pairs of inner-most compressions
    inners = re.findall(r"\d+\[+\w+]|\d+\[+]", tight_object)

    # Replace num / value pairs with expanded pairs
    for num_value in inners:
        tight_object = tight_object.replace(num_value, expansion(num_value))

    # Expand inner-most compressions
    if not inners:
        return tight_object
    else:
        return decompress(tight_object)

def expansion(pair):
    """ Extract the number in front of a bracketed string and multiply the
    number by the string.
    param: pair string
    return: long_letters string
    """
    # Split num / value into pairs
    split_pair = pair.split('[')

    # Multiply pairs together
    long_letters = int(split_pair[0]) * split_pair[1][:-1]

    return long_letters


def test():
    # multidigit
    test0 = '10[a]'
    answer = decompress(test0)
    assert answer == 'aaaaaaaaaa', \
        "answer was {}, not aaaaaaaaaa: ".format(answer)

    # nested
    test1 = '2[3[a]b]'
    answer = decompress(test1)
    assert answer == 'aaabaaab', \
        "answer was {}, not aaabaaab: ".format(answer)

    # recursive
    test2 = 'long2[chain]withlots3[3[of]chain]1[and2[some2[recursion]]]'
    answer = decompress(test2)
    assert answer == 'longchainchainwithlotsofofofchainofofofchainofofofchainandsomerecursionrecursionsomerecursionrecursion', \
        "answer was {}, not longchainchainwithlotsofofofchainofofofchainofofofchainandsomerecursionrecursionsomerecursionrecursion: ".format(answer)

    # banger
    test3 = '2[2[2[2[2[2[a]b]c]d]e]f]g'
    answer = decompress(test3)
    assert answer == 'aabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefaabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefg', \
        "answer was {}, not aabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefaabaabcaabaabcdaabaabcaabaabcdeaabaabcaabaabcdaabaabcaabaabcdefg: ".format(answer)

    # by zero
    test4 = '0[abc]'
    answer = decompress(test4)
    assert answer == '', "answer was {}, not".format(answer)

    # inner zero
    test5 = '5[0[abc]]xyz'
    answer = decompress(test5)
    assert answer == 'xyz', "answer was {}, not".format(answer)

    print("All tests Passed!")


def main():
    test()
    t = timeit.Timer(test)
    print(t.timeit(200)/100)


if __name__ == '__main__':
    main()
