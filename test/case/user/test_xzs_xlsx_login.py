import json
from config.config import *
import unittest,requests,ddt
from lib.xlsx import *
from lib.login_xzs_log import login_xzs
def readExceldDate(filename):
    book = xlrd.open_workbook(filename)
    sheet1 = book.sheet_by_index(1)
    rows = sheet1.nrows
    datalist = []
    for i in range(1,rows):
        datalist.append(sheet1.row_values(i)[0])
        a1 = sheet1.row_values(i)[0]
    return datalist
@ddt.ddt()
class TestCase(unittest.TestCase):
    a = xlrd_deom()
    name = test_path
    name_sheet = "test_user_login"
    @classmethod
    def setUpClass(cls):
        cls.l = cls.a.xlrd_in(cls.name,cls.name_sheet)
    @ddt.data(*readExceldDate(test_path))
    def test_some(self,test_name):
        list_1 = self.a.xlrd_get(self.l, test_name)
        url = list_1["url"]
        args = list_1["args"]
        print(args)
        args = json.loads(args)
        expect_res = list_1["expect_reps"]
        res_text = requests.post(url=url, json=args)
        login_xzs(test_name,url,args,expect_res,res_text.text)
        self.assertIn(expect_res, res_text.text)
if __name__ == '__main__':
    unittest.main()