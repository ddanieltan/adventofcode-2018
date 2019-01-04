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


#%%
def solve1():
    with open("07/input.txt") as f:
        lines = f.read()
    print(find_order(lines))


solve1()

#%%
time_taken = {}
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for idx, letter in enumerate(alphabet):
    time_taken[letter] = idx + 61
time_taken.get("B")

#%%
steps = "BFGKNRTWXIHPUMLQVZOYJACDSE"
time = 0
work_schedule = {}  # worker_id: (step, start, end)
workers_pool = set(range(3))
# use 1 worker

current_worker = workers_pool.pop()
next_step = steps[0]
time_required = time_taken.get(next_step)
work_schedule[current_worker] = (next_step, time, time + time_required)
steps = steps[1:]
time += 1

for worker_id, values in work_schedule.items():
    if (values[2]) == time:
        pass  #
# update work schedule
# worker_id=0, working on step C, start at 0 sec, end at 63

# time++
# each loop, check if end time is reached. add worker back to pool


#%%
steps = "BFGKNRTWXIHPUMLQVZOYJACDSE"
solve11 = solve11[1:]
solve11[0]

#%%

#%%
for time in range(10):
    steps = "BFGKNRTWXIHPUMLQVZOYJACDSE"
    work_schedule = {}  # worker_id: (step, start, end)
    workers_pool = set(range(3))

    current_worker = workers_pool.pop()
    next_step = steps[0]
    time_required = time_taken.get(next_step)
    # work_schedule[current_worker]=(next_step,time,time+time_required)
    work_schedule[current_worker] = (next_step, time, 3)

    steps = steps[1:]

    for worker_id, values in work_schedule.items():
        if (values[2]) == time:
            workers_pool.add(worker_id)
    print(work_schedule)
    time += 1

