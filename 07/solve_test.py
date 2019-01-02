from solve import parse_instruction


def test_parse_one_line():
    line = "Step C must be finished before step F can begin."
    assert parse_instruction(line) == ("C", "F")

