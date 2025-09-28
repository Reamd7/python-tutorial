"""
测试第3章：Python 速览 - 练习题

对应 exercises/chapter03_python_overview.py 的测试用例
"""

import pytest
import sys
import os

# 添加父目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter03_python_overview import (
    calculator_basic_math,
    calculator_power_and_modulo,
    string_concatenation_and_repetition,
    string_indexing_and_slicing,
    list_operations,
    list_methods_demo,
    fibonacci_sequence,
    print_number_series,
    string_formatting_demo
)


def test_calculator_basic_math():
    """测试基础数学运算 ?"""
    result = calculator_basic_math(10, 3)
    
    assert isinstance(result, dict)
    assert result['add'] == 13
    assert result['subtract'] == 7
    assert result['multiply'] == 30
    assert result['divide'] == pytest.approx(3.333333333333333)
    
    # 测试除零情况
    result_zero = calculator_basic_math(10, 0)
    assert result_zero['divide'] == float('inf') or result_zero['divide'] is None


def test_calculator_power_and_modulo():
    """测试幂运算和取模运算"""
    result = calculator_power_and_modulo(5, 3, 7)
    
    assert isinstance(result, dict)
    assert result['power'] == 125  # 5^3
    assert result['modulo'] == 5   # 5 % 7


def test_string_concatenation_and_repetition():
    """测试字符串连接和重复"""
    result = string_concatenation_and_repetition("Hello", 3)
    
    assert isinstance(result, dict)
    assert result['repeated'] == "HelloHelloHello"
    assert result['length'] == 15


def test_string_indexing_and_slicing():
    """测试字符串索引和切片"""
    result = string_indexing_and_slicing("Python")
    
    assert isinstance(result, dict)
    assert result['first_char'] == 'P'
    assert result['last_char'] == 'n'
    assert result['first_three'] == 'Pyt'
    assert result['last_three'] == 'hon'
    assert result['reverse'] == 'nohtyP'


def test_string_indexing_and_slicing_short():
    """测试短字符串的索引和切片"""
    result = string_indexing_and_slicing("Hi")
    
    assert result['first_char'] == 'H'
    assert result['last_char'] == 'i'
    assert result['first_three'] == 'Hi'  # 应该返回整个字符串
    assert result['last_three'] == 'Hi'   # 应该返回整个字符串
    assert result['reverse'] == 'iH'


def test_list_operations():
    """测试列表基础操作"""
    result = list_operations([1, 4, 9, 16, 25])
    
    assert isinstance(result, dict)
    assert result['length'] == 5
    assert result['sum'] == 55
    assert result['max'] == 25
    assert result['min'] == 1
    assert result['reversed'] == [25, 16, 9, 4, 1]


def test_list_operations_empty():
    """测试空列表操作"""
    result = list_operations([])
    
    assert result['length'] == 0
    assert result['sum'] == 0
    assert result['max'] is None or result['max'] == float('-inf')
    assert result['min'] is None or result['min'] == float('inf')
    assert result['reversed'] == []


def test_list_methods_demo():
    """测试列表方法演示"""
    result = list_methods_demo([1, 2, 3])
    
    assert isinstance(result, dict)
    assert result['appended'] == [1, 2, 3, 100]
    assert result['extended'] == [1, 2, 3, 200, 300]
    assert result['inserted'] == [1, 50, 2, 3]
    assert result['sorted'] == [1, 2, 3]


def test_fibonacci_sequence():
    """测试斐波那契数列"""
    result = fibonacci_sequence(100)
    
    assert isinstance(result, list)
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert result == expected
    
    # 测试边界情况
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0, 1]
    assert fibonacci_sequence(2) == [0, 1, 1]
    assert fibonacci_sequence(3) == [0, 1, 1, 2]



def test_print_number_series():
    """测试数字序列"""
    result = print_number_series(1, 6)
    assert result == [1, 2, 3, 4, 5]
    
    result_step = print_number_series(0, 10, 2)
    assert result_step == [0, 2, 4, 6, 8]
    
    result_negative = print_number_series(5, 0, -1)
    assert result_negative == [5, 4, 3, 2, 1]


def test_string_formatting_demo():
    """测试字符串格式化"""
    result = string_formatting_demo("小明", 20, 85.5)
    
    assert isinstance(result, dict)
    
    # 检查基本格式
    expected_text = "小明今年20岁，考试得了85.5分"
    assert expected_text in result['f_string']
    assert expected_text in result['format_method']
    
    # 检查精度格式化
    assert "85.5" in result['f_string'] or "85.6" in result['f_string']
    
    # 如果实现了 percent_style，检查它
    if 'percent_style' in result:
        assert expected_text in result['percent_style']


if __name__ == "__main__":
    pytest.main([__file__]) 