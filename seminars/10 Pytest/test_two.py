import pytest

def a_test_good_array_comparing():
    assert (1,2,3) == (1,0,3)
    assert True

@pytest.mark.parametrize("arg1, arg2", [(2, "lol"), (4, "kek")])
def test_something_new(arg1, arg2):
    assert arg1 in [3, 4]
    assert arg2 in ["lol", "kek"]