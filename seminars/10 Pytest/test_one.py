import pytest

print('HELLO')
CONSTA = 69

def for_mock():
    return 69

@pytest.fixture()
def test_fixture():
    print('SETUP')
    yield 'It is fixture '
    print('TEARDOWN')

def a_test_good_array_comparing(test_fixture):
    print(test_fixture)
    assert (1,2,3) == (1,2,3)
    assert False

def wrong_func():
    raise ValueError()
    
def test_mock(mocker):
    print(for_mock())
    mocker.patch("test_one.for_mock", return_value=1000)
    print(for_mock())
    #print(wrong_func())
    #assert False


