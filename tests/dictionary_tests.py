import pytest


# dictionary test 01 - clear method
def test_dictionary_01(fixture_dictionary):
    fixture_dictionary.clear()
    assert fixture_dictionary == {}


# dictionary test 02 - copy method
def test_dictionary_02(fixture_dictionary):
    copy_car = fixture_dictionary.copy()
    print('\n==============================')
    print('copy_car = ', copy_car)
    assert fixture_dictionary == copy_car


# dictionary test 03 - update method
def test_dictionary_03(fixture_dictionary):
    fixture_dictionary.update({'colour': 'Red'})
    print('\n==============================')
    print('dictionary with colour: Red = ', fixture_dictionary)
    assert 'colour' in fixture_dictionary


# dictionary test 04 - get method
def test_dictionary_04(fixture_dictionary):
    model = fixture_dictionary.get('model')
    year = fixture_dictionary.get('year')
    print('\n==============================')
    print('model = ', model)
    print('year = ', year)
    assert year == 1964, model == 'Mustang'


# dictionary test 05 - values method
def test_dictionary_05(fixture_dictionary):
    values = fixture_dictionary.values()
    print('\n==============================')
    print('values = ', values)
    assert 'Ford' in values, 'Mustang' in values
