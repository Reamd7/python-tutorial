"""
第6章：模块 - 测试文件

测试 exercises/chapter06_modules.py 中的练习函数
"""

import pytest
import sys
import os
from pathlib import Path

# 添加 exercises 目录到 Python 路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from exercises.chapter06_modules import (
    create_simple_module_content,
    demonstrate_import_variations,
    analyze_module_attributes,
    module_search_path_info,
    create_package_structure,
    relative_import_examples,
    standard_library_explorer,
    module_reloading_demo,
    namespace_and_scope_demo,
    practical_module_usage
)


class TestModules:
    """第6章：模块练习的测试类"""
    
    def test_create_simple_module_content(self):
        """测试创建简单模块内容"""
        result = create_simple_module_content()
        
        assert isinstance(result, str), "应该返回字符串"
        assert "PI" in result, "应该包含 PI 常量"
        assert "def greet" in result, "应该包含 greet 函数定义"
        assert "class Calculator" in result, "应该包含 Calculator 类"
        assert "__main__" in result, "应该包含 __main__ 检查"
    
    def test_demonstrate_import_variations(self):
        """测试各种导入方式演示"""
        result = demonstrate_import_variations("math")
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'import_module', 'import_as', 'from_import',
            'from_import_as', 'from_import_all'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        # 验证实际的计算结果
        if 'import_module' in result:
            assert isinstance(result['import_module'], (int, float, str))
    
    def test_analyze_module_attributes(self):
        """测试模块属性分析"""
        result = analyze_module_attributes("random")
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'total_attributes', 'public_attributes', 'private_attributes',
            'functions', 'module_name', 'module_doc'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['total_attributes'], int), "总属性数应该是整数"
        assert result['total_attributes'] > 0, "总属性数应该大于0"
        assert isinstance(result['functions'], list), "函数列表应该是列表"
        assert result['module_name'] == 'random', "模块名应该是 'random'"
    
    def test_module_search_path_info(self):
        """测试模块搜索路径信息"""
        result = module_search_path_info()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'python_path', 'current_directory', 'python_executable',
            'path_length', 'builtin_modules'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['python_path'], list), "Python 路径应该是列表"
        assert isinstance(result['path_length'], int), "路径长度应该是整数"
        assert result['path_length'] > 0, "路径长度应该大于0"
        assert isinstance(result['builtin_modules'], int), "内置模块数应该是整数"
    
    def test_create_package_structure(self):
        """测试包结构设计"""
        result = create_package_structure()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'package_tree', 'init_files', 'module_files', 'import_examples'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['init_files'], list), "__init__ 文件列表应该是列表"
        assert isinstance(result['module_files'], list), "模块文件列表应该是列表"
        assert isinstance(result['import_examples'], list), "导入示例应该是列表"
    
    def test_relative_import_examples(self):
        """测试相对导入示例"""
        result = relative_import_examples()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'absolute_imports', 'relative_imports', 'same_level',
            'parent_level', 'best_practices'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['best_practices'], list), "最佳实践应该是列表"
        assert len(result['best_practices']) > 0, "应该有最佳实践建议"
    
    def test_standard_library_explorer(self):
        """测试标准库探索"""
        result = standard_library_explorer()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'os_example', 'sys_example', 'datetime_example',
            'random_example', 'math_example'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_module_reloading_demo(self):
        """测试模块重新加载演示"""
        result = module_reloading_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'loaded_modules', 'reload_explanation',
            'importlib_usage', 'module_cache'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
        
        assert isinstance(result['loaded_modules'], int), "已加载模块数应该是整数"
        assert result['loaded_modules'] > 0, "已加载模块数应该大于0"
    
    def test_namespace_and_scope_demo(self):
        """测试命名空间和作用域演示"""
        result = namespace_and_scope_demo()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'local_namespace', 'global_namespace',
            'builtin_namespace', 'module_namespace'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"
    
    def test_practical_module_usage(self):
        """测试实际模块使用场景"""
        result = practical_module_usage()
        
        assert isinstance(result, dict), "应该返回字典"
        
        expected_keys = [
            'file_operations', 'data_processing', 'date_calculations',
            'random_generation', 'math_calculations'
        ]
        
        for key in expected_keys:
            assert key in result, f"应该包含键 {key}"


if __name__ == "__main__":
    pytest.main([__file__]) 