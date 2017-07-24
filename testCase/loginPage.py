import os
import  readconfig
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from comm.basePage import Page


class login(Page):

    login_username_loc = (By.NAME, "email")
    login_password_loc = (By.ID, "password")
    login_button_loc = (By.LINK_TEXT, "登录")

    # 输入用户登入
    def login_username(self, username):
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.login_password_loc).send_keys(password)


