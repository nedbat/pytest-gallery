class TestBase:
    def setup_method(self):
        print("setup_method base")

    def teardown_method(self):
        print("teardown_method base")


class TestClass(TestBase):

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup_method(self):
        super().setup_method()
        print("setup_method")

    def teardown_method(self):
        print("teardown_method")
        super().teardown_method()

    def test_method1(self):
        assert 1 == 1

    def test_method2(self):
        assert 2 == 2

    def test_method3(self):
        assert 3 == 3
