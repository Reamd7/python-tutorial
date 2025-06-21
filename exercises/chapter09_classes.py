"""
第9章：类 - 练习题

本章节练习基于 Python 官方教程第9章：类
参考：https://docs.python.org/zh-cn/3/tutorial/classes.html

涵盖内容：
- 类定义语法
- 实例对象和方法对象
- 类和实例变量
- 继承
- 私有变量
- 迭代器
- 生成器
"""


class BankAccount:
    """
    练习 9.3: 银行账户类
    
    实现一个基本的银行账户类，包含存款、取款、查询余额等功能
    """
    
    # 类变量：银行名称
    bank_name = "Python银行"
    
    def __init__(self, account_number, owner, initial_balance=0):
        """
        初始化银行账户
        
        Args:
            account_number (str): 账户号码
            owner (str): 账户所有者
            initial_balance (float): 初始余额，默认为0
        """
        # TODO: 初始化实例变量
        pass
    
    def deposit(self, amount):
        """
        存款
        
        Args:
            amount (float): 存款金额
        
        Returns:
            bool: 操作是否成功
        """
        # TODO: 实现存款功能
        # 检查金额是否有效（大于0）
        pass
    
    def withdraw(self, amount):
        """
        取款
        
        Args:
            amount (float): 取款金额
        
        Returns:
            bool: 操作是否成功
        """
        # TODO: 实现取款功能
        # 检查金额是否有效且余额充足
        pass
    
    def get_balance(self):
        """
        获取账户余额
        
        Returns:
            float: 当前余额
        """
        # TODO: 返回当前余额
        pass
    
    def __str__(self):
        """
        字符串表示
        
        Returns:
            str: 账户信息字符串
        """
        # TODO: 返回账户信息的字符串表示
        pass
    
    def __repr__(self):
        """
        官方字符串表示
        
        Returns:
            str: 账户的官方字符串表示
        """
        # TODO: 返回可重建对象的字符串表示
        pass


class SavingsAccount(BankAccount):
    """
    练习 9.5: 储蓄账户类（继承练习）
    
    继承 BankAccount，添加利息功能
    """
    
    def __init__(self, account_number, owner, initial_balance=0, interest_rate=0.02):
        """
        初始化储蓄账户
        
        Args:
            account_number (str): 账户号码
            owner (str): 账户所有者
            initial_balance (float): 初始余额
            interest_rate (float): 年利率，默认2%
        """
        # TODO: 调用父类构造器并设置利率
        pass
    
    def add_interest(self):
        """
        添加利息到账户
        
        Returns:
            float: 添加的利息金额
        """
        # TODO: 计算并添加利息
        pass
    
    def withdraw(self, amount):
        """
        重写取款方法，储蓄账户每次取款收取手续费
        
        Args:
            amount (float): 取款金额
        
        Returns:
            bool: 操作是否成功
        """
        # TODO: 重写取款方法，增加手续费逻辑
        # 手续费为固定2元
        pass


class Person:
    """
    练习 9.3.5: 人员类（类变量和实例变量）
    """
    
    # 类变量
    species = "Homo sapiens"
    population = 0
    
    def __init__(self, name, age):
        """初始化人员"""
        # TODO: 设置实例变量并更新人口计数
        pass
    
    @classmethod
    def get_population(cls):
        """获取人口总数"""
        # TODO: 返回类变量 population
        pass
    
    @staticmethod
    def is_adult(age):
        """判断是否成年"""
        # TODO: 判断年龄是否>=18
        pass
    
    def __del__(self):
        """析构函数"""
        # TODO: 更新人口计数
        pass


class Counter:
    """
    练习 9.8: 迭代器类
    
    实现一个计数器迭代器
    """
    
    def __init__(self, start=0, end=10):
        """
        初始化计数器
        
        Args:
            start (int): 起始值
            end (int): 结束值（不包含）
        """
        # TODO: 初始化迭代器状态
        pass
    
    def __iter__(self):
        """返回迭代器对象本身"""
        # TODO: 返回 self
        pass
    
    def __next__(self):
        """返回下一个值"""
        # TODO: 实现迭代逻辑
        # 当达到结束值时抛出 StopIteration
        pass


