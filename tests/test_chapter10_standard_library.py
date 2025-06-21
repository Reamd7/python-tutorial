"""
第10章：标准库简介 - 测试文件

测试 exercises/chapter10_standard_library.py 中的练习函数
"""

import pytest
import sys
import os
from pathlib import Path

# 添加 exercises 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter10_standard_library import (
    operating_system_interface,
    file_wildcards_demo,
    command_line_arguments,
    string_pattern_matching,
    mathematics_modules,
    date_and_time_handling,
    data_compression_demo,
    performance_measurement,
    internet_access_demo,
    quality_control_doctest,
    quality_control_unittest,
    pathlib_modern_approach,
    collections_module_demo,
    itertools_module_demo
)


class TestStandardLibrary:
    """第10章：标准库简介练习的测试类"""
    
    def test_operating_system_interface(self):
        """测试操作系统接口"""
        result = operating_system_interface()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'current_directory', 'environment_variables', 'directory_listing',
            'system_info', 'temp_directory', 'user_home', 'path_separator'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['current_directory'], str), "当前目录应该是字符串"
        assert isinstance(result['environment_variables'], dict), "环境变量应该是字典"
        assert isinstance(result['directory_listing'], list), "目录列表应该是列表"
        assert isinstance(result['path_separator'], str), "路径分隔符应该是字符串"
    
    def test_file_wildcards_demo(self):
        """测试文件通配符"""
        result = file_wildcards_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'py_files', 'all_files', 'recursive_search',
            'pattern_examples', 'glob_vs_listdir'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['py_files'], list), "Python 文件列表应该是列表"
        assert isinstance(result['all_files'], list), "所有文件列表应该是列表"
    
    def test_command_line_arguments(self):
        """测试命令行参数"""
        result = command_line_arguments()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'script_name', 'arguments', 'argument_count',
            'parsed_arguments', 'usage_example'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['script_name'], str), "脚本名应该是字符串"
        assert isinstance(result['arguments'], list), "参数应该是列表"
        assert isinstance(result['argument_count'], int), "参数数量应该是整数"
    
    def test_string_pattern_matching(self):
        """测试字符串模式匹配"""
        result = string_pattern_matching()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'email_validation', 'phone_extraction', 'text_substitution',
            'pattern_finding', 'split_examples'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_mathematics_modules(self):
        """测试数学模块"""
        result = mathematics_modules()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'math_functions', 'random_examples', 'statistics_demo',
            'trigonometric', 'logarithmic', 'probability_simulation'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_date_and_time_handling(self):
        """测试日期和时间"""
        result = date_and_time_handling()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'current_datetime', 'formatted_dates', 'date_arithmetic',
            'time_zones', 'duration_calculation', 'timestamp_conversion'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_data_compression_demo(self):
        """测试数据压缩"""
        result = data_compression_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'gzip_compression', 'zip_compression', 'compression_ratios',
            'decompression_demo', 'file_sizes'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_performance_measurement(self):
        """测试性能测量"""
        result = performance_measurement()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'list_vs_tuple', 'string_concatenation', 'loop_performance',
            'function_call_overhead', 'best_practices'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['best_practices'], list), "最佳实践应该是列表"
    
    def test_internet_access_demo(self):
        """测试互联网访问"""
        result = internet_access_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'url_fetch', 'json_api', 'error_handling',
            'timeout_handling', 'user_agent'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_quality_control_doctest(self):
        """测试质量控制 - doctest"""
        result = quality_control_doctest()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'simple_test', 'doctest_results', 'test_count', 'failure_count'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        # 验证 doctest 示例
        assert result['simple_test'] == 'doctest 示例', "简单测试应该返回预期值"
        assert isinstance(result['test_count'], int), "测试数量应该是整数"
        assert isinstance(result['failure_count'], int), "失败数量应该是整数"
    
    def test_quality_control_unittest(self):
        """测试质量控制 - unittest"""
        result = quality_control_unittest()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'test_suite', 'test_results', 'assertion_examples', 'setup_teardown'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_pathlib_modern_approach(self):
        """测试现代路径处理"""
        result = pathlib_modern_approach()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'path_creation', 'path_operations', 'file_operations',
            'directory_operations', 'pathlib_vs_os'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_collections_module_demo(self):
        """测试 collections 模块演示"""
        result = collections_module_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'counter_examples', 'defaultdict_examples', 'deque_examples',
            'namedtuple_examples', 'practical_applications'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_itertools_module_demo(self):
        """测试 itertools 模块演示"""
        result = itertools_module_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'infinite_iterators', 'finite_iterators', 'combinatorial_iterators',
            'practical_examples', 'performance_benefits'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"


if __name__ == "__main__":
    pytest.main([__file__]) 