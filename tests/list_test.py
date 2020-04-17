import pytest


# list test 01 - count method
def test_list_compare_1():
    list_01 = [1, 1, 2, 2, 2]
    a = 3
    b = list_01.count(2)
    # print('b= ', b)
    # print('a= ', a)
    assert a == b


# list test 02 - append method
def test_list_compare_2():
    list_01 = [1, 2, 3, 4, 5]
    list_02 = [1, 2, 3, 4, 5]
    assert list_01 == list_02
    list_02.append(6)
    # print('list_01= ', list_01)
    # print('list_02= ', list_02)
    assert list_01 != list_02


# list test 03 - clear method
def test_list_compare_3():
    list_01 = []
    list_02 = [1, 2, 3, 4, 5]
    list_02.clear()
    # print('list_02 will be printed= ')
    # print(list_02)
    assert list_01 == list_02


# list test 04 - reverse method
def test_list_compare_4():
    list_01 = ['first', 'second', 'third']
    list_02 = ['first', 'second', 'third']
    assert list_01 == list_02
    list_02.reverse()
    assert list_01 != list_02


# list test 05 - with parameters 1
def test_list_compare_5(fixture_return_numbers):
    list_01 = [10, 20, 30]
    assert fixture_return_numbers == list_01
