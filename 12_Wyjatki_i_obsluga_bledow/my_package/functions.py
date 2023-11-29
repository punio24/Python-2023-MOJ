

def function_with_error():
    l = [0]
    return l[6]


def ok_function():
    return function_with_error()

# POPRAWA

def function_with_error(i):
    l = [0]
    return l[i]

def ok_function():
    return function_with_error(6)