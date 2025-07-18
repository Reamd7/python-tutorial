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

def list_methods_comprehensive[T](original_list: list[T], item_to_add: T, item_to_remove: T):
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
    append_result = original_list.copy()
    append_result.append(item_to_add)
    # 'insert_result': 在索引 1 处插入 item_to_add 的结果
    insert_result = original_list.copy()
    insert_result.insert(1, item_to_add)
    # 'remove_result': 移除第一个 item_to_remove 的结果（如果存在）
    remove_result = original_list.copy()
    remove_result.remove(item_to_remove)
    # 'pop_result': 弹出最后一个元素后的 (剩余列表, 弹出的元素)
    pop_result = original_list.copy()
    pop_result.pop()
    # 'index_result': item_to_add 的索引（如果不存在返回 -1）
    index_result = original_list.copy()
    index_result.index(item_to_add)
    # 'count_result': item_to_add 在列表中的出现次数
    count_result = original_list.copy()
    count_result.count(item_to_add)
    # 'sort_result': 排序后的列表（如果可排序）
    sort_result = original_list.copy()
    # sort_result.sort()
    # 'reverse_result': 反转后的列表
    reverse_result = original_list.copy()
    reverse_result.reverse()
    return {
        'append_result': append_result,
        'insert_result': insert_result,
        'remove_result': remove_result,
        'pop_result': pop_result,
        'index_result': index_result,
        'count_result': count_result,
        # 'sort_result': sort_result,
        'reverse_result': reverse_result,
    }


from typing import TypeAlias, TypedDict
from typing import Union, Literal, Any, TypeVar

# 如果您使用 Python 3.12+
type PushOperation[T] = tuple[Literal['push'], T]
type PopOperation = tuple[Literal['pop']]
type StackOperation[T] = PushOperation[T] | PopOperation

def stack_operations[T](operations: list[StackOperation[T]]):
    """
    练习 5.1.1: 用列表实现堆栈
    
    Args:
        operations (list): 操作列表，格式：[('push', value), ('pop',), ...]
    
    Returns:
        dict: 堆栈操作结果
    """
    # TODO: 实现堆栈操作

    stack: list[T] = []
    for operation in operations:
        if operation[0] == 'push':
            stack.append(operation[1])
        elif operation[0] == 'pop':
            stack.pop()
    return {'final_stack': stack, 'popped_items': stack}

    # 返回 {'final_stack': list, 'popped_items': list}


type EnqueueOperation[T] = tuple[Literal['enqueue'], T]
type DequeueOperation = tuple[Literal['dequeue']]
type QueueOperation[T] = EnqueueOperation[T] | DequeueOperation

def queue_operations[T](operations: list[QueueOperation[T]]):
    """
    练习 5.1.2: 用列表实现队列（使用 collections.deque）
    
    Args:
        operations: 操作列表，格式：[('enqueue', value), ('dequeue',), ...]
    
    Returns:
        dict: 队列操作结果
    """
    queue: list[T] = []
    for operation in operations:
        if operation[0] == 'enqueue':
            queue.append(operation[1])
        elif operation[0] == 'dequeue':
            queue.pop(0)
    return {'final_queue': queue, 'dequeued_items': queue}

    # TODO: 使用 deque 实现队列操作
    # 返回 {'final_queue': list, 'dequeued_items': list}


def list_comprehensions_practice(numbers: list[int]):
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

    squares = [x**2 for x in numbers]
    evens = [x for x in numbers if x % 2 == 0]
    positive = [x for x in numbers if not (x <= 0)]
    squares_of_evens = [x**2 for x in numbers if x % 2 == 0]
    abs_values = [abs(x) for x in numbers]
    return {'squares': squares, 'evens': evens, 'positive': positive, 'squares_of_evens': squares_of_evens, 'abs_values': abs_values}


def nested_list_comprehension(matrix: list[list[int]]):
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
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    flattened = [item for sublist in matrix for item in sublist]
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    return {'transposed': transposed, 'flattened': flattened, 'diagonal': diagonal, 'row_sums': row_sums, 'col_sums': col_sums}


