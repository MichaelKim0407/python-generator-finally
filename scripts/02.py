__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
            if i == 5:
                return
    finally:
        print(i)


if __name__ == '__main__':
    for i in f1():
        pass

# Output
"""
5
"""

# Naturally, `finally` works if we break out of the generator from within
