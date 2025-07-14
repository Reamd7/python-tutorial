"""
第6章：模块 - 练习题

本章节练习基于 Python 官方教程第6章：模块
参考：https://docs.python.org/zh-cn/3/tutorial/modules.html

涵盖内容：
- 模块的创建和导入
- 模块搜索路径
- 包的概念和使用
- from...import 语句
- __name__ 变量的使用
- dir() 函数
"""

import os
import sys
import math
import random
from collections import defaultdict
from datetime import datetime, timedelta


def create_simple_module_content():
    """
    练习 6.1: 创建简单模块内容
    
    Returns:
        str: 一个简单模块的内容字符串，包含变量、函数和类
    """
    # TODO: 返回一个模块内容字符串，包含：
    # - 模块文档字符串
    # - 一个全局变量 PI = 3.14159
    # - 一个函数 greet(name) 返回问候语
    # - 一个简单的类 Calculator，有 add 和 multiply 方法
    # - __name__ == "__main__" 的测试代码
    import math
    PI = math.pi
    def greet(name):
        return f"Hello, {name}!"
    class Calculator:
        def add(self, a, b):
            return a + b
        def multiply(self, a, b):
            return a * b
    if __name__ == "__main__":
        print(f"PI: {PI}")
        print(greet("Alice"))
        calc = Calculator()
        print(calc.add(2, 3))
        print(calc.multiply(2, 3))

    pass


def demonstrate_import_variations(module_name="math"):
    """
    练习 6.1: 演示各种导入方式
    
    Args:
        module_name (str): 要导入的模块名
    
    Returns:
        dict: 不同导入方式的演示结果
    """
    # TODO: 演示以下导入方式并返回结果：
    # 'import_module': 使用 import math
    # 'import_as': 使用 import math as m
    # 'from_import': 使用 from math import pi, sqrt
    # 'from_import_as': 使用 from math import pi as PI
    # 'from_import_all': 说明 from math import * 的效果（但不要真的用）
    # 每个键对应的值应该是相关计算结果或说明

    import math
    import math as m
    from math import pi, sqrt
    from math import pi as PI
    # from math import *
    return {
        'import_module': math.pi,
        'import_as': m.pi,
        'from_import': pi,
        'from_import_as': PI,
        # 'from_import_all': 
    }
    pass


def analyze_module_attributes(module_name="random"):
    """
    练习 6.3: 分析模块属性
    
    Args:
        module_name (str): 要分析的模块名
    
    Returns:
        dict: 模块属性分析结果
    """
    # TODO: 使用 dir() 函数分析模块，返回：
    # 'total_attributes': 总属性数量
    # 'public_attributes': 非下划线开头的属性数量
    # 'private_attributes': 下划线开头的属性数量
    # 'functions': 函数类型的属性列表（使用 callable() 检查）
    # 'module_name': 模块的 __name__ 属性
    # 'module_doc': 模块的 __doc__ 属性的前100个字符
    attributes = dir(module_name)
    total_attributes = len(attributes)
    public_attributes = [attr for attr in attributes if not attr.startswith('_')]
    private_attributes = [attr for attr in attributes if attr.startswith('_')]
    functions = [attr for attr in public_attributes if callable(getattr(module_name, attr))]
    module_name = getattr(module_name, '__name__')
    module_doc = getattr(module_name, '__doc__')[:100]
    return {
        'total_attributes': total_attributes,
        'public_attributes': len(public_attributes),
        'private_attributes': len(private_attributes),
        'functions': functions,
        'module_name': module_name,
        'module_doc': module_doc,
    }
    pass


