from solve import parse_record


def test_parse_1_string():
    string_input = "[1518-11-01 00:00] Guard #10 begins shift"
    assert parse_record(string_input) == (
        datetime.datetime(1518, 11, 1, 0, 0),
        "Guard #10 begins shift",
    )

