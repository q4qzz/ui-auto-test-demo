"""冒烟测试：证明你的 pytest 环境是通的。

这个文件不测业务，只测"工具链能不能跑"。
Day 1 的目标就是让这两个用例变成绿色的 passed。
"""

import sys


def test_environment_is_ready():
    """最基础的断言：1 + 1 应该等于 2。"""
    assert 1 + 1 == 2


def test_python_version_is_modern():
    """确认 Python 版本不低于 3.10。"""
    assert sys.version_info >= (3, 10), f"当前版本过低: {sys.version}"
