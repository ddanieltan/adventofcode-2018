#%%
import re
import datetime

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
# string_input = "[1518-11-01 00:00] Guard #10 begins shift"
# parse_record(string_input)
# #%%
# a = datetime.strptime("1518-11-02 10:05", "%Y-%m-%d %H:%M")
# b = datetime.strptime("1518-11-01 10:05", "%Y-%m-%d %H:%M")
# print(sorted([a, b]))

