from pytest import raises

from iife import iife


def test_iife_function_no_args():
    @iife
    def func():
        return 1

    assert func == 1


def test_iife_function_with_args():
    @iife(p=1)
    def func(p):
        return p

    @iife(c=1)
    def func2(c):
        return c

    assert func == 1
    assert func2 == 1


def test_iife_class_no_args():
    @iife
    class cls:
        def __init__(self):
            self.value = 1

    assert cls.value == 1


def test_iife_class_with_args():
    @iife(val=1)
    class cls:
        def __init__(self, val: int):
            self.value = val

    assert cls.value == 1


def test_iife_async_function_no_args():
    with raises(NotImplementedError):

        @iife
        async def func():
            return 1

        assert func == 1


def test_iife_async_function_with_args():
    with raises(NotImplementedError):

        @iife(p=1)
        async def func(p):
            return p

        assert func == 1

    with raises(NotImplementedError):

        @iife(c=1)
        async def func2(c):
            return c

        assert func2 == 1


# def test_iife_generator_no_args():
#     @iife
#     def func():
#         yield from [1, 2, 3]

#     assert func == 1


# def test_iife_generator_with_args():
#     @iife(stop=3)
#     def func(stop: int):
#         yield from range(stop)

#     assert func == 1
