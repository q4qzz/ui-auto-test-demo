# -*- coding: utf-8 -*-
"""登录模块自动化测试用例。

【这个文件里的每一条，都对应你手工用例表里的一条】
  test_login_success    -> TC-LOGIN-001
  参数化里的 6 条        -> TC-LOGIN-002 / 003 / 004 / 005 / 006 / 009
  大小写 2 条           -> TC-LOGIN-007 / 008

【数据驱动的威力】
看下面的 test_login_failure——函数只写了一遍，
但 pytest 会用 6 组数据把它跑 6 遍，等于 6 条用例。
要加新用例？在列表里加一行就行，代码一个字都不用改。
"""

import pytest

from pages.inventory_page import InventoryPage

# ============================================================
# 一、正确登录
# ============================================================


def test_login_success(login_page):
    """TC-LOGIN-001：正确账号密码登录成功，跳转到商品列表页。"""
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(login_page.driver).wait_until_loaded()

    # 断言 1：跳转到了商品页
    assert inventory.is_loaded, f"没有跳转到商品页，当前地址是 {login_page.current_url}"
    # 断言 2：页面标题是 Products
    assert inventory.title == "Products", f"标题不对，实际是 {inventory.title!r}"
    # 断言 3：商品数量是 6
    assert inventory.item_count == 6, f"商品数量不对，实际是 {inventory.item_count}"


# ============================================================
# 二、各类错误输入 —— 数据驱动，一个函数跑 6 组数据
# ============================================================


@pytest.mark.parametrize(
    "username, password, expected_keyword",
    [
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        ("", "", "Username is required"),
        ("standard_user", "wrong_password", "do not match"),
        ("not_exist_user", "secret_sauce", "do not match"),
        ("locked_out_user", "secret_sauce", "locked out"),
    ],
    ids=[
        "用户名为空-TC002",
        "密码为空-TC003",
        "账号密码都为空-TC006",
        "密码错误-TC005",
        "用户名不存在-TC004",
        "账号被锁定-TC009",
    ],
)
def test_login_failure(login_page, username, password, expected_keyword):
    """错误输入时，页面应给出对应提示，且不能进入商品页。"""
    login_page.login(username, password)

    # 断言 1：显示了错误提示
    assert login_page.has_error(), "页面上没有出现错误提示"

    # 断言 2：错误提示的内容符合预期
    actual = login_page.error_text()
    assert expected_keyword.lower() in actual.lower(), (
        f"期望提示里包含 {expected_keyword!r}\n实际提示是 {actual!r}"
    )

    # 断言 3：没有跳进商品页
    assert "inventory" not in login_page.current_url, (
        f"错误输入竟然登录成功了！当前地址 {login_page.current_url}"
    )


# ============================================================
# 三、大小写敏感 —— 对应你手工发现的 TC-LOGIN-007 / 008
# ============================================================


@pytest.mark.parametrize(
    "username, password",
    [
        ("VISUAL_USER", "secret_sauce"),
        ("visual_user", "SECRET_SAUCE"),
    ],
    ids=["用户名全大写-TC008", "密码全大写-TC007"],
)
def test_login_is_case_sensitive(login_page, username, password):
    """用户名和密码都对大小写敏感，大写应登录失败。"""
    login_page.login(username, password)

    assert login_page.has_error(), "大写输入竟然登录成功了，说明系统不区分大小写"
    assert "do not match" in login_page.error_text().lower()
    assert "inventory" not in login_page.current_url
