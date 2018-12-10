#%%
import re
import itertools


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


#%%
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
def overlap(coordinates1, coordinates2):
    """
    Input: 2 array of coordinates
    Output: array of overlapping coordinates
    """
    c1 = set(coordinates1)
    c2 = set(coordinates2)
    overlapping_coordinates = list(c1.intersection(c2))

    return sorted(overlapping_coordinates)


#%%
def handle_claims(list_of_claims, length_of_canvas):
    combinations = itertools.combinations(list_of_claims, 2)
    overlapping_coordinates = []
    for c in combinations:
        claim_a = c[0]
        claim_b = c[1]

        parsed_a = parse_claim(claim_a)
        parsed_b = parse_claim(claim_b)

        coord_a = create_shape_coordinates(parsed_a, length_of_canvas)
        coord_b = create_shape_coordinates(parsed_b, length_of_canvas)
        output = overlap(coord_a, coord_b)
        if output != []:
            overlapping_coordinates += output

    # return overlapping_coordinates
    return len(overlapping_coordinates)


#%%
test = "#123 @ 3,2: 5x4"
tuple_input = parse_claim(test)
create_shape_coordinates(tuple_input, 10)

#%%
aa = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
handle_claims(aa, 8)