def module_search_path_info():
    """
    练习 6.1.2: 模块搜索路径信息
    
    Returns:
        dict: 模块搜索路径的相关信息
    """
    # TODO: 返回包含以下信息的字典：
    # 'python_path': sys.path 的内容
    # 'current_directory': 当前工作目录
    # 'python_executable': Python 解释器路径
    # 'path_length': sys.path 的长度
    # 'builtin_modules': 内置模块数量 len(sys.builtin_module_names)
    import sys
    import os
    python_path = sys.path
    current_directory = os.getcwd()
    python_executable = sys.executable
    path_length = len(sys.path)
    builtin_modules = len(sys.builtin_module_names)
    return {
        'python_path': python_path,
        'current_directory': current_directory,
        'python_executable': python_executable,
        'path_length': path_length,
        'builtin_modules': builtin_modules,
    }


def create_package_structure():
    """
    练习 6.4: 包结构设计
    
    Returns:
        dict: 包结构的设计方案
    """
    # TODO: 设计一个名为 'mypackage' 的包结构，返回：
    # 'package_tree': 包结构的字典表示
    # 'init_files': 需要创建的 __init__.py 文件列表
    # 'module_files': 子模块文件列表
    # 'import_examples': 展示如何导入包中的模块
    
    # 示例结构：
    # mypackage/
    #   __init__.py
    #   utils/
    #     __init__.py
    #     helpers.py
    #   data/
    #     __init__.py
    #     processing.py
    package_tree = {
        'mypackage': {
            '__init__.py': '',
            'utils': {
                '__init__.py': '',
                'helpers.py': '',
            },
            'data': {
                '__init__.py': '',
                'processing.py': '',
            },
        },
    }
    init_files = ['__init__.py']
    module_files = ['helpers.py', 'processing.py']
    import_examples = ['from mypackage.utils import helpers', 'from mypackage.data import processing']
    return {
        'package_tree': package_tree,
        'init_files': init_files,
        'module_files': module_files,
        'import_examples': import_examples,
    }
    pass


def relative_import_examples():
    """
    练习 6.4.2: 相对导入示例
    
    Returns:
        dict: 相对导入的示例和说明
    """
    # TODO: 返回相对导入的示例，包含：
    # 'absolute_imports': 绝对导入的示例列表
    # 'relative_imports': 相对导入的示例列表
    # 'same_level': 同级导入示例 (from . import module)
    # 'parent_level': 父级导入示例 (from .. import module)
    # 'best_practices': 最佳实践建议列表
    absolute_imports = ['from mypackage.utils import helpers', 'from mypackage.data import processing']
    relative_imports = ['from .utils import helpers', 'from ..data import processing']
    same_level = ['from . import utils', 'from . import data']
    parent_level = ['from .. import utils', 'from .. import data']
    best_practices = ['from mypackage.utils import helpers', 'from mypackage.data import processing']
    return {
        'absolute_imports': absolute_imports,
        'relative_imports': relative_imports,
        'same_level': same_level,
        'parent_level': parent_level,
        'best_practices': best_practices,
    }
    pass


def standard_library_explorer():
    """
    练习 6.2: 标准库探索
    
    Returns:
        dict: 标准库模块的使用示例
    """
    # TODO: 演示常用标准库模块的使用，返回：
    # 'os_example': 使用 os 模块的示例结果
    # 'sys_example': 使用 sys 模块的示例结果
    # 'datetime_example': 使用 datetime 模块的示例结果
    # 'random_example': 使用 random 模块的示例结果
    # 'math_example': 使用 math 模块的示例结果
    import os
    import sys
    import datetime
    import random
    import math
    return {
        'os_example': os.getcwd(),
        'sys_example': sys.path,
        'datetime_example': datetime.datetime.now(),
        'random_example': random.randint(1, 100),
        'math_example': math.pi,
    }
    pass


