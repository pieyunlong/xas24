import unittest

def setUpModule():
    print("stupmodule")
#     每次执行类前执行一次
def tearDownModule():
    print("tearDownModule")
#     每次执行类后执行一起
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")
    #     每次调用前执行一次 但只会执行一次
    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")
    # 每次调用后执行一次 但只会执行一次
    def setUp(self) -> None:
        print("setup")
    #     每次调用方法前都会执行一次
    def tearDown(self) -> None:
        print("tearDown")
    #     每次调用方法后都会执行一次
    def test_01(self):
        # 判断两个是知否相同
        self.assertEqual("a","a")
    def test_02(self):
        # 判断h是否在html里 a是否在b里
        self.assertIn("h","html")
    # def test_03(self):
    #     # 判断两个值是否相等（地址是否相等）
    #     self.assertIs(1*1,1/1)
    def test_03(self):
        # 判断两个值是否相等（地址是否相等）
        self.assertIsNot(1*1,1/1)
    def test_04(self):
        # 判断a是否大于b
        self.assertLess(1,2)
if __name__ == '__main__':
    unittest.main()
