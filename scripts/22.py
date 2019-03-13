__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    finally:
        print(i)


def f2(iterable):
    for i in iterable:
        if i == 5:
            print('break')
            break
    print('f2 returns')


if __name__ == '__main__':
    f2(f1())
    print('exit')

# Output
"""
break
f2 returns
5
exit
"""

# End-of-life is reached after the `f2` call
# (before line 23)
