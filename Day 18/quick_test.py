def fun1():
    print('fun1')
    return False


def fun2():
    print('fun2')
    return True


while fun1() or fun2():
    print('while')
    break