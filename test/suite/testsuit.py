import unittest
from test.case.user.test_mysql_ok import TestCase
class MyTestCase1(unittest.TestCase):
    def test_suit(self):
        suit=unittest.TestSuite()
        suit.addTest(TestCase("test_mysql_ok"))
        # suit.addTests([m('test_mysql_ok'),m('test_mysql_er')])
        # 文本测试报告
        with open("result.txt","w") as f:
            unittest.TextTestRunner(stream=f,verbosity=2).run(suit)
        # unittest.TextTestRunner(verbosity=2).run(suit)
    # def test_makesuit(self):
    #     suit1=unittest.makeSuite(MyTestCase)
    #     unittest.TextTestRunner(verbosity=2).run(suit1)
    # def test_loder(self):
        # suit2=unittest.TestLoader().loadTestsFromTestCase(m)
        # unittest.TextTestRunner(verbosity=2).run(suit2)
    # def test_discover(self):
    #     suit3=unittest.defaultTestLoader.discover("./")
    #     unittest.TextTestRunner(verbosity=2).run(suit3)
if __name__ == '__main__':
    unittest.main()