def tuple_operations(data_list: list[int]):
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

    tuple_created = tuple(data_list)
    unpacked = tuple_created[0], tuple_created[1], tuple_created[2]
    nested_tuple = ((1, 2), (3, 4))
    tuple_concatenation = tuple_created + nested_tuple
    tuple_repetition = tuple_created * 3
    return {'tuple_created': tuple_created, 'unpacked': unpacked, 'nested_tuple': nested_tuple, 'tuple_concatenation': tuple_concatenation, 'tuple_repetition': tuple_repetition}


def set_operations(set1: set[int], set2: set[int]):
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
    union = set1 | set2
    intersection = set1 & set2
    difference = set1 - set2
    symmetric_difference = set1 ^ set2
    is_subset = set1 <= set2
    is_superset = set1 >= set2
    is_disjoint = set1.isdisjoint(set2)
    return {'union': union, 'intersection': intersection, 'difference': difference, 'symmetric_difference': symmetric_difference, 'is_subset': is_subset, 'is_superset': is_superset, 'is_disjoint': is_disjoint}


def dictionary_operations(data: list[tuple[str, int]]):
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
    created_dict = dict(data)
    keys_list = list(created_dict.keys())
    values_list = list(created_dict.values())
    items_list = list(created_dict.items())
    dict_comprehension = {key: value * 2 for key, value in created_dict.items()}
    return {'created_dict': created_dict, 'keys_list': keys_list, 'values_list': values_list, 'items_list': items_list, 'dict_comprehension': dict_comprehension}

class StudentData(TypedDict, total=True):
    """
    学生数据结构，严格限定只包含以下字段：
    - name: 学生姓名  
    - scores: 学生分数列表
    """
    name: str
    scores: list[int]

def advanced_dictionary_practice(students_data: list[StudentData]):
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
    average_scores = {student['name']: sum(student['scores']) / len(student['scores']) for student in students_data}
    top_student = max(average_scores.items(), key=lambda x: x[1])[0]
    passing_students = [student for student in students_data if sum(student['scores']) / len(student['scores']) >= 60]
    subject_averages = {i: sum(student['scores'][i] for student in students_data) / len(students_data) for i in range(len(students_data[0]['scores']))}
    return {'average_scores': average_scores, 'top_student': top_student, 'passing_students': passing_students, 'subject_averages': subject_averages}


def looping_techniques_demo(data_dict: dict[str, int]):
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
    items_loop = list(data_dict.items())
    enumerate_keys = list(enumerate(data_dict.keys()))
    zip_keys_values = list(zip(data_dict.keys(), data_dict.values()))
    reversed_items = list(reversed(data_dict.items()))
    sorted_by_key = sorted(data_dict.items(), key=lambda x: x[0])
    sorted_by_value = sorted(data_dict.items(), key=lambda x: x[1])
    return {'items_loop': items_loop, 'enumerate_keys': enumerate_keys, 'zip_keys_values': zip_keys_values, 'reversed_items': reversed_items, 'sorted_by_key': sorted_by_key, 'sorted_by_value': sorted_by_value}


def sequence_comparison(seq1: list[int], seq2: list[int]):
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
    equal = all(x == y for x, y in zip(seq1, seq2))
    # 'lexicographic': 字典序比较结果 (-1, 0, 1)
    lexicographic = 0 if seq1 == seq2 else -1 if seq1 < seq2 else 1
    # 'length_comparison': 长度比较结果
    length_comparison = -1 if len(seq1) < len(seq2) else 1 if len(seq1) > len(seq2) else 0
    # 'type_same': 类型是否相同
    type_same = type(seq1) == type(seq2)
    # 'first_difference_index': 第一个不同元素的索引（如果存在）
    first_difference_index = next(
        (i for i, (x, y) in enumerate(zip(seq1, seq2)) if x != y), -1
    )
    return {'equal': equal, 'lexicographic': lexicographic, 'length_comparison': length_comparison, 'type_same': type_same, 'first_difference_index': first_difference_index}


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
    del_by_index = original_list.copy()
    del del_by_index[2]
    del_slice = original_list.copy()
    del del_slice[1:3]
    del_every_second = original_list.copy()
    del del_every_second[::2]
    clear_list = original_list.copy()
    clear_list.clear()
    return {'del_by_index': del_by_index, 'del_slice': del_slice, 'del_every_second': del_every_second, 'clear_list': clear_list}


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