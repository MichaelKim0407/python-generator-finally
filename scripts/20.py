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
            print('break')
            break
    print('f2 returns')


if __name__ == '__main__':
    f2()
    print('exit')

# Output
"""
break
5
f2 returns
exit
"""

# End-of-life is reached when the for loop breaks
# (before line 18)
