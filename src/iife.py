from typing import Callable, TypeVar


T = TypeVar("T")


def iife(c: Callable[[], T]) -> T:
    return c()
