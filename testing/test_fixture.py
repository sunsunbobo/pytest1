import pytest

#创建一个登录的fixture方法，yield关键字激活了fixture的teardown方法
#yield之前的操作相当于setup 之后的操作相当于teardown
#yield相当于return，如果想要return一些测试数据，可以放在yield后面返回
@pytest.fixture(autouse=True)
def login():
    print("登录操作")
    print("获取token")
    yield
    print("登出操作")


#测试用例1需要提前登录
def test_case1(login):
    print("测试用例1")


# 测试用例2不需要提前登录
def test_case2(connectDB):
    print("测试用例2")

#测试用例3需要提前登录
def test_case3(login):
    print("测试用例3")