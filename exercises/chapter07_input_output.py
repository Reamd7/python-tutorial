"""
第7章：输入与输出 - 练习题

本章节练习基于 Python 官方教程第7章：输入与输出
参考：https://docs.python.org/zh-cn/3/tutorial/inputoutput.html

涵盖内容：
- 更复杂的输出格式
- 格式化字符串字面值 (f-strings)
- 字符串 format() 方法
- 手动格式化字符串
- 读写文件
- 使用 json 保存结构化数据
"""

import json
import os
import tempfile
from pathlib import Path
from datetime import datetime
import csv


def string_formatting_comprehensive(name, age, score, salary):
    """
    练习 7.1: 复杂的字符串格式化
    
    Args:
        name (str): 姓名
        age (int): 年龄
        score (float): 分数
        salary (float): 薪资
    
    Returns:
        dict: 包含各种格式化方法的结果
    """
    # TODO: 使用不同的格式化方法，返回包含以下键的字典：
    # 'f_string_basic': f"姓名：{name}，年龄：{age}"
    # 'f_string_aligned': 使用对齐格式化，姓名左对齐15字符，年龄右对齐3字符
    # 'f_string_precision': 分数保留2位小数，薪资保留1位小数
    # 'format_method': 使用 .format() 方法格式化
    # 'format_positional': 使用位置参数 {0}, {1} 等
    # 'format_named': 使用命名参数 {name}, {age} 等
    # 'percent_style': 使用 % 格式化（传统方法）
    pass


def number_formatting_examples():
    """
    练习 7.1.1: 数字格式化示例
    
    Returns:
        dict: 各种数字格式化的结果
    """
    # TODO: 演示数字格式化，返回包含以下键的字典：
    # 'integer_padding': 整数填充至6位，前面补0
    # 'float_precision': 浮点数保留3位小数
    # 'percentage': 转换为百分比格式
    # 'scientific': 科学计数法表示
    # 'binary': 二进制表示
    # 'hex': 十六进制表示
    # 'octal': 八进制表示
    # 'comma_separated': 千位分隔符
    pass


def alignment_and_padding_demo():
    """
    练习 7.1.1: 对齐和填充演示
    
    Returns:
        dict: 对齐和填充的格式化结果
    """
    # TODO: 演示对齐和填充，返回包含以下键的字典：
    # 'left_align': 左对齐在20字符宽度内
    # 'right_align': 右对齐在20字符宽度内  
    # 'center_align': 居中对齐在20字符宽度内
    # 'zero_padding': 数字零填充
    # 'char_padding': 使用特定字符填充
    # 'truncate': 截断过长的字符串
    pass


def file_reading_operations(file_content="Hello, World!\nThis is line 2.\nLine 3 here."):
    """
    练习 7.2: 文件读取操作
    
    Args:
        file_content (str): 要写入测试文件的内容
    
    Returns:
        dict: 各种文件读取操作的结果
    """
    # TODO: 创建临时文件并演示读取操作，返回：
    # 'read_all': 读取整个文件
    # 'read_lines': 按行读取的列表
    # 'read_first_line': 只读取第一行
    # 'read_with_limit': 读取前20个字符
    # 'line_count': 文件行数
    # 'char_count': 文件字符数
    # 注意：使用临时文件避免创建实际文件
    pass


def file_writing_operations():
    """
    练习 7.2: 文件写入操作
    
    Returns:
        dict: 各种文件写入操作的结果
    """
    # TODO: 演示文件写入操作，返回：
    # 'write_text': 写入普通文本的结果
    # 'write_lines': 写入多行文本的结果
    # 'append_text': 追加文本的结果
    # 'write_numbers': 写入数字数据的结果
    # 'file_sizes': 各个操作后的文件大小
    # 使用临时文件和 with 语句
    pass


def file_modes_demonstration():
    """
    练习 7.2.1: 文件模式演示
    
    Returns:
        dict: 不同文件模式的说明和示例
    """
    # TODO: 演示不同文件模式，返回：
    # 'text_modes': 文本模式的说明和使用场景
    # 'binary_modes': 二进制模式的说明和使用场景
    # 'append_mode': 追加模式的演示
    # 'read_write_mode': 读写模式的演示
    # 'mode_combinations': 模式组合的说明
    pass


