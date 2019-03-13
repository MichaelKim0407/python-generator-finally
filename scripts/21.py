__author__ = 'Michael'


def f1():
    i = -1
    try:
        for i in range(10):
            yield i
    finally:
        print(i)


def f2():
    iterable = f1()
    for i in iterable:
        if i == 5:
            print('break')
            break
    print('f2 returns')


if __name__ == '__main__':
    f2()
    print('exit')

# Output
"""
break
f2 returns
5
exit
"""

# End-of-life is reached when `f2` returns
# (after line 18)
