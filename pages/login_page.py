# -*- coding: utf-8 -*-
"""登录页的页面对象（Page Object）。

【这个文件只干三件事】
  1. 记录页面上的元素在哪里（定位器）
  2. 提供"怎么操作这个页面"的方法（输入、点击）
  3. 提供"怎么读取这个页面的状态"的方法（错误提示是什么）

【它绝对不做的事】
  不做断言，不管对错。判断对错是 tests/ 的事。

【为什么这样分？】
网站改版时——比如登录按钮的 id 从 login-button 改成了 btn-login——
你只需要改这个文件里的【一行】，所有用例自动跟着生效。
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    """saucedemo 登录页。"""

    URL = "https://www.saucedemo.com"

    # ---------- 元素定位器 ----------
    # 集中放在最上面，一眼就能看全这个页面有哪些元素
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ---------- 操作：让页面发生什么 ----------

    def open(self):
        """打开登录页，并等它真正加载出来。"""
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        return self

    def enter_username(self, username):
        """在用户名框里输入（先清空，避免残留）。"""
        box = self.driver.find_element(*self.USERNAME_INPUT)
        box.clear()
        box.send_keys(username)
        return self

    def enter_password(self, password):
        """在密码框里输入。"""
        box = self.driver.find_element(*self.PASSWORD_INPUT)
        box.clear()
        box.send_keys(password)
        return self

    def click_login(self):
        """点击登录按钮。"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username, password):
        """一步完成登录。返回 self 是为了能链式调用。"""
        return self.enter_username(username).enter_password(password).click_login()

    # ---------- 查询：读取页面当前的状态 ----------

    def error_text(self):
        """返回错误提示文字；如果页面上没有错误提示，返回空字符串。"""
        elements = self.driver.find_elements(*self.ERROR_MESSAGE)
        return elements[0].text if elements else ""

    def has_error(self):
        """页面上是否显示了错误提示。"""
        return len(self.driver.find_elements(*self.ERROR_MESSAGE)) > 0

    @property
    def current_url(self):
        return self.driver.current_url
