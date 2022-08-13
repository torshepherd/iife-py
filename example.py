from iife import iife

# `iife` can be called with kwargs
@iife(x=True)
def f(x: bool):
    temp = 42
    return temp if x else 0


# The function `f` is evaluated and stored
# in the shadowing variable `f`
_ = f
print(f)  # -> 42

# Temporary variables used in initialization
# don't pollute the global namespace
temp  # -> NameError: name 'temp' is not defined


# `iife` can also be called with no args
@iife
class cout:
    def __lshift__(self, other):
        print(other)


cout << "Hello World!"
# The class `cout` is shadowed and inaccessible
# to users, effectively making it anonymous.
