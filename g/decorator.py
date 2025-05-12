import logging
from typing import Callable, ParamSpec, TypeVar

# P = ParamSpec('P')  # python 3.11<=
# T = TypeVar('T')

def add_logging[**P, T](f: Callable[P, T]) -> Callable[P, T]:
    """A type-safe decorator to add logging to a function."""
    def inner(*args: P.args, **kwargs: P.kwargs) -> T:
        logging.info(f'{f.__name__} was called')
        return f(*args, **kwargs)
    return inner

@add_logging
def add_two(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y
