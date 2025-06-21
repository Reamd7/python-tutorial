"""
第11章：标准库简介——第二部分 - 练习题

本章节练习基于 Python 官方教程第11章：标准库简介——第二部分
参考：https://docs.python.org/zh-cn/3/tutorial/stdlib2.html

涵盖内容：
- 输出格式
- 模板
- 使用二进制数据记录布局
- 多线程
- 日志
- 弱引用
- 用于操作列表的工具
- 十进制浮点数算术
"""

import string
import struct
import threading
import queue
import logging
import weakref
import array
import collections
import bisect
import heapq
import decimal
import fractions
import random
import reprlib
import pprint
import textwrap
import locale
from collections import deque
from datetime import datetime
import time


def output_formatting_demo():
    """
    练习 11.1: 输出格式
    
    Returns:
        dict: 输出格式化的高级示例
    """
    # TODO: 演示高级输出格式化，返回：
    # 'reprlib_demo': 使用 reprlib 处理大型数据结构
    # 'pprint_demo': 使用 pprint 美化输出
    # 'textwrap_demo': 使用 textwrap 格式化文本
    # 'locale_demo': 使用 locale 进行本地化格式化
    # 'formatting_comparison': 不同格式化方法的对比
    
    # 示例数据
    large_dict = {f"key_{i}": f"value_{i}" for i in range(100)}
    long_text = "这是一段很长的文本，需要进行换行处理，以便在指定宽度内显示。" * 5
    pass


def template_string_demo():
    """
    练习 11.2: 模板
    
    Returns:
        dict: 字符串模板的使用示例
    """
    # TODO: 使用 string.Template 进行模板处理，返回：
    # 'basic_template': 基本模板替换
    # 'safe_substitute': 安全替换（允许缺失变量）
    # 'custom_delimiter': 自定义分隔符
    # 'template_vs_format': 模板与 format 的对比
    # 'security_benefits': 模板的安全性优势
    
    # 示例数据
    template_data = {
        'name': '张三',
        'age': 25,
        'city': '北京'
    }
    pass


def binary_data_layout():
    """
    练习 11.3: 使用二进制数据记录布局
    
    Returns:
        dict: 二进制数据处理的示例
    """
    # TODO: 使用 struct 模块处理二进制数据，返回：
    # 'pack_data': 打包数据为二进制
    # 'unpack_data': 解包二进制数据
    # 'struct_formats': 不同格式说明符的使用
    # 'endianness': 字节序处理
    # 'practical_example': 实际应用示例（如文件头解析）
    
    # 示例：模拟文件头信息
    file_header = {
        'signature': b'PYTH',
        'version': 1,
        'flags': 0x1234,
        'timestamp': int(time.time())
    }
    pass


def multithreading_demo():
    """
    练习 11.4: 多线程
    
    Returns:
        dict: 多线程编程的示例
    """
    # TODO: 演示多线程编程，返回：
    # 'basic_threading': 基本线程创建和启动
    # 'thread_communication': 线程间通信（使用 queue）
    # 'thread_synchronization': 线程同步（锁、事件等）
    # 'worker_pattern': 工作线程模式
    # 'performance_comparison': 单线程 vs 多线程性能对比
    
    def worker_function(data, result_queue):
        # 模拟耗时工作
        result = sum(data)
        result_queue.put(result)
        return result
    
    pass


def logging_demo():
    """
    练习 11.5: 日志
    
    Returns:
        dict: 日志系统的使用示例
    """
    # TODO: 演示日志系统，返回：
    # 'basic_logging': 基本日志记录
    # 'log_levels': 不同日志级别的使用
    # 'formatters': 日志格式化器
    # 'handlers': 不同日志处理器（文件、控制台等）
    # 'logger_hierarchy': 日志器层次结构
    # 'configuration': 日志配置示例
    pass


def weak_references_demo():
    """
    练习 11.6: 弱引用
    
    Returns:
        dict: 弱引用的使用示例
    """
    class ExpensiveObject:
        def __init__(self, name):
            self.name = name
        
        def __del__(self):
            print(f"删除 {self.name}")
    
    # TODO: 演示弱引用，返回：
    # 'weak_reference': 弱引用的创建和使用
    # 'weak_callback': 弱引用回调函数
    # 'weak_collections': 弱引用集合类型
    # 'memory_management': 内存管理优势
    # 'cache_example': 弱引用缓存示例
    pass


def list_manipulation_tools():
    """
    练习 11.7: 用于操作列表的工具
    
    Returns:
        dict: 列表操作工具的使用示例
    """
    # TODO: 演示列表操作工具，返回：
    # 'array_demo': array 模块的使用
    # 'deque_demo': deque 的高级用法
    # 'bisect_demo': bisect 模块的二分查找
    # 'heapq_demo': heapq 模块的堆操作
    # 'performance_comparison': 不同数据结构的性能对比
    
    sample_data = list(range(1000))
    pass


