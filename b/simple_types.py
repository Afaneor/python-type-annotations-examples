from typing import List, Dict, Optional, Union, Any, Final

# Простые типы
name: str = "Python"
age: int = 30
price: float = 99.99
is_available: bool = True

# Составные типы
users: list = ["Alice", "Bob"]  # Но лучше указать тип элементов!
users: list[str] = ["Alice", "Bob"]  # Python 3.9+
users: List[str] = ["Alice", "Bob"]  # Python 3.6-3.8 (с импортом)

users: tuple[str, int] = ("Alice", 1) # два элемента: строка и число
users: tuple[str, ...] = ("Alice", 'a', '2', '3') # много строк

# Словари и другие коллекции
counts: dict[str, int] = {"apples": 10, "oranges": 5}  # Python 3.9+
counts: Dict[str, int] = {"apples": 10, "oranges": 5}  # Python 3.6-3.8

# None и опциональные значения
user_id: Optional[int] = None  # int или None
user_id: int | None = None  # int или None

# Union — объединение типов
user_id: Union[int, str] = 1  # int или str

# В Python 3.10+ можно использовать синтаксис |
user_id: int | str = "abc123"  # То же самое, но короче

def greet(name: str) -> str:
    return f"Hello, {name}!"

# Несколько аргументов
def add_user(name: str, age: int, is_active: bool = True) -> None:
    """Добавляет пользователя в систему."""
    # Код добавления пользователя...
    print(f"Added user {name}, age {age}, active: {is_active}")


def get_data():
    ...

# Any — любой тип
data: Any = get_data()  # Когда тип неизвестен или может быть любым

# noinspection PyListCreation
final_list : Final[object] = object()  # Неизменяемый список
print(final_list.__doc__)
final_list = [1, 2, 3]  # Ошибка! final_list нельзя переопределить