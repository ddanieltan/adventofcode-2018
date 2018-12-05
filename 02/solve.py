#%%
# Part 1
from collections import Counter


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
