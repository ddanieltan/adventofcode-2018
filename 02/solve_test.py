# from solve import *
from solve import solve1, solve2


def test_identify_2_repeat_letters():
    input_string = "abccdd"
    from collections import Counter

    check_for_2 = 2 in Counter(input_string).values()
    assert check_for_2 == True


def test_part1_checksum():
    input_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert solve1(input_list) == 12


def test_part2():
    input_list = input_list = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
    ]
    assert solve2(input_list) == "fgij"

