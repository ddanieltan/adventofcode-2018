#%%
import collections
import re

guards = collections.defaultdict(list)
times = collections.defaultdict(int)

#%%
for line in sorted(open("input.txt")):
    regex_main_pattern = "\[.+:(\d\d)] (.+)"
    matched = re.search(regex_main_pattern, line)

    minute = int(matched.group(1))
    action = matched.group(2)

    if action.startswith("Guard"):
        regex_guard_pattern = "Guard #(\d+) begins shift"
        guard_matched = re.search(regex_guard_pattern, action)
        guard_id = int(guard_matched.group(1))
    elif action == "falls asleep":
        start = minute
    elif action == "wakes up":
        end = minute
        guards[guard_id].append((start, end))
        times[guard_id] += end - start

#%%
(guard, time) = max(times.items(), key=lambda i: i[1])
print(guard, time)  # same ans as I got previously


# What minute does that guard spend asleep the most?
# I didn't realise this was the minute portion of the question...

#%%
(minute, count) = max(
    [
        (minute, sum(1 for start, end in guards[guard] if start <= minute < end))
        for minute in range(60)
    ],
    key=lambda i: i[1],
)

print("part 1:", guard * minute)

#%%
(guard, minute, count) = max(
    [
        (guard, minute, sum(1 for start, end in guards[guard] if start <= minute < end))
        for minute in range(60)
        for guard in guards
    ],
    key=lambda i: i[2],
)

print("part 2:", guard * minute)
