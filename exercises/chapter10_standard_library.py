"""
第10章：标准库简介 - 练习题

本章节练习基于 Python 官方教程第10章：标准库简介
参考：https://docs.python.org/zh-cn/3/tutorial/stdlib.html

涵盖内容：
- 操作系统接口
- 文件通配符
- 命令行参数
- 错误输出重定向和程序终止
- 字符串模式匹配
- 数学
- 互联网访问
- 日期和时间
- 数据压缩
- 性能测量
- 质量控制
- "内置电池"
"""

import os
import sys
import glob
import re
import math
import random
import statistics
import datetime
import time
import gzip
import zipfile
import timeit
import urllib.request
import json
import doctest
import unittest
from pathlib import Path
import tempfile


def operating_system_interface():
    """
    练习 10.1: 操作系统接口
    
    Returns:
        dict: 操作系统接口的使用示例
    """
    # TODO: 使用 os 模块进行系统操作，返回：
    # 'current_directory': 当前工作目录
    # 'environment_variables': 重要的环境变量（如 PATH, HOME）
    # 'directory_listing': 当前目录的文件列表
    # 'system_info': 系统信息（操作系统名称等）
    # 'temp_directory': 临时目录路径
    # 'user_home': 用户主目录
    # 'path_separator': 路径分隔符
    pass


def file_wildcards_demo():
    """
    练习 10.2: 文件通配符
    
    Returns:
        dict: 文件通配符的使用示例
    """
    # TODO: 使用 glob 模块进行文件匹配，返回：
    # 'py_files': 当前目录中的 .py 文件
    # 'all_files': 当前目录中的所有文件
    # 'recursive_search': 递归搜索所有 Python 文件
    # 'pattern_examples': 不同通配符模式的示例
    # 'glob_vs_listdir': glob 与 os.listdir 的对比
    pass


def command_line_arguments():
    """
    练习 10.3: 命令行参数
    
    Returns:
        dict: 命令行参数处理的示例
    """
    # TODO: 处理命令行参数，返回：
    # 'script_name': 脚本名称
    # 'arguments': 命令行参数列表
    # 'argument_count': 参数数量
    # 'parsed_arguments': 解析后的参数（模拟）
    # 'usage_example': 使用示例字符串
    pass


def string_pattern_matching():
    """
    练习 10.5: 字符串模式匹配
    
    Returns:
        dict: 正则表达式的使用示例
    """
    # TODO: 使用 re 模块进行模式匹配，返回：
    # 'email_validation': 邮箱地址验证示例
    # 'phone_extraction': 电话号码提取示例
    # 'text_substitution': 文本替换示例
    # 'pattern_finding': 模式查找示例
    # 'split_examples': 字符串分割示例
    
    sample_text = """
    联系我们：
    邮箱: alice@example.com, bob@company.org
    电话: 138-0013-8000, (010)8888-9999
    日期: 2024-01-15, 2024/02/20
    """
    pass


def mathematics_modules():
    """
    练习 10.6: 数学模块
    
    Returns:
        dict: 数学相关模块的使用示例
    """
    # TODO: 使用 math, random, statistics 模块，返回：
    # 'math_functions': 常用数学函数的结果
    # 'random_examples': 随机数生成示例
    # 'statistics_demo': 统计函数示例
    # 'trigonometric': 三角函数计算
    # 'logarithmic': 对数函数计算
    # 'probability_simulation': 概率模拟示例
    
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pass


def date_and_time_handling():
    """
    练习 10.8: 日期和时间
    
    Returns:
        dict: 日期时间处理的示例
    """
    # TODO: 使用 datetime 和 time 模块，返回：
    # 'current_datetime': 当前日期时间
    # 'formatted_dates': 不同格式的日期字符串
    # 'date_arithmetic': 日期计算示例
    # 'time_zones': 时区处理示例
    # 'duration_calculation': 时间间隔计算
    # 'timestamp_conversion': 时间戳转换
    pass


def data_compression_demo():
    """
    练习 10.9: 数据压缩
    
    Returns:
        dict: 数据压缩的演示
    """
    # TODO: 使用 gzip 和 zipfile 模块，返回：
    # 'gzip_compression': gzip 压缩示例
    # 'zip_compression': zip 压缩示例
    # 'compression_ratios': 压缩比对比
    # 'decompression_demo': 解压缩示例
    # 'file_sizes': 压缩前后的文件大小
    
    sample_text = "这是一个用于测试压缩的示例文本。" * 100
    pass


def performance_measurement():
    """
    练习 10.10: 性能测量
    
    Returns:
        dict: 性能测量的示例
    """
    # TODO: 使用 timeit 模块测量性能，返回：
    # 'list_vs_tuple': 列表 vs 元组的性能对比
    # 'string_concatenation': 字符串连接方法的性能对比
    # 'loop_performance': 不同循环方式的性能对比
    # 'function_call_overhead': 函数调用开销测量
    # 'best_practices': 性能优化建议
    pass


