# Reescreva a função 'maximo' do outro exercício,
# que devolve o maior valor dentre dois inteiros recebidos,
# para que ela passe a receber 3 valores inteiros como parâmetros
# e devolva o maior dentre eles.

def maximo (x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z
    
def test_maximo1():
    assert maximo(30, 14, 10) == 30

def test_maximo2():
    assert maximo(0, -1, 1) == 1

def test_maximo3():
    assert maximo(10, 12, 11) == 12

def test_maximo4():
    assert maximo(2, 6, -4) == 6