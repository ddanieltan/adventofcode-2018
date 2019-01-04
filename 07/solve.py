#%%
import numpy as np
import re
from collections import defaultdict

#%%
def parse_instruction(line):
    regex = r"Step ([A-Z]) must be finished before step ([A-Z]) can begin."
    matched = re.search(regex, line)
    if matched:
        return (matched.group(1), matched.group(2))
    else:
        raise Exception(f"Unable to parse line: {line}")


#%%
def preconditions(lines):
    preconditions = defaultdict(list)
    remaining_steps = set()
    for line in lines.splitlines():
        before, after = parse_instruction(line)
        remaining_steps.add(before)
        remaining_steps.add(after)
        preconditions[after].append(before)

    for k, _ in preconditions.items():
        remaining_steps.remove(k)

    for step in remaining_steps:
        preconditions[step]

    return preconditions


#%%
def find_order(lines):
    preconds = preconditions(lines)
    final_order = []
    while preconds:  # while there are items in the defaultdict
        candidates = [
            step  # give the step
            for step, reqs in preconds.items()  # tuple unpacking
            if not reqs  # if there are no prior requirements ie. value of said key is an empty list
        ]
        next_item = min(candidates)
        final_order.append(next_item)

        # now remove the next_item as a requirement for all other steps
        for reqs in preconds.values():
            if next_item in reqs:
                reqs.remove(next_item)

        # remove next_item as a key from the defaultdict
        del preconds[next_item]

    return "".join(final_order)

