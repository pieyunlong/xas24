import sys
import pickle
import unittest
from lib import email_files
from lib.HTMLTestRunner import HTMLTestRunner
from config.config import *
from test.suite.test_suites import get_suite
# if __name__ == '__main__':
#     now=time.strftime("%Y_%m_%d_%H_%M_%S")
#     fe=open(report_file,'wb')
#     runner=HTMLTestRunner(
#         stream=fe,  # 相当于f.write(报告)
#         title='xzs测试报告',
#         description='xzs测试报告',
#         verbosity=2  # 为每个测试用例生成测试报告
#     )
#     suit=unittest.defaultTestLoader.discover(os.getcwd(),'tes*.py')
#     runner.run(suit)
#     fe.close()
#     email_files.send_email(report_file)
def discover():
    return unittest.defaultTestLoader.discover(test_case_path)
    # unittest.defaultTestLoader.discover(os.getcwd(), 'tes*.py')
def run(suite):
    logging.info("=====测试开始======")
    with open(report_file,"wb") as f:
        resule = HTMLTestRunner(
                stream=f,  # 相当于f.write(报告)
                title='xzs测试报告',
                description='xzs测试报告',
                verbosity=2  # 为每个测试用例生成测试报告
            ).run(suite)
        print(resule)
        if resule.failures:
            save_failures(resule,test_last_fails)
    logging.info("=====测试结束=====")
    if send_email_enable:
        email_files.send_email(report_file)
        logging.info("*******邮箱发送成功*******")
def run_all():
    run(discover())
def run_suite(suite_name):
    suite = get_suite(suite_name)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print("不存在")
def collect():
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases() != 0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTest(tests)
    _collect(discover())
    return suite
def collect_only():
    t0 = time.time()
    i = 0
    for case in collect():
        i += 1
        print("{}.{}".format(str(i),case.id()))
    print("------------------------------")
    print("collect {} test is {:.3f}s".format(str(i),time.time() - t0))
def textlist(textfile):
    with open(textfile,"r") as f:
        suit_list = f.readlines()
    suit_list = [x.strip() for x in suit_list if not x.startswith("#")]
    suit = unittest.TestSuite()
    all_suit = collect()
    for case in all_suit:
        if case.id().split(".")[-1] in suit_list:
            suit.addTest(case)
    return suit
def get(get):
    suit = unittest.TestSuite()
    all_suit = collect()
    for case in all_suit:
        if case._testMethodDoc and get in case._testMethodDoc:
            suit.addTest(case)
    return suit
def save_failures(result,file):
    suite = unittest.TestSuite()
    print(result.failures)
    for case_result in result.failures:
        print(case_result)
        suite.addTest(case_result[0])
    with open(file,"wb") as f:
        pickle.dump(suite,f)
def rerun_fails():
    sys.path.append(test_last_fails)
    with open(test_last_fails,"rb") as f:
        suite = pickle.load(f)
    run(suite)
def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.get:
        run(get(options.get))
    else:
        run_all()
if __name__ == '__main__':
    # run_all()
    # run_suite("smoke_suite")
    # collect_only()
    # run(get("regok"))
    # print(textlist(testlist_path))
    # run(textlist(testlist_path))
    # rerun_fails()
    # main()
    pass