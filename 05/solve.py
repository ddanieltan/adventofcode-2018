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
for line in open("input.txt", "r"):
    print(calc_reaction(line))

#%%
!pwd