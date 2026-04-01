# 文件: user.py
import datetime
class UserNameMMTestForSearch:
    """用户类，表示系统中的用户"""

    def __init__(self, username: str, email: str, age: int):
        """初始化用户对象

        Args:
            username: 用户名
            email: 电子邮箱
            age: 年龄
        """
        self.username = username
        self.email = email
        self.age = age
        self.is_active = True
        self.created_at = datetime.now()

    @property
    def display_name(self) -> str:
        """获取显示名称"""
        return f"{self.username} ({self.email})"

    @property
    def is_adult(self) -> bool:
        """判断是否为成年人"""
        return self.age >= 18

    def activate(self) -> None:
        """激活用户"""
        self.is_active = True

    def deactivate(self) -> None:
        """停用用户"""
        self.is_active = False

    def update_email(self, new_email: str) -> bool:
        """更新邮箱地址

        Args:
            new_email: 新的邮箱地址

        Returns:
            bool: 更新是否成功
        """
        if self._validate_email(new_email):
            self.email = new_email
            return True
        return False

    def _validate_email(self, email: str) -> bool:
        """验证邮箱格式（内部方法）"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def __str__(self) -> str:
        """字符串表示"""
        status = "active" if self.is_active else "inactive"
        return f"User(username={self.username}, email={self.email}, age={self.age}, status={status})"

    def __repr__(self) -> str:
        """详细表示"""
        return f"<User {self.username} at {id(self)}>"