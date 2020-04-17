import pytest

@pytest.fixture
def first_fixture():
    print("print from first_fixture")

@pytest.fixture
def fixture_return_numbers():
    list_03 = [10, 20, 30]
    return list_03

@pytest.fixture
def fixtures_set_return_numbers():
    set_01 = {10, 20, 30}
    return set_01

@pytest.fixture
def fixtures_set_return_words():
    set_01 = {'rock', 'post-rock', 'punk-rock'}
    return set_01

# @pytest.fixture
# def fixture_dictionary():
#     dictionary_01 =