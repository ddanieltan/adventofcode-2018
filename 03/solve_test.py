from solve import parse_claim, create_shape_coordinates, overlap, handle_claims


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


def test_overlap1():
    a1 = [(1, 1), (1, 2), (2, 1), (2, 2)]
    a2 = [(2, 2), (3, 2), (2, 3), (3, 3)]
    assert overlap(a1, a2) == [(2, 2)]


def test_overlap2():
    a1 = create_shape_coordinates(parse_claim("#1 @ 1,3: 4x4"), 8)
    a2 = create_shape_coordinates(parse_claim("#2 @ 3,1: 4x4"), 8)
    assert overlap(a1, a2) == sorted([(4, 4), (5, 4), (4, 5), (5, 5)])


def test_no_overlap():
    a1 = create_shape_coordinates(parse_claim("#1 @ 1,3: 4x4"), 8)
    a2 = create_shape_coordinates(parse_claim("#3 @ 5,5: 2x2"), 8)
    assert overlap(a1, a2) == list()


def test_handle_claims():
    aa = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
    assert handle_claims(aa, 8) == 4

