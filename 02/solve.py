#%%
# Part 1
from collections import Counter
from itertools import combinations


def solve1(input_list):
    two_counter = 0
    three_counter = 0
    for i in input_list:
        dictionary = Counter(i)

        if 2 in dictionary.values():
            two_counter += 1
        if 3 in dictionary.values():
            three_counter += 1

    return two_counter * three_counter


#%%
def compare(a, b):
    """Given 2 words, return the num of different letters 
    and the different letters"""

    # check if words are same length
    if len(a) != len(b):
        return "Words not same length"

    num_of_diffs = 0
    diff_letters = []
    for i in range(len(a)):
        if a[i] == b[i]:
            diff_letters.append(a[i])
        else:
            num_of_diffs += 1

    return num_of_diffs, diff_letters


def solve2(input_list):

    combis = combinations(input_list, 2)

    for (a, b) in combis:
        num_of_diffs, diff_letters = compare(a, b)
        if num_of_diffs == 1:
            return "".join(diff_letters)

    return "No solution found"


#%%
compare("abcd", "abcc")

#%%
input_list = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]
solve2(input_list)

#%%
with open("input.txt", "r") as f:
    puzzle_input = f.read().splitlines()
print(f"Part 1 solution: {solve1(puzzle_input)}")
print(f"Part 2 solution: {solve2(puzzle_input)}")

