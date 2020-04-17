import pytest

# string test 01 - capitalize method
def test_string_01(fixture_string):
    capitalized = 'My name is Boris'
    assert capitalized == fixture_string.capitalize()

# string test 02 - lower method
def test_string_02(fixture_string):
    lower = 'my name is boris'
    assert lower == fixture_string.lower()

# string test 03 - upper method
def test_string_03(fixture_string):
    upper = 'MY NAME IS BORIS'
    assert upper == fixture_string.upper()

# string test 04 - title method
def test_string_04(fixture_string):
    title = 'My Name Is Boris'
    assert title == fixture_string.title()

# string test 05 - swapcase method
def test_string_05(fixture_string):
    swapcase = 'MY NAME IS bORIS'
    assert swapcase == fixture_string.swapcase()
