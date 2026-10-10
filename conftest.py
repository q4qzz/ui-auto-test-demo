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
    # ★ 关键：无痕模式。
    # 因为 --user-data-dir 是复用的，上一次跑测试留下的 localStorage
    # （比如购物车里的商品）会带到这一次，导致用例莫名其妙地失败。
    # 这种"脏数据"引起的失败叫 flaky test，是自动化测试的头号敌人。
    # 无痕模式保证每个用例都在干净的环境里开始。
    options.add_argument("--inprivate")
    # 以下参数用于在受限环境（CI 服务器、沙箱）中稳定启动
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    # 设了 HEADLESS=1 就不显示浏览器窗口，跑得更快
    if os.environ.get("HEADLESS") == "1":
        options.add_argument("--headless=new")
    return options


def _reset_storage(drv):
    """清空浏览器里残留的 localStorage / sessionStorage / cookie。

    【为什么必须做这一步】
    因为 --user-data-dir 是复用的，上一次跑测试时加进购物车的商品、
    留下的登录状态，会原封不动地带到这一次来。
    这种"脏数据"会让用例莫名其妙地失败，或者这次过、下次不过。

    【它叫什么】
    这种不稳定现象叫 flaky test（抖动用例），是自动化测试的头号敌人。
    面试时被问到"你怎么保证用例稳定"，这就是标准答案之一：
    「每个用例开始前显式清理环境状态，不依赖上一个用例的结果。」
    """
    drv.get(BASE_URL)
    drv.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
    drv.delete_all_cookies()


@pytest.fixture
def driver():
    """提供一个干净的浏览器，用完自动关闭。"""
    drv = webdriver.Edge(options=_build_options())
    _reset_storage(drv)
    yield drv
    drv.quit()


@pytest.fixture
def login_page(driver):
    """提供一个已经打开的登录页对象。"""
    from pages.login_page import LoginPage

    return LoginPage(driver).open()
