__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    finally:
        print(i)


if __name__ == '__main__':
    for i in f1():
        pass

# Output
"""
9
"""

# Generator finishes with i = 9