def decimal_arithmetic_demo():
    """
    练习 11.8: 十进制浮点数算术
    
    Returns:
        dict: 十进制算术的示例
    """
    # TODO: 使用 decimal 模块进行精确计算，返回：
    # 'precision_demo': 精度控制示例
    # 'rounding_modes': 不同舍入模式
    # 'financial_calculation': 金融计算示例
    # 'float_vs_decimal': float 与 Decimal 的对比
    # 'context_management': 上下文管理
    
    # 金融计算示例
    price = "29.95"
    tax_rate = "0.08"
    quantity = 3
    pass


def fractions_demo():
    """
    练习 11: 分数模块演示
    
    Returns:
        dict: fractions 模块的使用示例
    """
    # TODO: 使用 fractions 模块，返回：
    # 'basic_fractions': 基本分数操作
    # 'fraction_arithmetic': 分数算术运算
    # 'decimal_to_fraction': 小数转分数
    # 'rational_calculations': 有理数计算
    # 'precision_benefits': 精度优势演示
    pass


def advanced_collections_demo():
    """
    练习 11: 高级集合操作
    
    Returns:
        dict: 高级集合操作的示例
    """
    # TODO: 演示高级集合操作，返回：
    # 'counter_advanced': Counter 的高级用法
    # 'defaultdict_patterns': defaultdict 的常用模式
    # 'namedtuple_advanced': namedtuple 的高级特性
    # 'ordereddict_usage': OrderedDict 的使用场景
    # 'chainmap_demo': ChainMap 的使用示例
    pass


def performance_tools_demo():
    """
    练习 11: 性能工具演示
    
    Returns:
        dict: 性能分析工具的使用示例
    """
    import cProfile
    import profile
    import timeit
    
    # TODO: 演示性能分析工具，返回：
    # 'timeit_examples': timeit 的详细使用
    # 'profile_demo': profile 模块的使用
    # 'cProfile_demo': cProfile 的性能分析
    # 'memory_profiling': 内存使用分析
    # 'optimization_tips': 优化建议
    
    def example_function():
        return sum(range(10000))
    
    pass


def data_structures_comparison():
    """
    练习 11: 数据结构性能对比
    
    Returns:
        dict: 不同数据结构的性能对比
    """
    # TODO: 对比不同数据结构的性能，返回：
    # 'list_vs_deque': list 与 deque 的性能对比
    # 'dict_vs_defaultdict': dict 与 defaultdict 的对比
    # 'set_operations': 集合操作的性能测试
    # 'memory_usage': 内存使用对比
    # 'use_case_recommendations': 使用场景推荐
    pass


def advanced_string_processing():
    """
    练习 11: 高级字符串处理
    
    Returns:
        dict: 高级字符串处理技术
    """
    # TODO: 演示高级字符串处理，返回：
    # 'string_constants': string 模块的常量
    # 'custom_formatters': 自定义格式化器
    # 'text_analysis': 文本分析示例
    # 'encoding_handling': 编码处理
    # 'unicode_normalization': Unicode 标准化
    
    sample_text = """
    这是一个包含多种字符的示例文本：
    English, 中文, العربية, русский, 日本語
    数字：123456789
    符号：!@#$%^&*()
    """
    pass


def concurrency_patterns():
    """
    练习 11: 并发模式
    
    Returns:
        dict: 并发编程模式的示例
    """
    # TODO: 演示并发编程模式，返回：
    # 'producer_consumer': 生产者-消费者模式
    # 'thread_pool': 线程池模式
    # 'async_patterns': 异步编程模式
    # 'synchronization_primitives': 同步原语
    # 'deadlock_avoidance': 死锁避免技术
    pass


if __name__ == "__main__":
    print("第11章：标准库简介——第二部分 - 练习题")
    print("=" * 60)
    
    # 测试输出格式化
    print("11.1 输出格式化测试：")
    try:
        result = output_formatting_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  输出格式化函数尚未实现: {e}")
    
    # 测试模板
    print("\n11.2 模板测试：")
    try:
        result = template_string_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  模板函数尚未实现: {e}")
    
    # 测试二进制数据
    print("\n11.3 二进制数据测试：")
    try:
        result = binary_data_layout()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  二进制数据函数尚未实现: {e}")
    
    # 测试多线程
    print("\n11.4 多线程测试：")
    try:
        result = multithreading_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  多线程函数尚未实现: {e}")
    
    # 测试日志
    print("\n11.5 日志测试：")
    try:
        result = logging_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  日志函数尚未实现: {e}")
    
    # 测试十进制算术
    print("\n11.8 十进制算术测试：")
    try:
        result = decimal_arithmetic_demo()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  十进制算术函数尚未实现: {e}")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！")
    print("这些高级模块是 Python 标准库的精华，掌握它们将大大提升编程能力。") 