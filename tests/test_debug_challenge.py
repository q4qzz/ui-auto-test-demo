# -*- coding: utf-8 -*-
"""调试挑战：我在这个文件里埋了 3 个 bug。

【你的任务】
一次修一个，直到它变成绿色。

【怎么调试——这是通用方法，以后所有的 bug 都这么找】
  1. 先看报错的【最后一行】，那里写着异常类型：
       NoSuchElementException  -> 找不到元素，定位器写错了
       AssertionError          -> 元素找到了，但值不对
  2. 再看报错的【行号】，它精确告诉你是哪一行出的问题
  3. 打开那一行，问自己：
       - 我找的元素，页面上真的有吗？
       - 我比较的两个值，类型一样吗？（字符串 "1" 不等于数字 1）

【把这 3 个 bug 全修好，你对 Selenium 报错的理解会超过大部分人】
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = "https://www.saucedemo.com"


def test_debug_challenge(driver):
    """走一遍「登录 -> 加购 -> 检查角标」的流程，但代码里有 3 个 bug。"""

    driver.get(BASE_URL)

    # ============ 第 1 段：登录 ============
    driver.find_element(By.ID,"user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory"))

    # ============ 第 2 段：还没加购，页面上不应该有购物车角标 ============
    badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert badges == [] , "还没加购，不应该出现购物车角标"

    # ============ 第 3 段：加 1 件商品，角标应该变成 1 ============
    add_buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    add_buttons[0].click()

    badge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert badge.text == '1', f"角标应该显示 1，实际显示 {badge.text!r}"
