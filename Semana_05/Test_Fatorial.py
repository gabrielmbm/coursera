# def fatorial (n):
#     i = fat = 1
#     while i <= n:
#         fat = fat * i
#         i += 1
#     return fat

def fatorial (x):
    if x == 0:
        return 1
    elif x < 0:
        return 0
    else:
        y = 1
        while x != 0:
            y = x * y
            x -= 1
        return y

def test_fatorial0():
    assert fatorial(0) == 1

def test_fatorial1():
    assert fatorial(1) == 1

def test_fatorial_negativo():
    assert fatorial(-10) == 0

def test_fatorial4():
    assert fatorial(4) == 24

def test_fatorial5():
    assert fatorial(5) == 120