def module_reloading_demo():
    """
    练习 6.1.3: 模块重新加载演示
    
    Returns:
        dict: 模块重新加载的相关信息
    """
    # TODO: 演示模块重新加载概念，返回：
    # 'loaded_modules': 当前已加载的模块数量
    # 'reload_explanation': 解释为什么通常不需要重新加载模块
    # 'importlib_usage': 说明如何使用 importlib.reload()
    # 'module_cache': 说明 sys.modules 的作用
    import importlib
    import sys
    loaded_modules = len(sys.modules)
    reload_explanation = "通常不需要重新加载模块，因为模块在第一次导入时会被缓存。"
    importlib_usage = "可以使用 importlib.reload() 重新加载模块。"
    module_cache = "sys.modules 是一个字典，存储了所有已加载的模块。"
    return {
        'loaded_modules': loaded_modules,
        'reload_explanation': reload_explanation,
        'importlib_usage': importlib_usage,
        'module_cache': module_cache,
    }
    pass


def namespace_and_scope_demo():
    """
    练习 6.1: 命名空间和作用域演示
    
    Returns:
        dict: 命名空间和作用域的演示
    """
    # TODO: 演示命名空间概念，返回：
    # 'local_namespace': 本地命名空间中的变量
    # 'global_namespace': 全局命名空间中的一些变量
    # 'builtin_namespace': 内置命名空间的一些函数
    # 'module_namespace': 导入模块的命名空间示例
    local_namespace = locals()
    global_namespace = globals()
    builtin_namespace = dir(__builtins__)
    module_namespace = dir(math)
    return {
        'local_namespace': local_namespace,
        'global_namespace': global_namespace,
        'builtin_namespace': builtin_namespace,
        'module_namespace': module_namespace,
    }
    pass


def practical_module_usage():
    """
    练习 6: 实际模块使用场景
    
    Returns:
        dict: 实际使用场景的演示
    """
    # TODO: 创建实际使用场景，返回：
    # 'file_operations': 使用 os 和 pathlib 进行文件操作
    # 'data_processing': 使用 collections 进行数据处理
    # 'date_calculations': 使用 datetime 进行日期计算
    # 'random_generation': 使用 random 生成随机数据
    # 'math_calculations': 使用 math 进行数学计算
    pass


# 辅助工具函数
def create_demo_module_file(filename="demo_module.py"):
    """
    创建一个演示用的模块文件
    
    Args:
        filename (str): 要创建的文件名
    
    Returns:
        bool: 是否创建成功
    """
    # TODO: 创建一个演示模块文件，包含：
    # - 模块文档字符串
    # - 一些函数和变量
    # - __name__ == "__main__" 的测试代码
    pass


def cleanup_demo_files():
    """
    清理演示文件
    
    Returns:
        list: 已清理的文件列表
    """
    # TODO: 清理创建的演示文件
    pass


if __name__ == "__main__":
    print("第6章：模块 - 练习题")
    print("=" * 40)
    
    # 测试模块导入变化
    print("6.1 模块导入演示：")
    try:
        result = demonstrate_import_variations()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  导入演示函数尚未实现: {e}")
    
    # 测试模块属性分析
    print("\n6.3 模块属性分析：")
    try:
        result = analyze_module_attributes("math")
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  模块属性分析函数尚未实现: {e}")
    
    # 测试搜索路径信息
    print("\n6.1.2 模块搜索路径：")
    try:
        result = module_search_path_info()
        print(f"  Python 路径条目数: {result.get('path_length', 'Unknown')}")
        print(f"  当前目录: {result.get('current_directory', 'Unknown')}")
    except Exception as e:
        print(f"  搜索路径信息函数尚未实现: {e}")
    
    # 测试标准库探索
    print("\n6.2 标准库探索：")
    try:
        result = standard_library_explorer()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  标准库探索函数尚未实现: {e}")
    
    # 测试实际使用场景
    print("\n6 实际模块使用：")
    try:
        result = practical_module_usage()
        for key, value in result.items():
            print(f"  {key}: {value}")
    except Exception as e:
        print(f"  实际使用场景函数尚未实现: {e}")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！")
    print("提示：某些函数涉及文件创建，请小心处理文件操作。") 