from solve import *


def test_aA():
    assert calc_reaction("aA") == ""


def test_abBa():
    assert calc_reaction("aA") == ""


def test_abAB():
    assert calc_reaction("abAB") == "abAB"


def test_aabAAB():
    assert calc_reaction("aabAAB") == "aabAAB"
