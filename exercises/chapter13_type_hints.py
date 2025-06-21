"""
第13章：类型提示 (Type Hints)
Type Hints and Static Typing

本章涵盖：
- 基础类型注解
- 复合类型：List, Dict, Tuple, Set
- Optional 和 Union 类型
- 泛型 (Generics)
- 类型别名 (Type Aliases)
- 协议 (Protocols)
- TypedDict 和 NamedTuple
- mypy 静态类型检查
"""

from typing import (
    List, Dict, Tuple, Set, Optional, Union, Any, Callable,
    TypeVar, Generic, Protocol, overload, cast, Final
)
from typing_extensions import TypedDict, Literal
from dataclasses import dataclass
from collections.abc import Iterable
import json


# =============================================================================
# 1. 基础类型注解
# =============================================================================

def greet_user(name: str, age: int) -> str:
    """
    TODO: 实现带类型注解的函数
    - 接受 name (字符串) 和 age (整数)
    - 返回格式化的问候语: "Hello {name}, you are {age} years old!"
    """
    pass


def calculate_bmi(weight: float, height: float) -> float:
    """
    TODO: 计算BMI指数
    - 使用公式: weight / (height * height)
    - 返回计算结果，保留2位小数
    """
    pass


def is_adult(age: int) -> bool:
    """
    TODO: 判断是否成年
    - 年龄 >= 18 返回 True，否则返回 False
    """
    pass


# =============================================================================
# 2. 复合类型
# =============================================================================

def process_numbers(numbers: List[int]) -> Dict[str, Union[int, float]]:
    """
    TODO: 处理数字列表
    - 计算总和、平均值、最大值、最小值
    - 返回包含这些统计信息的字典
    - 键为: 'sum', 'average', 'max', 'min'
    """
    pass


def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    """
    TODO: 按长度分组单词
    - 将单词按长度分组
    - 返回字典，键为长度，值为该长度的单词列表
    """
    pass


