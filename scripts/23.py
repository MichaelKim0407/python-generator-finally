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
    iterable = f1()
    f2(iterable)
    print('exit')

# Output
"""
break
f2 returns
exit
5
"""

# End-of-life is reached when the script exits
# (after line 24)
