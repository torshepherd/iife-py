"""# IIFE (immediately-invoked function expressions)

The `iife` package provides a decorator function `iife` that calls the function/class it decorates and assigns the result to the name of the function/class.

Some use cases include

## Creating an anonymous object.

Have you ever written a class that you know will only have one instance? You can use the iife decorator to create that instance immediately.

```python
@iife
@dataclass
class player:
    x: int = 1
    y: int = 2

# player is an instance of the player class, but the class cannot be reinstantiated because the name is shadowed.
player(x=3, y=4) # SyntaxError
player.x # 1
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

from .iife import iife