def json_operations():
    """
    练习 7.2.2: JSON 操作
    
    Returns:
        dict: JSON 序列化和反序列化的结果
    """
    # TODO: 演示 JSON 操作，返回：
    # 'serialize_dict': 字典序列化为 JSON 字符串
    # 'serialize_list': 列表序列化为 JSON 字符串
    # 'deserialize_json': JSON 字符串反序列化
    # 'file_json_write': 写入 JSON 文件的结果
    # 'file_json_read': 从 JSON 文件读取的结果
    # 'pretty_json': 格式化的 JSON 输出
    
    # 示例数据
    data = {
        "students": [
            {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
            {"name": "Bob", "age": 22, "grades": [92, 88, 95]}
        ],
        "class": "Python 101",
        "date": "2024-01-15"
    }
    pass


def csv_file_operations():
    """
    练习 7.2: CSV 文件操作
    
    Returns:
        dict: CSV 文件操作的结果
    """
    # TODO: 演示 CSV 文件操作，返回：
    # 'write_csv': 写入 CSV 数据
    # 'read_csv': 读取 CSV 数据
    # 'csv_with_headers': 带标题的 CSV 处理
    # 'csv_different_delimiter': 使用不同分隔符的 CSV
    
    # 示例数据
    students_data = [
        ["Name", "Age", "Grade"],
        ["Alice", 20, 85],
        ["Bob", 22, 92],
        ["Charlie", 21, 78]
    ]
    pass


def path_operations():
    """
    练习 7.2: 路径操作（使用 pathlib）
    
    Returns:
        dict: 路径操作的结果
    """
    # TODO: 使用 pathlib 进行路径操作，返回：
    # 'current_path': 当前工作目录
    # 'file_exists': 检查文件是否存在
    # 'create_directory': 创建目录的结果
    # 'list_files': 列出目录中的文件
    # 'file_info': 文件信息（大小、修改时间等）
    # 'path_parts': 路径的各个部分
    pass


def advanced_string_formatting():
    """
    练习 7.1: 高级字符串格式化
    
    Returns:
        dict: 高级格式化技术的演示
    """
    # TODO: 演示高级格式化技术，返回：
    # 'nested_formatting': 嵌套格式化
    # 'conditional_formatting': 条件格式化
    # 'custom_format': 自定义格式化函数
    # 'datetime_formatting': 日期时间格式化
    # 'locale_formatting': 本地化格式化（如果适用）
    pass


def file_error_handling():
    """
    练习 7.2: 文件操作错误处理
    
    Returns:
        dict: 错误处理的演示结果
    """
    # TODO: 演示文件操作中的错误处理，返回：
    # 'file_not_found': 处理文件不存在的情况
    # 'permission_error': 处理权限错误的情况
    # 'encoding_error': 处理编码错误的情况
    # 'disk_full': 处理磁盘空间不足的情况（模拟）
    # 'best_practices': 文件操作的最佳实践列表
    pass


def text_file_encoding_demo():
    """
    练习 7.2: 文本文件编码演示
    
    Returns:
        dict: 不同编码的处理结果
    """
    # TODO: 演示文本编码处理，返回：
    # 'utf8_example': UTF-8 编码的文件操作
    # 'gbk_example': GBK 编码的文件操作（如果适用）
    # 'ascii_example': ASCII 编码的文件操作
    # 'encoding_detection': 编码检测的方法
    # 'encoding_conversion': 编码转换的示例
    pass


if __name__ == "__main__":
    print("第7章：输入与输出 - 练习题")
    print("=" * 45)
    
    # 测试字符串格式化
    print("7.1 字符串格式化测试：")
    try:
        result = string_formatting_comprehensive("张三", 25, 87.5, 12345.67)
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  字符串格式化函数尚未实现: {e}")
    
    # 测试数字格式化
    print("\n7.1.1 数字格式化测试：")
    try:
        result = number_formatting_examples()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  数字格式化函数尚未实现: {e}")
    
    # 测试文件读取
    print("\n7.2 文件读取测试：")
    try:
        result = file_reading_operations()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  文件读取函数尚未实现: {e}")
    
    # 测试 JSON 操作
    print("\n7.2.2 JSON 操作测试：")
    try:
        result = json_operations()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  JSON 操作函数尚未实现: {e}")
    
    # 测试路径操作
    print("\n7.2 路径操作测试：")
    try:
        result = path_operations()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  路径操作函数尚未实现: {e}")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！")
    print("注意：练习中使用临时文件，不会在你的系统中留下垃圾文件。") 