def merge_dictionaries(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """
    TODO: 合并两个字典
    - 如果键重复，使用两个值的和
    - 返回合并后的字典
    """
    pass


def extract_coordinates(points: List[Tuple[float, float]]) -> Tuple[List[float], List[float]]:
    """
    TODO: 提取坐标点
    - 从坐标点列表中分别提取x和y坐标
    - 返回 (x坐标列表, y坐标列表) 的元组
    """
    pass


# =============================================================================
# 3. Optional 和 Union 类型
# =============================================================================

def find_user_by_id(user_id: int, users: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    TODO: 根据ID查找用户
    - 在用户列表中查找指定ID的用户
    - 找到返回用户字典，未找到返回 None
    """
    pass


def parse_number(value: Union[str, int, float]) -> Optional[float]:
    """
    TODO: 解析数字
    - 如果是字符串，尝试转换为浮点数
    - 如果是数字，直接转换为浮点数
    - 转换失败返回 None
    """
    pass


def safe_divide(a: Union[int, float], b: Union[int, float]) -> Optional[float]:
    """
    TODO: 安全除法
    - 执行除法运算，避免除零错误
    - 除零时返回 None
    """
    pass


# =============================================================================
# 4. 类型别名
# =============================================================================

# TODO: 定义类型别名
UserId = int
UserName = str
User = Dict[str, Union[str, int]]
UserList = List[User]
Point = Tuple[float, float]
Matrix = List[List[float]]


def create_user(user_id: UserId, name: UserName, email: str) -> User:
    """
    TODO: 创建用户
    - 使用定义的类型别名
    - 返回用户字典
    """
    pass


def calculate_distance(point1: Point, point2: Point) -> float:
    """
    TODO: 计算两点间距离
    - 使用欧几里得距离公式
    - 返回距离值
    """
    pass


def matrix_multiply(matrix1: Matrix, matrix2: Matrix) -> Optional[Matrix]:
    """
    TODO: 矩阵乘法
    - 检查矩阵维度是否兼容
    - 执行矩阵乘法
    - 不兼容时返回 None
    """
    pass


# =============================================================================
# 5. 泛型 (Generics)
# =============================================================================

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')


class Stack(Generic[T]):
    """
    TODO: 实现泛型栈
    """
    
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def push(self, item: T) -> None:
        """TODO: 压入元素"""
        pass
    
    def pop(self) -> Optional[T]:
        """TODO: 弹出元素，空栈返回None"""
        pass
    
    def peek(self) -> Optional[T]:
        """TODO: 查看栈顶元素，不弹出"""
        pass
    
    def is_empty(self) -> bool:
        """TODO: 检查栈是否为空"""
        pass
    
    def size(self) -> int:
        """TODO: 返回栈的大小"""
        pass


class Cache(Generic[K, V]):
    """
    TODO: 实现泛型缓存
    """
    
    def __init__(self, max_size: int = 100) -> None:
        self.data: Dict[K, V] = {}
        self.max_size = max_size
    
    def get(self, key: K) -> Optional[V]:
        """TODO: 获取缓存值"""
        pass
    
    def set(self, key: K, value: V) -> None:
        """TODO: 设置缓存值，超出大小时删除最旧的"""
        pass
    
    def clear(self) -> None:
        """TODO: 清空缓存"""
        pass


def get_first_item(items: List[T]) -> Optional[T]:
    """
    TODO: 获取列表第一个元素
    - 泛型函数示例
    - 空列表返回 None
    """
    pass


def swap_elements(items: List[T], index1: int, index2: int) -> List[T]:
    """
    TODO: 交换列表中的两个元素
    - 返回交换后的新列表
    - 索引无效时返回原列表
    """
    pass


# =============================================================================
# 6. 协议 (Protocols)
# =============================================================================

class Drawable(Protocol):
    """绘制协议"""
    
    def draw(self) -> str:
        """绘制方法"""
        ...
    
    def area(self) -> float:
        """面积计算"""
        ...


class Circle:
    """
    TODO: 实现圆形类
    - 实现 Drawable 协议
    """
    
    def __init__(self, radius: float) -> None:
        self.radius = radius
    
    def draw(self) -> str:
        """TODO: 返回圆形的描述"""
        pass
    
    def area(self) -> float:
        """TODO: 计算圆的面积"""
        pass


class Rectangle:
    """
    TODO: 实现矩形类
    - 实现 Drawable 协议
    """
    
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
    
    def draw(self) -> str:
        """TODO: 返回矩形的描述"""
        pass
    
    def area(self) -> float:
        """TODO: 计算矩形面积"""
        pass


def draw_shapes(shapes: List[Drawable]) -> List[str]:
    """
    TODO: 绘制形状列表
    - 调用每个形状的draw方法
    - 返回描述列表
    """
    pass


def total_area(shapes: List[Drawable]) -> float:
    """
    TODO: 计算总面积
    - 计算所有形状的面积总和
    """
    pass


# =============================================================================
# 7. TypedDict 和 结构化数据
# =============================================================================

class PersonDict(TypedDict):
    """TODO: 定义人员字典类型"""
    name: str
    age: int
    email: str
    is_active: bool


class AddressDict(TypedDict, total=False):
    """TODO: 定义地址字典类型（所有字段可选）"""
    street: str
    city: str
    state: str
    zip_code: str


def create_person(name: str, age: int, email: str) -> PersonDict:
    """
    TODO: 创建人员记录
    - 返回符合 PersonDict 类型的字典
    - is_active 默认为 True
    """
    pass


def update_person_email(person: PersonDict, new_email: str) -> PersonDict:
    """
    TODO: 更新人员邮箱
    - 创建新的PersonDict，更新邮箱字段
    """
    pass


def validate_person(data: Dict[str, Any]) -> bool:
    """
    TODO: 验证人员数据
    - 检查是否包含所有必需字段
    - 检查字段类型是否正确
    """
    pass


# =============================================================================
# 8. 高级类型特性
# =============================================================================

@dataclass
class Product:
    """商品数据类"""
    id: int
    name: str
    price: float
    category: str
    in_stock: bool = True


def filter_products(
    products: List[Product], 
    predicate: Callable[[Product], bool]
) -> List[Product]:
    """
    TODO: 过滤商品
    - 使用给定的谓词函数过滤商品列表
    """
    pass


@overload
def get_config(key: str) -> str: ...

@overload
def get_config(key: str, default: int) -> Union[str, int]: ...

def get_config(key: str, default: Any = None) -> Any:
    """
    TODO: 获取配置值
    - 模拟配置获取，支持重载
    - 如果key为"debug"返回"false"，为"port"返回"8080"
    - 其他情况返回default
    """
    pass


# 字面量类型
StatusType = Literal["pending", "approved", "rejected"]

def update_status(item_id: int, status: StatusType) -> Dict[str, Any]:
    """
    TODO: 更新状态
    - status 只能是指定的字面量值
    - 返回包含id和status的字典
    """
    pass


# Final 类型
API_VERSION: Final[str] = "v1.0"
MAX_RETRY_COUNT: Final[int] = 3

def get_api_info() -> Dict[str, Union[str, int]]:
    """
    TODO: 获取API信息
    - 返回包含版本和最大重试次数的字典
    """
    pass


# =============================================================================
# 9. 类型检查工具函数
# =============================================================================

def type_safe_json_loads(json_str: str) -> Dict[str, Any]:
    """
    TODO: 类型安全的JSON解析
    - 解析JSON字符串
    - 确保返回字典类型
    - 解析失败时返回空字典
    """
    pass


def type_safe_get(data: Dict[str, Any], key: str, expected_type: type) -> Any:
    """
    TODO: 类型安全的字典取值
    - 获取字典中的值
    - 检查值的类型是否符合期望
    - 类型不匹配时返回None
    """
    pass


# =============================================================================
# 10. 示例和测试
# =============================================================================

def demonstrate_type_hints() -> None:
    """演示类型提示的使用"""
    print("=== 类型提示示例 ===")
    
    # 基础类型
    print("\n1. 基础类型:")
    try:
        greeting = greet_user("Alice", 25)
        print(f"问候: {greeting}")
    except Exception as e:
        print(f"未实现: {e}")
    
    # 复合类型
    print("\n2. 复合类型:")
    try:
        numbers = [1, 2, 3, 4, 5]
        stats = process_numbers(numbers)
        print(f"统计: {stats}")
    except Exception as e:
        print(f"未实现: {e}")
    
    # 泛型
    print("\n3. 泛型:")
    try:
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        print(f"栈顶: {stack.peek()}")
    except Exception as e:
        print(f"未实现: {e}")


if __name__ == "__main__":
    demonstrate_type_hints()
    print("\n=== 运行 'mypy exercises/chapter13_type_hints.py' 进行静态类型检查 ===") 