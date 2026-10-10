# -*- coding: utf-8 -*-
"""pytest 全局配置：浏览器 fixture。

【fixture 是什么？】
它就是"测试开始前帮你准备好东西、测试结束后帮你收拾干净"的机制。
这里它负责：每个用例启动一个全新的浏览器，用例跑完自动关闭浏览器。

【为什么每个用例都用新浏览器？】
这叫「用例独立性」——每个用例都应该在干净的环境里跑，
不能受上一条用例的影响。否则一条用例失败了，后面的会跟着连环失败，
你根本分不清是谁的问题。这是自动化测试的一条铁律。
"""

import os
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

ROOT = Path(__file__).parent
BASE_URL = "https://www.saucedemo.com"


def _build_options():
    """构造浏览器启动参数。"""
    options = Options()
    # 独立的浏览器配置目录，不干扰日常使用的 Edge
    options.add_argument(f"--user-data-dir={ROOT / '.edge-profile'}")
    options.add_argument("--window-size=1280,900")
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    # 以下参数用于在受限环境（CI 服务器、沙箱）中稳定启动
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    # 设了 HEADLESS=1 就不显示浏览器窗口，跑得更快
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
    return options


@pytest.fixture
def driver():
    """提供一个干净的浏览器，用完自动关闭。"""
    drv = webdriver.Edge(options=_build_options())
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    """提供一个已经打开的登录页对象。"""
    from pages.login_page import LoginPage

    return LoginPage(driver).open()
