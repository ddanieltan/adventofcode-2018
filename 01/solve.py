# Part 1
#%%
def calc(freq_list):
    frequency = 0

    for i in freq_list:
        operand = i[0]
        number = int(i[1:])

        if operand == "+":
            frequency += number
        elif operand == "-":
            frequency -= number

    return frequency


#%%
with open("input.txt", "r") as f:
    puzzle_input = f.read().splitlines()
print(f"Part 1 answer: {calc(puzzle_input)}")

# Part 2
#%%
from itertools import cycle


def calc_repeat(freq_list):
    frequency = 0
    seen = {0}
    for i in cycle(freq_list):
        operand = i[0]
        number = int(i[1:])
        if operand == "+":
            frequency += number
        elif operand == "-":
            frequency -= number

        if frequency in seen:
            return frequency
        seen.add(frequency)


#%%
with open("input.txt", "r") as f:
    puzzle_input = f.read().splitlines()
print(f"Part 2 answer: {calc_repeat(puzzle_input)}")