def internet_access_demo():
    """
    练习 10.7: 互联网访问
    
    Returns:
        dict: 互联网访问的示例
    """
    # TODO: 使用 urllib 模块进行网络访问，返回：
    # 'url_fetch': URL 内容获取示例（使用安全的测试URL）
    # 'json_api': JSON API 调用示例
    # 'error_handling': 网络错误处理
    # 'timeout_handling': 超时处理
    # 'user_agent': User-Agent 设置示例
    
    # 注意：实际实现时可能需要处理网络连接问题
    pass


def quality_control_doctest():
    """
    练习 10.11: 质量控制 - doctest
    
    Returns:
        dict: doctest 的使用示例
    
    Examples:
        >>> quality_control_doctest()['simple_test']
        'doctest 示例'
        
        >>> 2 + 2
        4
        
        >>> [1, 2, 3]
        [1, 2, 3]
    """
    # TODO: 演示 doctest 的使用，返回：
    # 'simple_test': 简单测试示例
    # 'doctest_results': doctest 运行结果
    # 'test_count': 测试数量
    # 'failure_count': 失败数量
    pass


def quality_control_unittest():
    """
    练习 10.11: 质量控制 - unittest
    
    Returns:
        dict: unittest 的使用示例
    """
    class TestMathOperations(unittest.TestCase):
        def test_addition(self):
            self.assertEqual(2 + 2, 4)
        
        def test_multiplication(self):
            self.assertEqual(3 * 4, 12)
        
        def test_division(self):
            self.assertEqual(10 / 2, 5)
            with self.assertRaises(ZeroDivisionError):
                10 / 0
    
    # TODO: 演示 unittest 的使用，返回：
    # 'test_suite': 测试套件信息
    # 'test_results': 测试运行结果
    # 'assertion_examples': 断言方法示例
    # 'setup_teardown': setUp 和 tearDown 示例
    pass


def pathlib_modern_approach():
    """
    练习 10: 现代路径处理 (pathlib)
    
    Returns:
        dict: pathlib 的使用示例
    """
    # TODO: 使用 pathlib 进行现代化路径操作，返回：
    # 'path_creation': 路径创建示例
    # 'path_operations': 路径操作示例
    # 'file_operations': 文件操作示例
    # 'directory_operations': 目录操作示例
    # 'pathlib_vs_os': pathlib 与 os.path 的对比
    pass


def collections_module_demo():
    """
    练习 10: collections 模块演示
    
    Returns:
        dict: collections 模块的使用示例
    """
    from collections import Counter, defaultdict, deque, namedtuple
    
    # TODO: 演示 collections 模块，返回：
    # 'counter_examples': Counter 的使用示例
    # 'defaultdict_examples': defaultdict 的使用示例
    # 'deque_examples': deque 的使用示例
    # 'namedtuple_examples': namedtuple 的使用示例
    # 'practical_applications': 实际应用场景
    
    sample_data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    pass


def itertools_module_demo():
    """
    练习 10: itertools 模块演示
    
    Returns:
        dict: itertools 模块的使用示例
    """
    import itertools
    
    # TODO: 演示 itertools 模块，返回：
    # 'infinite_iterators': 无限迭代器示例
    # 'finite_iterators': 有限迭代器示例
    # 'combinatorial_iterators': 组合迭代器示例
    # 'practical_examples': 实际应用示例
    # 'performance_benefits': 性能优势演示
    pass


if __name__ == "__main__":
    print("第10章：标准库简介 - 练习题")
    print("=" * 50)
    
    # 测试操作系统接口
    print("10.1 操作系统接口测试：")
    try:
        result = operating_system_interface()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  操作系统接口函数尚未实现: {e}")
    
    # 测试文件通配符
    print("\n10.2 文件通配符测试：")
    try:
        result = file_wildcards_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  文件通配符函数尚未实现: {e}")
    
    # 测试字符串模式匹配
    print("\n10.5 字符串模式匹配测试：")
    try:
        result = string_pattern_matching()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  字符串模式匹配函数尚未实现: {e}")
    
    # 测试数学模块
    print("\n10.6 数学模块测试：")
    try:
        result = mathematics_modules()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  数学模块函数尚未实现: {e}")
    
    # 测试日期时间
    print("\n10.8 日期时间测试：")
    try:
        result = date_and_time_handling()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  日期时间函数尚未实现: {e}")
    
    # 测试性能测量
    print("\n10.10 性能测量测试：")
    try:
        result = performance_measurement()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  性能测量函数尚未实现: {e}")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！")
    print("标准库是 Python 的强大之处，熟练掌握将大大提高开发效率。") 