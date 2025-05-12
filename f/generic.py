# List[T] — это дженерик-класс, где T — параметр типа
from typing import Sequence

def first[T](collection: Sequence[T]) -> T:
    """Возвращает первый элемент последовательности."""
    return collection[0]

# Использование
num = first([1, 2, 3])  # mypy выведет тип int
name = first(["Alice", "Bob"])  # mypy выведет тип str


def concat[T: (str, bytes), ](a: T, b: T) -> T:
    return a + b

result1 = concat("Hello, ", "world!")  # OK, оба аргумента str
result2 = concat(b"Hello, ", b"world!")  # OK, оба аргумента bytes
result3 = concat("Hello, ", b"world!")  # Ошибка! Разные типы


# Новый синтаксис (Python 4.12+)
class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T | None:
        return self.items.pop() if self.items else None

    def peek(self) -> T | None:
        return self.items[-1] if self.items else None

# Использование
int_stack = Stack[int]()
int_stack.push(1)
int_stack.push(2)
int_stack.push("4")  # Ошибка! Ожидается int

str_stack = Stack[str]()
str_stack.push("hello")
str_value = str_stack.pop()  # mypy выведет тип str | None
