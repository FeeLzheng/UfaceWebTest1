import os
import webbrowser
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):

    def __init__(self,driver,url=""):
        self.driver=driver
        self.url=url


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print
            u"%s 页面中未能找到 %s 元素" % (self, loc)


    def send_key(self,*loc,value):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            print
            u"%s 页面中未能找到 %s 元素" % (self, loc)

    def _open(self, url):

    # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()

