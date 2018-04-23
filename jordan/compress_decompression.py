import re


def decompression(compressed_string: str) -> str:
    """
    Decompress a string containing the pattern of number[letters] by
        repeating the letters number mount of times
    :param compressed_string: a compressed string containing the pattern of
        number[letters] any amount of times
    :return: the decompressed version of the string given
    """
    # While there is a string that matches the pattern of number[letters]
    # Replace the pattern with the letters multiplied by the numbers
    while re.search(r'[0-9]+\[[a-z]*\]', compressed_string):
        node = re.search(
            r'(?P<number>[0-9]+)\[(?P<letter>[a-z]*)\]',
            compressed_string)
        compressed_string = compressed_string.replace(
            node.group(0),
            node.group('letter') * int(node.group('number'))
        )
    return compressed_string
