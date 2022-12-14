"""# iife

## Immediately-invoked function expressions in Python

The `iife` package provides a decorator function `iife` that calls the function/class it decorates and assigns the result to the name of the function/class.

## The entire package:

This is the entire package (`iife.py`):

```python
from typing import Callable, TypeVar

T = TypeVar("T")

def iife(c: Callable[[], T]) -> T:
    return c()
```

That's it.

Some use cases include...

## Creating an anonymous object.

Have you ever written a class that you know will only have one instance? You can use the iife decorator to create that instance immediately.

```python
@iife
@dataclass
class player:
    x: int = 1
    y: int = 2

# player is an instance of the player class
player.x # -> 1

# The class cannot be reinstantiated because the name is shadowed.
new_player = player(x=3, y=4) # -> SyntaxError
```

This might also be useful in library development to hide the implementation details of the class from the end user, who can only access the single instance.

## Complex initialization.

Sometimes a variable needs to be initialized by complex logic that cannot be expressed as a single assignment. Traditionally, this can be done with temporarily setting the variable to a default value:

```python
x = None
y = [1, 2, 3]
for i in y:
    if i == 2:
        x = i
```

Why not do it with an IIFE? (To be honest, this isn't the best example, but it's more fun to do it like this.)

```python
@iife
def x() -> Optional[int]:
    y = [1, 2, 3]
    for i in y:
        if i == 2:
            return i
```

... And a bunch more. Maybe. Tbh this is mostly for fun."""

from asyncio import iscoroutinefunction
from typing import Any, Callable, Coroutine, Optional, TypeVar, overload

T = TypeVar("T")


@overload
def iife(c: Callable[[], T], /, **kwargs) -> T:
    ...


# TODO: async functions
# Should async IIFEs evaluate to the coroutine or run the coroutine and await the result?
@overload
def iife(c: Callable[[], Coroutine[Any, Any, T]], /, **kwargs) -> T:
    ...


@overload
def iife(c=None, /, **kwargs) -> Callable[[Callable[..., T]], T]:
    ...


def iife(
    c: Optional[Callable[[], T | Coroutine[Any, Any, T]]] = None, /, **kwargs
) -> T | Callable[[Callable[..., T | Coroutine[Any, Any, T]]], T]:
    """Call the function/class and assign the result to the name of the function/class."""
    if iscoroutinefunction(c):
        raise NotImplementedError("iife cannot be used with async functions yet")

    if isinstance(c, Callable) and not kwargs:
        return c()

    else:

        def inner(c: Callable[..., T | Coroutine[Any, Any, T]]) -> T:
            if iscoroutinefunction(c):
                raise NotImplementedError(
                    "iife cannot be used with async functions yet"
                )
            else:
                return c(**kwargs)  # type: ignore

        return inner
