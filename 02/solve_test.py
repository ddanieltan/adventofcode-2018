from solve import solve1


def test_identify_2_repeat_letters():
    input_string = "abccdd"
    from collections import Counter

    check_for_2 = 2 in Counter(input_string).values()
    assert check_for_2 == True


def test_part1_checksum():
    input_list = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
    assert solve1(input_list) == 12

