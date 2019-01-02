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
raw = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""


def preconditions(lines):
    preconditions = defaultdict(list)
    for line in lines.splitlines():
        before, after = parse_instruction(line)
        preconditions[after].append(before)
    return preconditions


def find_order(lines):
    preconds = preconditions(lines)

    while preconds:
        candidates = []
