
def test_w(connectDB):
    print("test")

class TestDemo:
    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self):
        print("测试用例b")

class TestDemo1:
    def test_c(self):
        print("测试用例c")

    def test_d(self, connectDB):
        print("测试用例d")