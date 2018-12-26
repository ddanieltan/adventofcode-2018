#%%
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
destroy_combinations = [i + j for i, j in zip(lowercase, uppercase)] + [
    j + i for i, j in zip(lowercase, uppercase)
]

#%%
def calc_reaction(string_input):
    string_output = string_input

    for combi in destroy_combinations:
        if combi in string_output:
            string_output = string_output.replace(combi, "")
            return calc_reaction(string_output)

    return string_output


#%%
def solve1():
    for line in open("05/input.txt", "r"):
        string_input = line.strip()

    print(f"Part 1 solution: {len(calc_reaction(string_input))}")


#%%
def solve2():
    for line in open("05/input.txt", "r"):
        string_input = line.strip()

    best_letter = ""
    best_length = 1_000_000
    agents = set([c.lower() for c in string_input])  # problem with letter k

    for a in agents:
        temp_string_input = string_input.replace(a, "").replace(a.upper(), "")

        current_length = len(calc_reaction(temp_string_input))
        if current_length < best_length:
            best_letter = a
            best_length = current_length

        print(a, best_letter, best_length)

    print(
        f"Part 2 solution: {best_length}"
    )  # error -> maximum recursion depth exceeded


#%%
# reddit solution
def are_opp(a, b):
    return a.lower() == b.lower() and (
        (a.isupper() and b.islower()) or (a.islower() and b.isupper())
    )


def react(line):
    buf = []
    for c in line:
        if buf and are_opp(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)


for line in open("05/input.txt", "r"):
    string_input = line.strip()
agents = set([c.lower() for c in string_input])

print(min([react(line.replace(a, "").replace(a.upper(), "")) for a in agents]))

#%%
solve2()
