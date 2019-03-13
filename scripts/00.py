__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    finally:
        print(i)


if __name__ == '__main__':
    f1()

# Output
"""
"""

# No output because the generator is not iterated!

# If you got back to this script after reading others and got confused,
# I did too, for a second..
# The reason `finally` block is not executed is that `try` block is not entered yet.