def fibonacci_generator(n):
    """
    练习 9.9: 生成器函数 - 斐波那契数列
    
    Args:
        n (int): 生成前 n 个斐波那契数
    
    Yields:
        int: 斐波那契数
    """
    # TODO: 使用 yield 实现斐波那契生成器
    pass


def prime_generator(limit):
    """
    练习 9.9: 生成器函数 - 素数生成器
    
    Args:
        limit (int): 生成小于 limit 的素数
    
    Yields:
        int: 素数
    """
    # TODO: 使用 yield 实现素数生成器
    pass


class Rectangle:
    """
    练习 9.4: 几何图形类（特殊方法）
    """
    
    def __init__(self, width, height):
        """初始化矩形"""
        # TODO: 设置宽度和高度
        pass
    
    def area(self):
        """计算面积"""
        # TODO: 返回面积
        pass
    
    def perimeter(self):
        """计算周长"""
        # TODO: 返回周长
        pass
    
    def __eq__(self, other):
        """等于比较"""
        # TODO: 比较两个矩形是否相等
        pass
    
    def __lt__(self, other):
        """小于比较（按面积）"""
        # TODO: 按面积比较大小
        pass
    
    def __add__(self, other):
        """加法操作（面积相加）"""
        # TODO: 返回面积之和
        pass
    
    def __str__(self):
        """字符串表示"""
        # TODO: 返回矩形描述
        pass


class Circle:
    """
    练习 9.5: 圆形类（多重继承练习的基类）
    """
    
    def __init__(self, radius):
        """初始化圆形"""
        # TODO: 设置半径
        pass
    
    def area(self):
        """计算面积"""
        # TODO: 返回圆形面积（π * r²）
        # 可以使用 math.pi
        pass
    
    def circumference(self):
        """计算周长"""
        # TODO: 返回圆形周长（2 * π * r）
        pass


# 辅助函数用于测试
def test_bank_account():
    """测试银行账户类"""
    try:
        account = BankAccount("123456", "张三", 1000)
        print(f"创建账户: {account}")
        
        print(f"存款500: {account.deposit(500)}")
        print(f"当前余额: {account.get_balance()}")
        
        print(f"取款200: {account.withdraw(200)}")
        print(f"当前余额: {account.get_balance()}")
        
        print(f"尝试取款2000: {account.withdraw(2000)}")
        print(f"最终余额: {account.get_balance()}")
        
    except Exception as e:
        print(f"银行账户测试失败: {e}")


def test_inheritance():
    """测试继承"""
    try:
        savings = SavingsAccount("789012", "李四", 1000, 0.03)
        print(f"储蓄账户: {savings}")
        
        interest = savings.add_interest()
        print(f"添加利息: {interest}")
        print(f"余额: {savings.get_balance()}")
        
        print(f"取款100: {savings.withdraw(100)}")
        print(f"最终余额: {savings.get_balance()}")
        
    except Exception as e:
        print(f"继承测试失败: {e}")


def test_iterators_and_generators():
    """测试迭代器和生成器"""
    try:
        # 测试计数器迭代器
        print("计数器迭代器:")
        counter = Counter(0, 5)
        for num in counter:
            print(num, end=" ")
        print()
        
        # 测试斐波那契生成器
        print("斐波那契生成器:")
        fib_gen = fibonacci_generator(8)
        for num in fib_gen:
            print(num, end=" ")
        print()
        
        # 测试素数生成器
        print("素数生成器:")
        prime_gen = prime_generator(20)
        for prime in prime_gen:
            print(prime, end=" ")
        print()
        
    except Exception as e:
        print(f"迭代器和生成器测试失败: {e}")


if __name__ == "__main__":
    print("第9章：类 - 练习题")
    print("=" * 40)
    
    print("9.3 银行账户类测试：")
    test_bank_account()
    
    print("\n9.5 继承测试：")
    test_inheritance()
    
    print("\n9.8-9.9 迭代器和生成器测试：")
    test_iterators_and_generators()
    
    print("\n请实现上述类和方法，然后运行 pytest tests/ 验证实现！") 