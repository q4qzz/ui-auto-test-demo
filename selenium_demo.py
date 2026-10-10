# -*- coding: utf-8 -*-
"""Day 2 演示：让浏览器自己登录 saucedemo。

【这个脚本会做什么】
  1. 自动打开一个 Edge 浏览器窗口
  2. 自己打开 https://www.saucedemo.com
  3. 自己在用户名框里打字
  4. 自己在密码框里打字
  5. 自己点击 Login 按钮
  6. 检查是否登录成功、商品有几个
  7. 停 5 秒让你看清楚，然后关闭浏览器

【你要做的事】
  双击 run_demo.bat，然后【盯着屏幕看】。
  你会看到浏览器自己动起来——这就是自动化。
"""

import os
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

# 独立的浏览器配置目录，不干扰你日常使用的 Edge
profile = Path(__file__).parent / ".edge-profile"
profile.mkdir(exist_ok=True)

options = Options()
options.add_argument(f"--user-data-dir={profile}")
options.add_argument("--window-size=1280,900")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
# 以下几个参数是为了在受限环境（例如 CI 服务器）里也能正常启动浏览器
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")

# 设了 HEADLESS=1 就不显示窗口（用于验证）
if os.environ.get("HEADLESS") == "1":
    options.add_argument("--headless=new")

print("=" * 55)
print("第 1 步：启动浏览器")
print("=" * 55)
driver = webdriver.Edge(options=options)
print("浏览器已启动，版本:", driver.capabilities.get("browserVersion"))

try:
    print()
    print("=" * 55)
    print("第 2 步：打开网站")
    print("=" * 55)
    driver.get(URL)
    print("  当前地址:", driver.current_url)
    print("  页面标题:", driver.title)
    time.sleep(1)

    print()
    print("=" * 55)
    print("第 3 步：定位页面元素")
    print("=" * 55)
    username_box = driver.find_element(By.ID, "user-name")
    password_box = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    print("  用户名输入框:", username_box.get_attribute("placeholder"))
    print("  密码输入框  :", password_box.get_attribute("placeholder"))
    print("  登录按钮    :", login_button.get_attribute("value"))
    time.sleep(1)

    print()
    print("=" * 55)
    print("第 4 步：自己输入账号密码（看屏幕！）")
    print("=" * 55)
    username_box.send_keys(USERNAME)
    print("  已输入用户名:", USERNAME)
    time.sleep(0.8)
    password_box.send_keys(PASSWORD)
    print("  已输入密码:", PASSWORD)
    time.sleep(0.8)

    print()
    print("=" * 55)
    print("第 5 步：点击登录按钮")
    print("=" * 55)
    login_button.click()
    print("  已点击")

    print()
    print("=" * 55)
    print("第 6 步：等待并检查结果")
    print("=" * 55)
    # 显式等待：最多等 10 秒，直到网址里出现 inventory
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("inventory"))
    print("  登录成功！当前地址:", driver.current_url)

    page_title = driver.find_element(By.CLASS_NAME, "title").text
    print("  页面标题文字:", page_title)

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print("  页面上商品数量:", len(products))

    print()
    print("=" * 55)
    print("全部跑通！浏览器将在 5 秒后自动关闭。")
    print("=" * 55)
    time.sleep(5)

finally:
    driver.quit()
    print("浏览器已关闭。")
