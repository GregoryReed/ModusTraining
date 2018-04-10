from itertools import repeat
import re

def decompression(comp_str):
    main_str = ''
    # Check for any recursion
    recursion_check = re.compile(r'\[[0-9]+\[[a-z0-9\[\]]+\][a-z]+\]')

    for recursion_pattern in recursion_check.findall(comp_str):
        comp_str = comp_str.replace(
            recursion_pattern[1:-1], decompression(recursion_pattern[1:-1])
        )

    # Split compressed string into sections
    split_str = comp_str.split(']')

    # Cycle through each section and split into different parts
    for section in split_str:
        if not section:
            continue
        split_items = re.split('([a-z]+(?=[0-9]+)|\[)', section)
        if not split_items[0]:
            main_str += split_items[1]
            split_items = split_items[2:]

        # Append letters onto master string
        if len(split_items) - 1:
            for x in repeat(split_items[-1], int(split_items[0])):
                main_str += x
        else:
            main_str += split_items[0]

    return main_str

if __name__ is '__main__':
    test_options = [
        ['3[abc]4[ab]c', 'abcabcabcababababc'],
        ['hithere21[break]', 'hitherebreakbreakbreakbreakbreakbreakbreakbreak'
                             'breakbreakbreakbreakbreakbreakbreakbreakbreak'
                             'breakbreakbreakbreak'],
        ['2[2[2[a]b]c]d', 'aabaabcaabaabcd'],
        ['nowordstest', 'nowordstest'],
        ['extra characters', 'extra characters']
    ]
    for code in test_options:
        print(code[0])
        assert decompression(code[0]) == code[1]
