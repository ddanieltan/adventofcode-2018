#%%
def calc(freq_list):
    frequency=0

    for i in freq_list:
        operand=i[0]
        number=int(i[1:])

        if operand=='+':
            frequency+=number
        elif operand=='-':
            frequency-=number
    
    return frequency

#%%
with open('input.txt','r') as f:
    puzzle_input=f.read().splitlines()
