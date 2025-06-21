"""
测试基础练习题的实现

这个文件包含了对 basic_exercises.py 中函数的测试用例。
运行 'pytest tests/' 来执行所有测试。
"""

import pytest
import sys
import os

# 添加父目录到 Python 路径，以便导入练习模块
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.basic_exercises import (
    hello_world,
    add_numbers,
    is_even,
    find_max,
    count_vowels,
    reverse_string,
    fibonacci
)


def test_hello_world():
    """测试 hello_world 函数"""
    assert hello_world() == "Hello, World!"


def test_add_numbers():
    """测试 add_numbers 函数"""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(3.5, 2.5) == 6.0


def test_is_even():
    """测试 is_even 函数"""
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-2) == True
    assert is_even(-3) == False


def test_find_max():
    """测试 find_max 函数"""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([-1, -2, -3]) == -1
    assert find_max([0]) == 0
    assert find_max([3.14, 2.71, 1.41]) == 3.14


def test_count_vowels():
    """测试 count_vowels 函数"""
    assert count_vowels("hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("bcdfg") == 0
    assert count_vowels("") == 0
    assert count_vowels("Python") == 1


def test_reverse_string():
    """测试 reverse_string 函数"""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("12345") == "54321"


def test_fibonacci():
    """测试 fibonacci 函数"""
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]


if __name__ == "__main__":
    # 运行所有测试
    pytest.main([__file__]) 