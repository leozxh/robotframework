#用Python写Robot Framework测试
from robot.api import TestSuite
from robot.api import ResultWriter
from robot.model import Keyword


class CxmCaiWuTest:

    def __init__(self, name, librarys=["SeleniumLibrary"]):
        # 创建测试套件
        self.suite = TestSuite(name)

        # 导入SeleniumLibrary
        for lib in librarys:
            self.suite.resource.imports.library(lib)

    # 定义变量
    def create_variables(self):
        variables = {
            "${url}": "http://test.mmp-new.caixm.cn/",
            "${browser}": "Chrome",
            "${username_type}": "id=userName",
            "${password_type}": "id=password",
            "${loginBtn}": 'xpath=//*[@id="root"]/div/div[2]/div[2]/div/form/div[3]/div/div/span/button'

        }
        for k, v in variables.items():
            self.suite.resource.variables.create(k, v)

    # 测试用例：启动浏览器
    def open_browsers(self):
        test_01 = self.suite.tests.create("启动浏览器")
        test_01.keywords.create("Open Browser",
            args=["${url}", "${browser}"])
        test_01.keywords.create("Title Should Be",
            args=["菜小秘"])

    # 测试用例：输入账号和密码，登录财务端
    def et_word(self):
        test_02 = self.suite.tests.create("登录财务端")
        test_02.keywords.create("Sleep", args=["5s"])
        test_02.keywords.create("Input Text",
            args=["${username_type}", "15868134428"])
        test_02.keywords.create("Input Text",
            args=["${password_type}", "232323"])
        test_02.keywords.create("Click Button",
            args=["${loginBtn}"])
        test_02.keywords.create("Sleep", args=["5s"])

    # 测试用例：断言验证登录之后标题
    def assert_title(self):
        test_03 = self.suite.tests.create("断言验证登录之后标题")
        test_03.keywords.create("Title Should Be",
                                args=["工作台 - 菜小秘"])

    # 测试用例：关闭测试用例
    def close_browsers(self):
        test_04 = self.suite.tests.create("关闭浏览器")
        test_04.keywords.create("Close All Browsers")


        # 运行
    def run(self):
        self.create_variables()
        self.open_browsers()
        self.et_word()
        self.assert_title()
        self.close_browsers()

        # 运行套件
        result = self.suite.run(critical="菜小秘财务端",
            output="../reports/output.xml")

        # 生成日志、报告文件
        ResultWriter(result).write_results(
            report="../reports/report.html", log="../reports/log.html")

if __name__ == "__main__":
    suite = CxmCaiWuTest("菜小秘财务端测试套件")
    suite.run()