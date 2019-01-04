from solve import parse_instruction, find_order


def test_parse_one_line():
    line = "Step C must be finished before step F can begin."
    assert parse_instruction(line) == ("C", "F")


def test_find_order():
    raw = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""
    assert find_order(raw) == "CABDFE"

