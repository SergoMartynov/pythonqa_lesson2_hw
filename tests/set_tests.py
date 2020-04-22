import pytest


# set test 01 - compare a length of the set
def test_set_01(fixtures_set_return_numbers):
    b = len(fixtures_set_return_numbers)
    a = 3
    print('\n==============================')
    print('this is a = ', a)
    print('this is b = ', b)
    assert b == a


# set test 02 - test for clear method
def test_set_02(fixtures_set_return_words):
    empty_set_01 = set()
    fixtures_set_return_words.clear()
    print('\n==============================')
    print('this is empty_set_01 = ', empty_set_01)
    print('this is empty_set_02 = ', fixtures_set_return_words)
    assert empty_set_01 == fixtures_set_return_words


# set test 03 - test for difference method
def test_set_03(fixtures_set_return_words):
    set_02 = {'rock', 'post-rock', 'punk-rock', 'metal'}
    metal = set_02.difference(fixtures_set_return_words)
    print('\n==============================')
    print('the diff is = ', metal)
    assert metal == {'metal'}


# set test 04 - test for remove method
def test_set_04(fixtures_set_return_words):
    fixtures_set_return_words.remove('punk-rock')
    no_punk = {'rock', 'post-rock'}
    print('\n==============================')
    print('this is fixtures_set_return_words = ', fixtures_set_return_words)
    print('this is no_punk = ', no_punk)
    assert no_punk == fixtures_set_return_words


# set test 05 - test add method
def test_set_05(fixtures_set_return_numbers):
    fixtures_set_return_numbers.add(0)
    set_02 = {0, 10, 20, 30}
    print('\n==============================')
    print('this is fixtures_set_return_numbers = ', fixtures_set_return_numbers)
    print('this is set_02 = ', set_02)
    assert set_02 == fixtures_set_return_numbers
