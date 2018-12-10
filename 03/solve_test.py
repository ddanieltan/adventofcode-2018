from solve import parse_claim, create_shape_coordinates


def test_parse_claim1():
    test_input = "#123 @ 3,2: 5x4"
    assert parse_claim(test_input) == (123, 3, 2, 5, 4)


def test_parse_claim2():
    test_input = "#1 @ 1,3: 4x4"
    assert parse_claim(test_input) == (1, 1, 3, 4, 4)


def test_create_shape_coordinates():
    test_input = (1, 1, 3, 4, 4)
    length_of_canvas = 8
    answer = sorted(
        [
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (2, 3),
            (3, 3),
            (4, 3),
            (5, 3),
            (2, 4),
            (3, 4),
            (4, 4),
            (5, 4),
            (2, 5),
            (3, 5),
            (4, 5),
            (5, 5),
        ]
    )
    assert create_shape_coordinates(test_input, length_of_canvas) == answer

