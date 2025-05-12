from typing import Callable, Awaitable


def apply_twice(func: Callable[
    [int, int],  # аргументы функции
    int  # возвращаемое значение
],
                x: int) -> int:
    func(x, x)
    return func(x, x)

def example_function(a: int, b: int) -> int:
    ...

def example_function2(a: str, b: str) -> str:
    ...

apply_twice(example_function, 2)
apply_twice(example_function2, 3)


async def async_example(a: int, b: int) -> int:
    ...

async def async_example_string(a: int, b: int) -> str:
    ...

async def call(coro: Awaitable[int]):
    await coro

call(async_example(1, 2))
call(async_example_string(1, 2))