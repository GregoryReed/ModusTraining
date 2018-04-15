#!/usr/bin/env python
# -*- coding: utf-8 -*-


def tester():
    """ A number of tests to check if the remove method is working as expected
    :return:
    """
    # remove unique number from list
    test1 = [54, 22, 5, 2, 78, 98]
    test1.remove(5)
    assert test1 == [54, 22, 2, 78, 98], "answer was {}, not [54, 22, 2, 78, 98]".format(test1)

    # remove repeated letter from list
    test2 = ['a', 'abc', 'a', 'bb', 'c', 'z']
    test2.remove('a')
    assert test2 == ['abc', 'a', 'bb', 'c', 'z'], "answer was {}, not ['abc', 'a', 'bb', 'c', 'z']".format(test2)

    # numbers after removed number shift to left in list
    list3 = [54, 22, 5, 2, 78, 98]
    index_78_before = list3.index(78)
    list3.remove(2)
    index_78_after = list3.index(78)
    test3 = index_78_before - index_78_after
    assert test3 == 1, "answer was {}, not 1".format(test3)

    # when letter not in list, raise ValueError
    test4 = ['xyz', 'abc', 'mark', 'bb', 'c', 'z']
    try:
        test4.remove('a')
        raise AssertionError('ValueError should have been raised')
    except ValueError:
        assert test4 == ['xyz', 'abc', 'mark', 'bb', 'c', 'z'], "answer was {}, not ['abc', 'a', 'bb', 'c', 'z']".format(test4)

    # size of list shrinks when a list is removed
    test5 = [[45, 'ab'], [33, 'bc'], ['nyc', 69]]
    test5.remove([33, 'bc'])
    assert len(test5) == 2, "answer was {}, not 2".format(len(test5))

print('All tests passed.')

def main():
    tester()


if __name__ == '__main__':
    main()