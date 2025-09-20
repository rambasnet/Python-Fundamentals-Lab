"""Module to test fuitful functions in litagreining.py module.
"""

from litagreining import classify


def test_classify_raudur() -> None:
    """Function to test for radur cases.
    """
    assert classify(200, 20, 25) == "raudur"
    assert classify(100, 0, 0) == "raudur"
    assert classify(10, 5, 6) == "raudur"


def test_classify_svartur() -> None:
    """Function to test for svartur cases.
    """
    assert classify(0, 0, 0) == "svartur"


# r == g > b -> yellow
def test_classify_gulur() -> None:
    """Function to test for fulur
    """
    assert classify(200, 200, 100) == "gulur"
    assert classify(100, 100, 50) == "gulur"


# FIXME 1: Write a test function with at least 1 test case for grar
# FIXME 2: Write a test function with at least 1 test case for blangraenn
# FIXME 3: Write a test function with at least 1 test case for hvitur
# FIXME 4: Write a test function with at least 1 test case for graenn
# FIXME 5: Write a test function with at least 1 test case for blar
# FIXME 6: Write a test function with at least 1 test case for gulur
# FIXME 7: Write a test function with at least 1 test case for othekkt
# FIXME 8: Write a test function with at least 1 test case for fjolubleikur
# FIXME 9: Write a test function with at least 1 test case for blagraenn
