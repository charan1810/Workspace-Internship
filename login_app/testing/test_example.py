def test_equal_or_not():
    assert 3==3

def test_greater_or_not():
    assert 3>=2
    
def test_lesser_or_not():
    assert 2<=15

def test_not_equal_or_not():
    assert 3!=2

def test_is_instance():
    assert isinstance('this is a string',str)
    assert not isinstance('10',int)
    