"""
第14章：数据类 (Dataclasses)
Dataclasses and Modern Data Handling

本章涵盖：
- @dataclass 装饰器基础
- 字段定义和默认值
- 后处理方法 __post_init__
- 不可变数据类 (frozen)
- 字段配置和验证
- 数据类继承
- 与传统类的对比
- JSON序列化和反序列化
"""

from dataclasses import dataclass, field, fields, asdict, astuple
from typing import List, Optional, ClassVar, Any, Dict
from datetime import datetime, date
from enum import Enum, auto
import json


# =============================================================================
# 1. 基础数据类
# =============================================================================

@dataclass
class Person:
    """
    TODO: 基础人员数据类
    - 定义 name (str), age (int), email (str) 字段
    - 添加一个方法 is_adult() 返回是否成年
    """
    pass


@dataclass
class Point:
    """
    TODO: 2D坐标点
    - 定义 x (float) 和 y (float) 字段
    - 添加方法 distance_to(other: Point) -> float
    - 添加方法 move(dx: float, dy: float) -> Point (返回新点)
    """
    pass


@dataclass
class Book:
    """
    TODO: 图书数据类
    - title (str): 书名
    - author (str): 作者
    - pages (int): 页数
    - price (float): 价格
    - isbn (Optional[str]): ISBN，默认为 None
    - in_stock (bool): 是否有库存，默认为 True
    """
    pass


# =============================================================================
# 2. 带默认值和字段配置
# =============================================================================

@dataclass
class User:
    """
    TODO: 用户数据类，演示各种字段配置
    - username (str): 用户名
    - email (str): 邮箱
    - full_name (str): 全名，默认为空字符串
    - is_active (bool): 是否激活，默认 True
    - created_at (datetime): 创建时间，使用 field(default_factory=datetime.now)
    - tags (List[str]): 标签列表，默认为空列表
    - metadata (Dict[str, Any]): 元数据，默认为空字典
    """
    pass


@dataclass
class Product:
    """
    TODO: 商品数据类
    - id (int): 商品ID
    - name (str): 商品名称
    - price (float): 价格
    - category (str): 分类
    - description (str): 描述，默认空字符串
    - discount (float): 折扣，默认 0.0
    - stock_count (int): 库存数量，默认 0
    - review_scores (List[float]): 评分列表，默认空列表
    
    添加方法：
    - discounted_price() -> float: 返回折扣后价格
    - average_rating() -> float: 返回平均评分
    - is_available() -> bool: 是否有库存
    """
    pass


# =============================================================================
# 3. 不可变数据类 (frozen)
# =============================================================================

@dataclass(frozen=True)
class ImmutablePoint:
    """
    TODO: 不可变坐标点
    - x (float) 和 y (float) 坐标
    - 添加 __add__ 方法实现点的相加
    - 添加 __mul__ 方法实现标量乘法
    - 添加属性方法 magnitude() 计算向量长度
    """
    pass


@dataclass(frozen=True)
class Color:
    """
    TODO: 不可变颜色类
    - red (int), green (int), blue (int): RGB值 (0-255)
    - alpha (float): 透明度，默认 1.0
    
    添加方法：
    - to_hex() -> str: 转换为十六进制字符串
    - brighten(factor: float) -> Color: 返回变亮的新颜色
    - darken(factor: float) -> Color: 返回变暗的新颜色
    """
    pass


# =============================================================================
# 4. 后处理方法 __post_init__
# =============================================================================

@dataclass
class Rectangle:
    """
    TODO: 矩形类，使用 __post_init__ 进行验证
    - width (float): 宽度
    - height (float): 高度
    
    在 __post_init__ 中：
    - 验证宽度和高度都大于 0
    - 如果无效，抛出 ValueError
    
    添加方法：
    - area() -> float: 计算面积
    - perimeter() -> float: 计算周长
    - is_square() -> bool: 是否为正方形
    """
    pass


@dataclass
class EmailAddress:
    """
    TODO: 邮箱地址类，使用 __post_init__ 验证格式
    - address (str): 邮箱地址
    - domain (str): 域名 (在 __post_init__ 中从 address 提取)
    - username (str): 用户名 (在 __post_init__ 中从 address 提取)
    
    在 __post_init__ 中：
    - 验证邮箱格式 (包含 @ 且 @ 前后都有内容)
    - 提取并设置 domain 和 username
    """
    pass


# =============================================================================
# 5. 高级字段配置
# =============================================================================

@dataclass
class DatabaseRecord:
    """
    TODO: 数据库记录类，演示高级字段配置
    - id (int): 记录ID
    - data (Dict[str, Any]): 数据字典，默认空字典
    - created_at (datetime): 创建时间，不包含在比较中
    - updated_at (datetime): 更新时间，不包含在比较和打印中
    - version (int): 版本号，默认 1，不包含在初始化中
    
    提示：使用 field() 的 compare, repr, init 参数
    """
    pass


class Priority(Enum):
    """任务优先级枚举"""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    URGENT = auto()


@dataclass
class Task:
    """
    TODO: 任务类
    - title (str): 任务标题
    - description (str): 任务描述，默认空字符串
    - priority (Priority): 优先级，默认 Priority.MEDIUM
    - assigned_to (Optional[str]): 分配给谁，默认 None
    - due_date (Optional[date]): 截止日期，默认 None
    - completed (bool): 是否完成，默认 False
    - subtasks (List[str]): 子任务列表，默认空列表
    
    添加方法：
    - mark_completed(): 标记为已完成
    - add_subtask(subtask: str): 添加子任务
    - days_until_due() -> Optional[int]: 距离截止日期的天数
    """
    pass


