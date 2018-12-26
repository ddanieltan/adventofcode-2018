from solve import calc_reaction


def test_aA():
    assert calc_reaction("aA") == ""


def test_abBa():
    assert calc_reaction("abBa") == "aa"


def test_abAB():
    assert calc_reaction("abAB") == "abAB"


def test_aabAAB():
    assert calc_reaction("aabAAB") == "aabAAB"

