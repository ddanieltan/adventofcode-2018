#%%
import numpy as np
import collections
import re


def parse_claim(string_input):
    """
    Input: string claim
    Output: defaultdict with parameters, each in int
    
    A claim like #123 @ 3,2: 5x4 
    means that claim ID 123 
    specifies a rectangle 3 inches from the left edge, 
    2 inches from the top edge, 
    5 inches wide, and 
    4 inches tall.
    
    """
    regex = r"(#)(\d+)( @ )(\d+)(,)(\d+)(: )(\d+)(x)(\d+)"
    matched = re.search(regex, string_input)

    d = collections.defaultdict(int)
    if matched:
        d["claim_id"] = int(matched.group(2))
        d["from_the_left"] = int(matched.group(4))
        d["from_the_top"] = int(matched.group(6))
        d["width"] = int(matched.group(8))
        d["height"] = int(matched.group(10))

    return d


#%%
canvas = np.zeros((10, 10), dtype=np.int)

c = parse_claim("#1 @ 1,3: 4x4")
print(c)
# claim=canvas[c[3]:c[3]+c[5],c[1]:c[1]+c[4]]
# print(claims)
