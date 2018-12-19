#%%
import re
import datetime
from collections import defaultdict

#%%
def parse_record(string_input):
    """
    Input: String input eg. [1518-11-01 00:00] Guard #10 begins shift
    Output: defaultdict of all the important parameters
    """
    regex1 = r"\[(.+)\] (.+)"
    matched = re.search(regex1, string_input)

    time_string = matched.group(1)
    datetime_parser_pattern = (
        "%Y-%m-%d %H:%M"
    )  # https://www.tutorialspoint.com/python/time_strptime.htm
    date_object = datetime.datetime.strptime(time_string, datetime_parser_pattern)

    note_string = matched.group(2)

    return date_object, note_string


#%%
# Importing data
dictionary = {}
for line in open("input.txt", "r"):
    date_object, note_string = parse_record(line)
    dictionary[date_object] = note_string

#%%
workers_minutes_slept = defaultdict(list)

for key in sorted(dictionary.keys()):
    regex_guard = "Guard #(\d+) begins shift"
    note_string = dictionary[key]
    minute_value = int(key.minute)
    matched = re.search(regex_guard, note_string)
    if matched:
        current_guard = matched.group(1)
    elif note_string == "falls asleep":
        workers_minutes_slept[current_guard].append(minute_value)
    elif note_string == "wakes up":
        workers_minutes_slept[current_guard].append(minute_value)

# print(workers_minutes_slept)
#%%
def calculate_minutes_slept(guard_id, minutes_list):
    minutes_slept = []
    for a, b in zip(minutes_list[0::2], minutes_list[1::2]):
        minutes_slept.append(b - a)
    return guard_id, sum(minutes_slept)


#%%
for k in workers_minutes_slept:
    print(calculate_minutes_slept(k, workers_minutes_slept[k]))
# Part 1 ans = 421 * 495
print(421 * 495)