# =============================================================================
# 6. 数据类继承
# =============================================================================

@dataclass
class Animal:
    """
    TODO: 动物基类
    - name (str): 动物名称
    - species (str): 物种
    - age (int): 年龄
    
    添加方法：
    - make_sound() -> str: 返回 "Some generic animal sound"
    - info() -> str: 返回动物的基本信息
    """
    pass


@dataclass
class Dog(Animal):
    """
    TODO: 狗类，继承自 Animal
    - breed (str): 品种
    - is_trained (bool): 是否训练过，默认 False
    
    重写方法：
    - make_sound() -> str: 返回 "Woof!"
    
    添加方法：
    - fetch() -> str: 如果训练过返回相关信息
    """
    pass


@dataclass
class Cat(Animal):
    """
    TODO: 猫类，继承自 Animal
    - indoor_only (bool): 是否只在室内，默认 True
    - favorite_toy (str): 最喜欢的玩具，默认 "ball"
    
    重写方法：
    - make_sound() -> str: 返回 "Meow!"
    
    添加方法：
    - hunt() -> str: 返回狩猎行为描述
    """
    pass


# =============================================================================
# 7. 类变量和实例变量
# =============================================================================

@dataclass
class Student:
    """
    TODO: 学生类，演示类变量的使用
    - name (str): 学生姓名
    - student_id (str): 学号
    - grades (List[float]): 成绩列表，默认空列表
    - school_name (ClassVar[str]): 学校名称，类变量，默认 "Unknown School"
    - total_students (ClassVar[int]): 学生总数，类变量，默认 0
    
    在 __post_init__ 中增加学生总数
    
    添加方法：
    - add_grade(grade: float): 添加成绩
    - gpa() -> float: 计算GPA (平均分)
    - get_student_count() -> int: 类方法，返回学生总数
    """
    pass


# =============================================================================
# 8. JSON 序列化和反序列化
# =============================================================================

@dataclass
class Address:
    """
    TODO: 地址类
    - street (str): 街道
    - city (str): 城市
    - state (str): 州/省
    - zip_code (str): 邮编
    - country (str): 国家，默认 "US"
    
    添加方法：
    - to_dict() -> Dict[str, Any]: 转换为字典
    - from_dict(data: Dict[str, Any]) -> Address: 类方法，从字典创建
    - to_json() -> str: 转换为JSON字符串
    - from_json(json_str: str) -> Address: 类方法，从JSON创建
    """
    pass


@dataclass
class PersonWithAddress:
    """
    TODO: 带地址的人员类
    - name (str): 姓名
    - age (int): 年龄
    - email (str): 邮箱
    - address (Address): 地址
    - phone_numbers (List[str]): 电话号码列表，默认空列表
    
    添加方法：
    - to_dict() -> Dict[str, Any]: 转换为字典（包括嵌套对象）
    - from_dict(data: Dict[str, Any]) -> PersonWithAddress: 从字典创建
    - to_json() -> str: 转换为JSON
    - from_json(json_str: str) -> PersonWithAddress: 从JSON创建
    """
    pass


# =============================================================================
# 9. 数据验证和转换
# =============================================================================

@dataclass
class BankAccount:
    """
    TODO: 银行账户类，演示数据验证
    - account_number (str): 账户号码
    - balance (float): 余额
    - owner_name (str): 账户所有者
    - account_type (str): 账户类型，默认 "checking"
    - is_active (bool): 是否激活，默认 True
    
    在 __post_init__ 中验证：
    - 账户号码不能为空
    - 余额不能为负数
    - 所有者姓名不能为空
    
    添加方法：
    - deposit(amount: float): 存款
    - withdraw(amount: float) -> bool: 取款，返回是否成功
    - transfer_to(other_account, amount: float) -> bool: 转账
    """
    pass


# =============================================================================
# 10. 性能比较和实用工具
# =============================================================================

class TraditionalClass:
    """
    TODO: 传统类实现（用于性能对比）
    - 手动实现 __init__, __repr__, __eq__ 等方法
    - 字段：name (str), value (int), items (List[str])
    """
    pass


@dataclass
class DataclassVersion:
    """
    TODO: 数据类版本（用于性能对比）
    - 字段：name (str), value (int), items (List[str])
    """
    pass


def compare_implementations():
    """
    TODO: 比较传统类和数据类的实现
    - 创建两种类的实例
    - 比较创建时间、内存使用等
    - 测试相等性比较、字符串表示等功能
    """
    pass


def dataclass_utilities_demo():
    """
    TODO: 演示数据类实用工具
    - 使用 fields() 函数检查字段
    - 使用 asdict() 和 astuple() 转换
    - 演示字段的各种属性
    """
    pass


# =============================================================================
# 主程序示例
# =============================================================================

def main():
    """主程序示例"""
    print("=== 数据类示例 ===")
    
    # 基础数据类示例
    print("\n1. 基础数据类:")
    try:
        person = Person("Alice", 25, "alice@example.com")
        print(f"Person: {person}")
        print(f"Is adult: {person.is_adult()}")
    except Exception as e:
        print(f"未实现: {e}")
    
    # 不可变数据类示例
    print("\n2. 不可变数据类:")
    try:
        point1 = ImmutablePoint(1.0, 2.0)
        point2 = ImmutablePoint(3.0, 4.0)
        result = point1 + point2
        print(f"Point addition: {point1} + {point2} = {result}")
    except Exception as e:
        print(f"未实现: {e}")
    
    print("\n=== 运行 'python -m exercises.chapter14_dataclasses' 查看更多示例 ===")


if __name__ == "__main__":
    main() 