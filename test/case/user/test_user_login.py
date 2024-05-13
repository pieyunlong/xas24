import json
import unittest,requests
from lib.xlsx import *
from config.config import *

class TestCase(unittest.TestCase):
    a = xlrd_deom()
    @classmethod
    def setUpClass(cls) -> None:
        cls.l = cls.a.xlrd_in(test_path,"test_user_login")
    def test_ok(self):
        test_name = "test_ok"
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        print(args)
        dict_1 = json.loads(args)
        a = requests.post(url=url, json=dict_1)
        self.assertIn(list_1["expect_reps"], a.text)
    def test_err1(self):
        test_name = "test_err1"
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        print(args)
        dict_1 = json.loads(args)
        a = requests.post(url=url, json=dict_1)
        self.assertIn(list_1["expect_reps"], a.text)
    def test_err2(self):
        test_name = "test_err2"
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        print(args)
        dict_1 = json.loads(args)
        a = requests.post(url=url, json=dict_1)
        self.assertIn(list_1["expect_reps"], a.text)
    def test_err3(self):
        test_name = "test_err3"
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        print(args)
        dict_1 = json.loads(args)
        a = requests.post(url=url, json=dict_1)
        self.assertIn(list_1["expect_reps"], a.text)
if __name__ == '__main__':
    unittest.main()