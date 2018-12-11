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
#%%
length_of_canvas = 1000
canvas = np.zeros((length_of_canvas, length_of_canvas), dtype=np.int)
with open("input.txt", "r") as f:
    data = f.read().splitlines()
    for d in data:
        c = parse_claim(d)
        canvas[
            c.get("from_the_top") : c.get("from_the_top") + c.get("height"),
            c.get("from_the_left") : c.get("from_the_left") + c.get("width"),
        ] += 1

    output1 = np.sum(np.where(canvas > 1, 1, 0))
    print(f"Ans for part1: {output1}")

for line in open("input.txt", "r"):  # interesting alternative to `with open()`
    c = parse_claim(line)
    if np.all(
        canvas[
            c.get("from_the_top") : c.get("from_the_top") + c.get("height"),
            c.get("from_the_left") : c.get("from_the_left") + c.get("width"),
        ]
        == 1
    ):
        output2 = c.get("claim_id")
        print(f"Ans for part 2: {output2}")

