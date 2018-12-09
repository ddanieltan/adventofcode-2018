#%%
import re


def parse_claim(string_input):
    """
    Input: string claim
    Output: tuple with parameters, each in int
    
    A claim like #123 @ 3,2: 5x4 
    means that claim ID 123 
    specifies a rectangle 3 inches from the left edge, 
    2 inches from the top edge, 
    5 inches wide, and 
    4 inches tall.
    
    """
    regex = r"(#)(\d+)( @ )(\d+)(,)(\d+)(: )(\d+)(x)(\d+)"
    matched = re.search(regex, string_input)
    if matched:
        claim_id = int(matched.group(2))
        from_the_left = int(matched.group(4))
        from_the_top = int(matched.group(6))
        width = int(matched.group(8))
        height = int(matched.group(10))

    return claim_id, from_the_left, from_the_top, width, height


def create_shape_coordinates(tuple_input):
    claim_id, from_the_left, from_the_top, width, height = tuple_input


#%%
test = "#123 @ 3,2: 5x4"
parse_claim(test)
