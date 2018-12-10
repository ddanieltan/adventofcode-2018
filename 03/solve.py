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


def create_shape_coordinates(tuple_input, length_of_canvas):
    """
    Input: parsed claims(tuple), length of canvas
    Output: array of coordinates representing the shape of the claim
    
    """

    claim_id, from_the_left, from_the_top, width, height = tuple_input
    coordinates = []

    shape_bottom_left_corner = (
        from_the_left + 1,
        length_of_canvas - from_the_top - height + 1,
    )

    for y in range(shape_bottom_left_corner[1], length_of_canvas - from_the_top + 1, 1):

        for x in range(
            shape_bottom_left_corner[0], shape_bottom_left_corner[0] + width, 1
        ):
            coordinates.append((x, y))

    return sorted(coordinates)


#%%
test = "#123 @ 3,2: 5x4"
tuple_input = parse_claim(test)
create_shape_coordinates(tuple_input, 10)

#%%
create_shape_coordinates((1, 1, 3, 4, 4), 8)
