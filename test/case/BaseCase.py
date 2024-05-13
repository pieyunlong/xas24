import unittest,requests,json,sys,ast
from config.config import *
from lib.xlsx import *
from lib.login_xzs_log import login_xzs
sys.path.append("../..")#统一将包的路径提升到项目目录下
class BaseCase(unittest.TestCase):
    r = xlrd_deom()
    @classmethod
    def setUpClass(cls):
        if cls.__name__ !="BaseCase":
            cls.data_list =cls.r.xlrd_in(test_path,cls.__name__)
    def get_case_data(self,case_name):
        return self.r.xlrd_get(self.data_list,case_name)
    def send_request(self,case_data):
        case_name = case_data.get("test_name")
        url = case_data.get("url")
        args = case_data.get("args")
        headers = case_data.get("headers")
        expect = case_data.get("expect_reps")
        method = case_data.get("method")
        data_type = case_data.get("data_type")
        if method.upper() == "GET":
            res = requests.get(url=url,params=args)
        elif data_type.upper() == "FORM":
            args = json.loads(args)
            res = requests.post(url=url,json=args)
            login_xzs(case_name,url,args,expect,res.text)
            self.assertIn(expect,res.text)
        elif data_type.upper() == "JSON":
            args = json.loads(args)
            res = requests.post(url=url, json=args,headers=headers)
            login_xzs(case_name, url, args, expect, res.json())
            self.assertIn(expect,res.text)
if __name__ == '__main__':
    unittest.main()
