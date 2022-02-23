import pytest



def test_hello():
    assert False, "This should fail"

def test_hello2(sample_fixture):
    assert sample_fixture=='a', "This should pass"
