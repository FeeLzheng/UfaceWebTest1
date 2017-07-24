import unittest
from testCase.loginPage import login
from selenium.webdriver import Remote
from selenium import webdriver
import readconfig
localReadConfig =readconfig.readconfig()
import time
from comm import common
import paramunittest
from  comm.Log import MyLog

login_xls = common.get_xls("userCase.xlsx", "login")
log = MyLog.get_log()
logger = log.get_logger()

@paramunittest.parametrized(*login_xls)
class Login(unittest.TestCase):
    def setParameters(self,case,email,password):
        self.email=email
        self.password=password
        self.case=case

    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.get(localReadConfig.get_HTTP("baseurl"))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        logger.info("开始."+self.case+"测试.")


    def tearDown(self):
        self.driver.quit()
        logger.info("结束."+self.case+"测试.")

    def test01(self):
        login(self.driver).login_username(self.email)
        login(self.driver).login_password(self.password)
        time.sleep(5)






if __name__=="__main__":
    unittest.main()