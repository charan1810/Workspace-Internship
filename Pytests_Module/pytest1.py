def test_equal_or_not_equal():
    assert 3==3
    assert 3!=2
 
def test_is_instance():
    assert isinstance("This is a string",str)
    assert not isinstance("10",int)