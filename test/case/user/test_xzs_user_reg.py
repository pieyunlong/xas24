import json
import unittest,requests,ddt
from lib.xlsx import *
from lib.db import *
from config.config import *


@ddt.ddt()
class TestCase(unittest.TestCase):
    a = xlrd_deom()
    @classmethod
    def setUpClass(cls) -> None:
        cls.l = cls.a.xlrd_in(test_path,"test_user_reg")
    @ddt.data("test_ok","test_err1")
    def test_something(self,test_name):
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        dict_1 = json.loads(args)
        if dict_1["userName"] == "test":
            del_user(dict_1['userName'])
        a = requests.post(url=url, json=dict_1)
        self.assertEqual(list_1["expect_reps"], a.text)
        if dict_1["userName"] == "test":
            del_user(dict_1['userName'])


if __name__ == '__main__':
    unittest.main()
