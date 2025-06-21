"""
第5章：数据结构 - 练习题

本章节练习基于 Python 官方教程第5章：数据结构
参考：https://docs.python.org/zh-cn/3/tutorial/datastructures.html

涵盖内容：
- 列表详解（列表方法、堆栈、队列、列表推导式）
- 元组和序列
- 集合
- 字典
- 循环的技巧
"""

from collections import deque


def list_methods_comprehensive(original_list, item_to_add, item_to_remove):
    """
    练习 5.1: 列表方法综合练习
    
    Args:
        original_list (list): 原始列表
        item_to_add: 要添加的项目
        item_to_remove: 要移除的项目
    
    Returns:
        dict: 各种列表操作的结果
    """
    # TODO: 返回包含以下操作结果的字典：
    # 'append_result': 使用 append() 添加 item_to_add 后的列表
    # 'insert_result': 在索引 1 处插入 item_to_add 的结果
    # 'remove_result': 移除第一个 item_to_remove 的结果（如果存在）
    # 'pop_result': 弹出最后一个元素后的 (剩余列表, 弹出的元素)
    # 'index_result': item_to_add 的索引（如果不存在返回 -1）
    # 'count_result': item_to_add 在列表中的出现次数
    # 'sort_result': 排序后的列表（如果可排序）
    # 'reverse_result': 反转后的列表
    pass


def stack_operations(operations):
    """
    练习 5.1.1: 用列表实现堆栈
    
    Args:
        operations (list): 操作列表，格式：[('push', value), ('pop',), ...]
    
    Returns:
        dict: 堆栈操作结果
    """
    # TODO: 实现堆栈操作
    # 返回 {'final_stack': list, 'popped_items': list}
    pass


def queue_operations(operations):
    """
    练习 5.1.2: 用列表实现队列（使用 collections.deque）
    
    Args:
        operations (list): 操作列表，格式：[('enqueue', value), ('dequeue',), ...]
    
    Returns:
        dict: 队列操作结果
    """
    # TODO: 使用 deque 实现队列操作
    # 返回 {'final_queue': list, 'dequeued_items': list}
    pass


def list_comprehensions_practice(numbers):
    """
    练习 5.1.3: 列表推导式练习
    
    Args:
        numbers (list): 数字列表
    
    Returns:
        dict: 各种列表推导式的结果
    """
    # TODO: 返回包含以下列表推导式结果的字典：
    # 'squares': 平方数列表
    # 'evens': 偶数列表
    # 'positive': 正数列表
    # 'squares_of_evens': 偶数的平方列表
    # 'abs_values': 绝对值列表
    pass


def nested_list_comprehension(matrix):
    """
    练习 5.1.4: 嵌套列表推导式
    
    Args:
        matrix (list): 二维矩阵（列表的列表）
    
    Returns:
        dict: 矩阵操作结果
    """
    # TODO: 返回包含以下结果的字典：
    # 'transposed': 转置矩阵
    # 'flattened': 扁平化后的一维列表
    # 'diagonal': 对角线元素（如果是方阵）
    # 'row_sums': 每行元素之和
    # 'col_sums': 每列元素之和
    pass


def tuple_operations(data_list):
    """
    练习 5.3: 元组和序列操作
    
    Args:
        data_list (list): 数据列表
    
    Returns:
        dict: 元组操作结果
    """
    # TODO: 返回包含以下结果的字典：
    # 'tuple_created': 从列表创建的元组
    # 'unpacked': 元组解包的结果（如果可能）
    # 'nested_tuple': 嵌套元组 ((1, 2), (3, 4))
    # 'tuple_concatenation': 两个元组连接的结果
    # 'tuple_repetition': 元组重复3次的结果
    pass


def set_operations(set1, set2):
    """
    练习 5.4: 集合操作
    
    Args:
        set1 (set): 第一个集合
        set2 (set): 第二个集合
    
    Returns:
        dict: 集合操作结果
    """
    # TODO: 返回包含以下集合操作结果的字典：
    # 'union': 并集
    # 'intersection': 交集
    # 'difference': 差集 (set1 - set2)
    # 'symmetric_difference': 对称差集
    # 'is_subset': set1 是否是 set2 的子集
    # 'is_superset': set1 是否是 set2 的超集
    # 'is_disjoint': 两个集合是否无交集
    pass


