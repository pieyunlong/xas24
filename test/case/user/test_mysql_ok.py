import unittest,requests
from lib.db import *
from lib.login_xzs_log import login_xzs
name = "test001"
notname = "test"

class TestCase(unittest.TestCase):
    url = "http://127.0.0.1:8000/api/student/user/register"
    def test_mysql_ok(self):
        """regok:正常注册"""
        if check_user(notname):
            del_user(notname)
        data = {"userName":notname,"password":"123456","userLevel":1}
        a = requests.post(url = self.url,json=data)
        data1 = {"code":1,"message":"成功","response":None}
        # self.assertDictEqual(a.json(),data1)
        login_xzs(name, self.url, data, data1, a.json())
        self.assertTrue(check_user(notname))
        del_user(notname)
    def test_mysql_er(self):
        if  check_user(name):
            pass
        else:
            add_user(name,"123456")
        data = {"userName":name,"password":"123456","userLevel":1}
        a = requests.post(url = self.url,json=data)
        data1 = {"code":2,"message":"用户已存在","response":None}
        login_xzs(name, self.url, data, data1, a.json())
        self.assertDictEqual(a.json(),data1)

if __name__ == '__main__':
    unittest.main()
