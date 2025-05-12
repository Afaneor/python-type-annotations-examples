from typing import ClassVar


class ExampleClass:
    a: int
    b: ClassVar[int]

example = ExampleClass()
example.a = '123'
example.a = 123

example.b = 456
ExampleClass.b = 789
