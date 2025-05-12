from typing import overload


@overload
def process(response: None) -> None:
    ...
@overload
def process(response: int) -> tuple[int, str]:
    ...
@overload
def process(response: bytes) -> str:
    ...

def process(response):
    ...  # actual implementation goes here

res = process(1)
a = res[0]

new = process(b'')
new.capitalize()


