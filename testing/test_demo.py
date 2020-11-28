import pytest


def test_a():
    print("test_demo.py 测试用例1")

def test_c():
    assert 1 == 2

def test_b():
    print("test_demo.py 测试用例2")

def test_c1():
    assert 1 == 2

def test_b1():
    print("test_demo.py 测试用例2")

@pytest.mark.parametrize('a',[1,2,3])
@pytest.mark.parametrize('b',[4,5,6])
def test_para(a,b):
    print(f'a={a},b={b}')
