from conftest import setup_data

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 5 - 3 != 2

def test_basic_assertions():
    
    assert 'hello' == 'hello'

    assert 'hello' != 'hello'

    assert 'a' in 'abc'

    assert isinstance(42, int)

    assert True

    assert not False

def test_list_comparison():
    result = [1, 2, 3]
    expected = [1, 2, 4]
    assert result == expected

def test_fixture_example(setup_data):
    assert setup_data['name'] == 'John'
    