def dictionary_operations(data):
    """
    练习 5.5: 字典操作
    
    Args:
        data (list): 元组列表，格式：[(key, value), ...]
    
    Returns:
        dict: 字典操作结果
    """
    # TODO: 返回包含以下操作结果的字典：
    # 'created_dict': 从 data 创建的字典
    # 'keys_list': 所有键的列表
    # 'values_list': 所有值的列表
    # 'items_list': 所有键值对的列表
    # 'dict_comprehension': 使用字典推导式创建 {key: value*2} 的字典
    pass


def advanced_dictionary_practice(students_data):
    """
    练习 5.5: 高级字典练习
    
    Args:
        students_data (list): 学生数据，格式：[{'name': str, 'scores': [int, ...]}, ...]
    
    Returns:
        dict: 处理结果
    """
    # TODO: 返回包含以下结果的字典：
    # 'average_scores': {student_name: average_score}
    # 'top_student': 平均分最高的学生姓名
    # 'passing_students': 平均分>=60的学生列表
    # 'subject_averages': 如果每个学生有相同数量的科目，计算每科的平均分
    pass


def looping_techniques_demo(data_dict):
    """
    练习 5.6: 循环的技巧
    
    Args:
        data_dict (dict): 要处理的字典
    
    Returns:
        dict: 循环技巧演示结果
    """
    # TODO: 演示各种循环技巧，返回：
    # 'items_loop': 使用 items() 循环的结果列表
    # 'enumerate_keys': 使用 enumerate() 对键的结果
    # 'zip_keys_values': 使用 zip() 配对键值的结果
    # 'reversed_items': 反向循环的结果
    # 'sorted_by_key': 按键排序循环的结果
    # 'sorted_by_value': 按值排序循环的结果
    pass


def sequence_comparison(seq1, seq2):
    """
    练习 5.8: 序列和其他类型的比较
    
    Args:
        seq1: 第一个序列
        seq2: 第二个序列
    
    Returns:
        dict: 比较结果
    """
    # TODO: 返回包含以下比较结果的字典：
    # 'equal': 是否相等
    # 'lexicographic': 字典序比较结果 (-1, 0, 1)
    # 'length_comparison': 长度比较结果
    # 'type_same': 类型是否相同
    # 'first_difference_index': 第一个不同元素的索引（如果存在）
    pass


def del_statement_demo(original_list):
    """
    练习 5.2: del 语句演示
    
    Args:
        original_list (list): 原始列表
    
    Returns:
        dict: del 语句操作结果
    """
    # TODO: 演示 del 语句的各种用法，返回：
    # 'del_by_index': 删除索引2的元素后的列表
    # 'del_slice': 删除切片 [1:3] 后的列表
    # 'del_every_second': 删除每隔一个元素后的列表
    # 'clear_list': 清空列表后的结果
    pass


if __name__ == "__main__":
    print("第5章：数据结构 - 练习题")
    print("=" * 40)
    
    # 测试列表方法
    print("5.1 列表方法测试：")
    try:
        result = list_methods_comprehensive([1, 2, 3, 2, 4], 5, 2)
        for key, value in result.items():
            print(f"{key}: {value}")
    except:
        print("列表方法函数尚未实现")
    
    # 测试堆栛操作
    print("\n5.1.1 堆栈操作测试：")
    try:
        operations = [('push', 1), ('push', 2), ('push', 3), ('pop',), ('pop',)]
        result = stack_operations(operations)
        print(f"堆栈操作结果: {result}")
    except:
        print("堆栈操作函数尚未实现")
    
    # 测试队列操作
    print("\n5.1.2 队列操作测试：")
    try:
        operations = [('enqueue', 'a'), ('enqueue', 'b'), ('dequeue',), ('enqueue', 'c')]
        result = queue_operations(operations)
        print(f"队列操作结果: {result}")
    except:
        print("队列操作函数尚未实现")
    
    # 测试列表推导式
    print("\n5.1.3 列表推导式测试：")
    try:
        result = list_comprehensions_practice([-2, -1, 0, 1, 2, 3, 4])
        for key, value in result.items():
            print(f"{key}: {value}")
    except:
        print("列表推导式函数尚未实现")
    
    # 测试集合操作
    print("\n5.4 集合操作测试：")
    try:
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        result = set_operations(set1, set2)
        for key, value in result.items():
            print(f"{key}: {value}")
    except:
        print("集合操作函数尚未实现")
    
    # 测试字典操作
    print("\n5.5 字典操作测试：")
    try:
        data = [('name', 'Alice'), ('age', 25), ('city', 'Beijing')]
        result = dictionary_operations(data)
        for key, value in result.items():
            print(f"{key}: {value}")
    except:
        print("字典操作函数尚未实现")
    
    print("\n请实现上述函数，然后运行 pytest tests/ 验证实现！") 