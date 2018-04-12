#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Calculate the total volume in a lake according to the size of a lake.
    lake is described as a list of values representing a histogram like chart
    each dip in the chart would represent a volume of water held in the lake
    calculates the sum of all the dips
   Author: James Burgess (james-burgess.github.io)
"""

import timeit


def find_lake_volume(lake_data):
    """Calculate the total volume in a lake.
        makes a run from left to right and righ to left
        finds dips ahead and appends to respective run array
        comparison is made between both runs to find the smallest dip and
        adds dip to answer.
    """
    ans = 0
    lake_len = len(lake_data) - 1
    right_run = [0]
    left_run = [0]
    left_max_height = lake_data[0]
    right_max_height = lake_data[-1]

    for i in range(lake_len):
        # find left peak
        if lake_data[i] >= left_max_height:
            left_max_height = lake_data[i]

        # append dip size
        if lake_data[i+1] < left_max_height:
            left_run.append(left_max_height - lake_data[i+1])
        else:
            left_run.append(0)

        # find right peak
        if lake_data[lake_len - i] >= right_max_height:
            right_max_height = lake_data[lake_len - i]

        # append dip size
        if lake_data[lake_len - i - 1] < right_max_height:
            right_run.append(right_max_height - lake_data[lake_len - i - 1])
        else:
            right_run.append(0)

    # reverse right_run
    right_run = right_run[::-1]

    # add smallest dip to answer
    for i in range(lake_len):
        ans += min(left_run[i], right_run[i])

    return ans


def test():
    # small v
    test0 = [2, 0, 2]
    # random set
    test1 = [244, 246, 34, 35, 226, 30, 203, 116, 219, 114, 217, 95, 141, 142,
             114, 61, 95, 82, 126, 221, 184, 146, 95, 164, 115, 194, 229, 10,
             178, 143, 154, 190, 255, 100, 153, 212, 211, 57, 228, 169, 8, 48,
             0, 196, 54, 204, 36, 222, 97, 149, 75, 227, 14, 19, 141, 239, 193,
             100, 204, 51, 240, 120, 128, 184, 98, 244, 48, 8, 110, 56, 5, 137,
             72, 106, 56, 187, 134, 165, 114, 92, 76, 135, 169, 22, 28, 242,
             88, 151, 215, 37, 89, 102, 2, 241, 246, 212, 74, 17, 254]
    # small dips
    test2 = [2, 2, 1, 3, 2, 3, 3, 2, 1, 2, 1, 2, 3, 2, 1, 3, 1, 1, 1, 2, 3, 1,
             1, 2, 1, 3, 1, 2, 2, 3, 1, 2, 1, 3, 2, 3, 3, 3, 1, 1, 2, 1, 3, 3,
             2, 3, 2, 3, 3, 2, 1, 3, 1, 3, 2, 3, 1, 2, 3, 3, 2, 3, 2, 2, 3, 3,
             1, 3, 2, 2, 3, 1, 1, 3, 2, 3, 3, 3, 1, 1, 2, 2, 1, 2, 3, 3, 3, 2,
             2, 3, 1, 2, 1, 2, 1, 2, 1, 1, 1]
    # negative numbers
    test3 = [0, 1, -2, -2, -2, -2, 0, -2, 0, -2, -2, -1, 1, -2, -1, -1, -2, -2,
             -1, -1, -2, -3, 0, -1, 1, -3, -1, 1, -2, 1, -3, 1, 0, -3, -3, 1,
             0, 0, -2, 0, -2, -2, -1, 1, 0, -2, -3, -1, -1, 1, 0, -2, -1, -3,
             1, 0, -3, 0, -3, -1, 1, -2, -1, -3, -3, -1, -2, -3, 1, 1, -2, -3,
             1, 1, -3, -1, -2, -2, 1, 1, -3, 1, -2, -2, -1, -2, -2, -3, 1, -3,
             -2, 1, -2, 1, -1, -3, -2, -3, 1]
    # huge set 1028
    test4 = [233, 230, 75, 250, 48, 164, 167, 187, 164, 189, 59, 56, 138, 81,
             102, 76, 123, 6, 161, 237, 41, 204, 172, 53, 251, 54, 167, 62,
             197, 175, 92, 226, 164, 33, 156, 33, 9, 125, 219, 89, 136, 49, 65,
             166, 92, 187, 128, 0, 82, 196, 87, 119, 8, 202, 170, 209, 37, 106,
             2, 204, 13, 176, 207, 76, 51, 154, 121, 146, 206, 86, 100, 146,
             34, 9, 179, 90, 89, 61, 144, 61, 33, 4, 7, 71, 229, 139, 135, 36,
             150, 67, 184, 148, 145, 184, 225, 103, 206, 215, 34, 101, 59, 22,
             246, 183, 197, 135, 104, 83, 64, 17, 124, 165, 50, 103, 38, 82,
             239, 157, 151, 63, 100, 242, 46, 156, 13, 111, 9, 136, 106, 140,
             86, 189, 122, 128, 136, 37, 181, 118, 191, 202, 109, 186, 23, 134,
             249, 129, 213, 134, 33, 252, 70, 170, 43, 13, 252, 32, 144, 3,
             203, 177, 18, 70, 100, 3, 187, 185, 64, 222, 143, 63, 227, 234,
             160, 154, 80, 39, 255, 153, 130, 140, 174, 67, 236, 212, 92, 119,
             150, 243, 242, 123, 117, 12, 188, 210, 129, 61, 165, 218, 37, 173,
             191, 86, 200, 248, 253, 47, 39, 229, 67, 125, 146, 187, 233, 255,
             205, 111, 149, 83, 196, 11, 47, 114, 136, 159, 70, 129, 32, 196,
             83, 159, 85, 114, 66, 174, 220, 173, 82, 6, 75, 252, 241, 74, 133,
             184, 232, 75, 164, 190, 84, 96, 197, 163, 30, 176, 172, 222, 138,
             163, 224, 109, 53, 106, 0, 222, 6, 192, 28, 54, 250, 107, 84, 140,
             1, 216, 5, 43, 23, 91, 68, 251, 213, 167, 250, 28, 142, 105, 3,
             148, 21, 158, 28, 73, 26, 107, 84, 143, 111, 88, 32, 74, 229, 16,
             22, 222, 188, 116, 164, 0, 37, 24, 247, 131, 69, 82, 152, 242, 76,
             44, 170, 90, 159, 8, 169, 78, 228, 65, 9, 61, 78, 207, 6, 88, 83,
             163, 88, 62, 14, 134, 82, 105, 166, 150, 235, 73, 80, 173, 249,
             94, 18, 117, 201, 204, 154, 188, 250, 49, 172, 115, 236, 214, 93,
             174, 137, 119, 171, 134, 88, 247, 94, 240, 183, 190, 62, 24, 11,
             112, 189, 19, 75, 25, 67, 1, 210, 8, 201, 117, 223, 23, 203, 217,
             59, 187, 124, 20, 43, 108, 143, 18, 108, 47, 83, 92, 195, 17, 189,
             154, 234, 221, 113, 30, 163, 162, 124, 168, 13, 99, 108, 54, 251,
             127, 32, 214, 239, 147, 135, 16, 172, 57, 116, 155, 160, 45, 182,
             188, 89, 200, 143, 90, 212, 63, 242, 129, 86, 185, 197, 154, 176,
             53, 90, 4, 104, 255, 228, 134, 199, 127, 223, 158, 157, 191, 81,
             47, 65, 255, 120, 74, 236, 37, 102, 142, 61, 204, 112, 192, 66, 2,
             159, 42, 112, 109, 178, 8, 173, 229, 191, 30, 10, 58, 147, 251,
             102, 142, 221, 242, 187, 101, 163, 227, 10, 115, 230, 20, 196, 97,
             205, 16, 140, 5, 116, 204, 176, 11, 229, 93, 48, 72, 159, 251, 12,
             4, 48, 64, 239, 35, 193, 47, 145, 48, 100, 214, 159, 9, 227, 115,
             196, 118, 162, 140, 241, 94, 172, 48, 240, 218, 1, 60, 176, 38,
             217, 85, 116, 202, 202, 52, 146, 182, 190, 204, 31, 120, 205, 167,
             56, 246, 145, 76, 194, 92, 151, 80, 250, 237, 120, 195, 1, 163,
             231, 82, 87, 108, 110, 252, 86, 25, 156, 39, 42, 206, 63, 126,
             254, 221, 6, 125, 170, 33, 52, 1, 44, 230, 216, 12, 141, 83, 53,
             5, 116, 97, 205, 173, 221, 127, 151, 218, 12, 162, 164, 252, 99,
             53, 75, 202, 190, 112, 181, 162, 22, 17, 151, 67, 197, 4, 11, 196,
             88, 165, 145, 214, 157, 33, 214, 61, 104, 107, 3, 211, 182, 172,
             64, 165, 219, 26, 209, 104, 180, 212, 234, 161, 95, 26, 210, 31,
             55, 38, 83, 130, 189, 57, 216, 79, 193, 250, 27, 230, 113, 221,
             180, 236, 38, 152, 209, 245, 161, 59, 73, 47, 244, 97, 105, 136,
             124, 123, 112, 159, 219, 219, 151, 47, 219, 43, 62, 176, 37, 146,
             62, 186, 238, 250, 8, 127, 33, 172, 204, 66, 129, 127, 76, 29, 43,
             227, 45, 150, 47, 251, 242, 99, 254, 102, 72, 136, 203, 171, 94,
             66, 254, 165, 119, 220, 102, 157, 62, 212, 63, 90, 84, 144, 5,
             231, 33, 63, 133, 57, 126, 41, 38, 142, 156, 68, 1, 189, 193, 82,
             152, 85, 170, 108, 61, 97, 245, 139, 205, 115, 169, 6, 87, 182,
             112, 240, 91, 120, 51, 160, 78, 119, 113, 128, 124, 213, 32, 138,
             206, 218, 123, 137, 43, 236, 234, 29, 44, 171, 100, 169, 167, 227,
             164, 84, 232, 38, 247, 173, 76, 152, 6, 200, 237, 75, 116, 48,
             203, 72, 120, 68, 201, 110, 162, 127, 193, 133, 120, 134, 136, 98,
             34, 209, 130, 101, 18, 169, 82, 151, 116, 215, 93, 206, 5, 167,
             193, 103, 245, 217, 49, 57, 164, 131, 143, 204, 131, 92, 208, 95,
             119, 93, 135, 36, 120, 194, 51, 209, 62, 102, 106, 0, 142, 200,
             58, 5, 165, 159, 144, 122, 45, 251, 187, 113, 181, 122, 56, 8, 15,
             196, 39, 101, 88, 103, 109, 176, 36, 182, 205, 38, 117, 214, 64,
             185, 225, 180, 15, 159, 119, 38, 172, 19, 155, 193, 124, 121, 72,
             24, 110, 51, 96, 38, 40, 245, 224, 127, 222, 120, 133, 70, 208,
             62, 73, 144, 168, 33, 101, 43, 103, 131, 250, 39, 66, 225, 20,
             194, 148, 51, 184, 208, 230, 105, 104, 92, 177, 148, 94, 56, 216,
             247, 149, 11, 146, 222, 205, 49, 44, 235, 94, 253, 69, 165, 253,
             164, 55, 26, 26, 91, 115, 210, 48, 232, 147, 1, 66, 231, 118, 45,
             135, 129, 107, 56, 254, 123, 15, 156, 241, 24, 157, 169, 209, 253,
             39, 237, 198, 154, 201, 216, 39, 36, 246, 191, 138, 136, 41, 241,
             126, 91, 106, 127, 113, 193, 112, 93, 29, 112, 27, 145]

    answer = find_lake_volume(test0)
    assert answer == 2, "Test0 - Answer was %s not 2" %answer

    answer = find_lake_volume(test1)
    assert answer == 11960, "Test1 - Answer was %s not 11960" % answer

    answer = find_lake_volume(test2)
    assert answer == 80, "Test1 - Answer was %s not 80" % answer

    answer = find_lake_volume(test3)
    assert answer == 208, "Test1 - Answer was %s not 208" % answer


    answer = find_lake_volume(test4)
    assert answer == 129507, "Test4 - Answer was %s not 129507" % answer

def main():
    example = [1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]

    answer = find_lake_volume(example)
    assert answer == 15, "answer was not 15, answer was: " + str(answer)

    t = timeit.Timer(test)
    print(t.timeit(1))


if __name__ == '__main__':
    main()
