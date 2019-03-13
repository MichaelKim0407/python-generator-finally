__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    finally:
        print(i)


def f2():
    for i in f1():
        if i == 5:
            break


if __name__ == '__main__':
    f2()

# Output
"""
5
"""

# `finally` block will be executed even if the generator ends prematurely
