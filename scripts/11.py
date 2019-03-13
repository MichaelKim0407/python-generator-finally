__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    except ValueError:
        print('ValueError in f1')
    finally:
        print(i)


def f2():
    for i in f1():
        if i == 5:
            raise ValueError


if __name__ == '__main__':
    try:
        f2()
    except ValueError:
        pass

# Output
"""
5
"""

# Works with exceptions, too
# Note that the ValueError raised in `f2` will not affect `f1`'s `except` block
