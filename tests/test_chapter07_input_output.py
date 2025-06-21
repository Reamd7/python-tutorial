"""
第7章：输入与输出 - 测试文件

测试 exercises/chapter07_input_output.py 中的练习函数
"""

import pytest
import sys
import os
import tempfile
import json
from pathlib import Path

# 添加 exercises 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter07_input_output import (
    string_formatting_comprehensive,
    number_formatting_examples,
    alignment_and_padding_demo,
    file_reading_operations,
    file_writing_operations,
    file_modes_demonstration,
    json_operations,
    csv_file_operations,
    path_operations,
    advanced_string_formatting,
    file_error_handling,
    text_file_encoding_demo
)


class TestInputOutput:
    """第7章：输入与输出练习的测试类"""
    
    def test_string_formatting_comprehensive(self):
        """测试复杂的字符串格式化"""
        result = string_formatting_comprehensive("张三", 25, 87.5, 12345.67)
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'f_string_basic', 'f_string_aligned', 'f_string_precision',
            'format_method', 'format_positional', 'format_named', 'percent_style'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
            assert isinstance(result[key], str), f"{key} 应该是字符串"
        
        # 验证基本格式化包含姓名和年龄
        assert "张三" in result['f_string_basic'], "基本格式化应该包含姓名"
        assert "25" in result['f_string_basic'], "基本格式化应该包含年龄"
    
    def test_number_formatting_examples(self):
        """测试数字格式化示例"""
        result = number_formatting_examples()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'integer_padding', 'float_precision', 'percentage',
            'scientific', 'binary', 'hex', 'octal', 'comma_separated'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
            assert isinstance(result[key], str), f"{key} 应该是字符串"
    
    def test_alignment_and_padding_demo(self):
        """测试对齐和填充演示"""
        result = alignment_and_padding_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'left_align', 'right_align', 'center_align',
            'zero_padding', 'char_padding', 'truncate'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
            assert isinstance(result[key], str), f"{key} 应该是字符串"
    
    def test_file_reading_operations(self):
        """测试文件读取操作"""
        test_content = "Hello, World!\nThis is line 2.\nLine 3 here."
        result = file_reading_operations(test_content)
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'read_all', 'read_lines', 'read_first_line',
            'read_with_limit', 'line_count', 'char_count'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert result['read_all'] == test_content, "读取的内容应该与原内容一致"
        assert isinstance(result['read_lines'], list), "按行读取应该返回列表"
        assert isinstance(result['line_count'], int), "行数应该是整数"
        assert isinstance(result['char_count'], int), "字符数应该是整数"
    
    def test_file_writing_operations(self):
        """测试文件写入操作"""
        result = file_writing_operations()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'write_text', 'write_lines', 'append_text',
            'write_numbers', 'file_sizes'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_file_modes_demonstration(self):
        """测试文件模式演示"""
        result = file_modes_demonstration()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'text_modes', 'binary_modes', 'append_mode',
            'read_write_mode', 'mode_combinations'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_json_operations(self):
        """测试 JSON 操作"""
        result = json_operations()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'serialize_dict', 'serialize_list', 'deserialize_json',
            'file_json_write', 'file_json_read', 'pretty_json'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        # 验证 JSON 序列化结果是有效的 JSON 字符串
        if 'serialize_dict' in result:
            try:
                json.loads(result['serialize_dict'])
            except json.JSONDecodeError:
                pytest.fail("序列化的字典应该是有效的 JSON")
    
    def test_csv_file_operations(self):
        """测试 CSV 文件操作"""
        result = csv_file_operations()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'write_csv', 'read_csv', 'csv_with_headers', 'csv_different_delimiter'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_path_operations(self):
        """测试路径操作"""
        result = path_operations()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'current_path', 'file_exists', 'create_directory',
            'list_files', 'file_info', 'path_parts'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        # 验证当前路径是 Path 对象或字符串
        assert isinstance(result['current_path'], (str, Path)), "当前路径应该是字符串或 Path 对象"
    
    def test_advanced_string_formatting(self):
        """测试高级字符串格式化"""
        result = advanced_string_formatting()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'nested_formatting', 'conditional_formatting', 'custom_format',
            'datetime_formatting', 'locale_formatting'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_file_error_handling(self):
        """测试文件操作错误处理"""
        result = file_error_handling()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'file_not_found', 'permission_error', 'encoding_error',
            'disk_full', 'best_practices'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['best_practices'], list), "最佳实践应该是列表"
        assert len(result['best_practices']) > 0, "应该有最佳实践建议"
    
    def test_text_file_encoding_demo(self):
        """测试文本文件编码演示"""
        result = text_file_encoding_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'utf8_example', 'gbk_example', 'ascii_example',
            'encoding_detection', 'encoding_conversion'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"


if __name__ == "__main__":
    pytest.main([__file__]) 