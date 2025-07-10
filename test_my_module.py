from my_module import add, subtract

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(0,0) == 0
    assert add(40,40) == 80


def test_subtract():
    assert subtract(5,2) == 3
    assert subtract(10,10) == 0
    assert subtract(0,5) == -5


