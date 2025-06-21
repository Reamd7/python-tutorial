"""
测试第4章：更多控制流工具 - 练习题

对应 exercises/chapter04_control_flow.py 的测试用例
"""

import pytest
import sys
import os

# 添加父目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter04_control_flow import (
    grade_classifier,
    number_analysis,
    range_experiments,
    find_primes,
    factorial_function,
    power_with_default,
    person_info,
    apply_operation,
    create_multiplier,
    validate_input,
    loop_with_else_demo,
    match_statement_demo
)


def test_grade_classifier():
    """测试成绩分类器"""
    assert grade_classifier(95) == 'A'
    assert grade_classifier(87) == 'B'
    assert grade_classifier(72) == 'C'
    assert grade_classifier(65) == 'D'
    assert grade_classifier(45) == 'F'
    
    # 边界测试
    assert grade_classifier(90) == 'A'
    assert grade_classifier(89) == 'B'
    assert grade_classifier(80) == 'B'
    assert grade_classifier(79) == 'C'
    assert grade_classifier(60) == 'D'
    assert grade_classifier(59) == 'F'


def test_number_analysis():
    """测试数字列表分析"""
    result = number_analysis([-2, -1, 0, 1, 2, 3, 4, 5])
    
    assert isinstance(result, dict)
    assert result['even_count'] == 4  # -2, 0, 2, 4
    assert result['odd_count'] == 4   # -1, 1, 3, 5
    assert result['positive_count'] == 5  # 1, 2, 3, 4, 5
    assert result['negative_count'] == 2  # -2, -1
    assert result['zero_count'] == 1  # 0


def test_range_experiments():
    """测试 range 函数实验"""
    result = range_experiments()
    
    assert isinstance(result, dict)
    assert result['range_10'] == list(range(10))
    assert result['range_5_15'] == list(range(5, 15))
    assert result['range_0_20_2'] == list(range(0, 20, 2))
    assert result['range_20_0_minus2'] == list(range(20, 0, -2))


def test_find_primes():
    """测试素数查找"""
    primes_30 = find_primes(30)
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert primes_30 == expected
    
    # 测试边界情况
    assert find_primes(2) == []
    assert find_primes(3) == [2]
    assert find_primes(10) == [2, 3, 5, 7]


def test_factorial_function():
    """测试阶乘函数"""
    assert factorial_function(0) == 1
    assert factorial_function(1) == 1
    assert factorial_function(5) == 120
    assert factorial_function(10) == 3628800


def test_power_with_default():
    """测试默认参数的幂运算"""
    assert power_with_default(3) == 9    # 3^2
    assert power_with_default(3, 3) == 27  # 3^3
    assert power_with_default(2, 4) == 16  # 2^4
    assert power_with_default(5, 0) == 1   # 5^0


def test_person_info():
    """测试个人信息函数"""
    result = person_info("张三", 25)
    
    assert isinstance(result, dict)
    assert result['name'] == "张三"
    assert result['age'] == 25
    assert result['city'] == "未知"
    
    # 测试带城市参数
    result_with_city = person_info("李四", 30, "北京")
    assert result_with_city['city'] == "北京"
    
    # 测试额外参数
    result_with_extra = person_info("王五", 35, "上海", job="工程师", hobby="编程")
    assert result_with_extra['job'] == "工程师"
    assert result_with_extra['hobby'] == "编程"


def test_apply_operation():
    """测试 Lambda 表达式应用"""
    numbers = [1, 2, 3, 4, 5]
    
    # 测试平方操作
    squared = apply_operation(numbers, lambda x: x ** 2)
    assert squared == [1, 4, 9, 16, 25]
    
    # 测试加倍操作
    doubled = apply_operation(numbers, lambda x: x * 2)
    assert doubled == [2, 4, 6, 8, 10]


def test_create_multiplier():
    """测试乘法器创建"""
    times_3 = create_multiplier(3)
    assert times_3(4) == 12
    assert times_3(5) == 15
    
    times_10 = create_multiplier(10)
    assert times_10(7) == 70


def test_validate_input():
    """测试输入验证"""
    # 有效输入
    result = validate_input(50)
    assert result['valid'] == True
    
    # 类型错误
    result = validate_input("50")
    assert result['valid'] == False
    assert 'type' in result['message'].lower()
    
    # 范围错误
    result = validate_input(150)
    assert result['valid'] == False
    assert 'range' in result['message'].lower()
    
    # 自定义范围
    result = validate_input(75, min_val=0, max_val=50)
    assert result['valid'] == False


def test_loop_with_else_demo():
    """测试循环的 else 子句"""
    numbers = [1, 2, 3, 4, 5]
    
    # 找到目标
    result = loop_with_else_demo(numbers, 3)
    assert result['found'] == True
    assert result['index'] == 2
    
    # 未找到目标
    result = loop_with_else_demo(numbers, 10)
    assert result['found'] == False
    assert result['index'] is None


def test_match_statement_demo():
    """测试 match 语句（或 if-elif 替代）"""
    # 测试不同类型的值
    result_int = match_statement_demo(42)
    assert isinstance(result_int, str)
    
    result_str = match_statement_demo("hello")
    assert isinstance(result_str, str)
    
    result_list = match_statement_demo([1, 2, 3])
    assert isinstance(result_list, str)


if __name__ == "__main__":
    pytest.main([__file__]) 