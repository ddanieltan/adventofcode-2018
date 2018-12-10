from solve import parse_claim


def test_parse_claim1():
    test_input = "#123 @ 3,2: 5x4"
    assert parse_claim(test_input) == (123, 3, 2, 5, 4)


def test_parse_claim2():
    test_input = "#1 @ 1,3: 4x4"
    assert parse_claim(test_input) == (1, 1, 3, 4, 4)

