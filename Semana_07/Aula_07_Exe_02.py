# Dado um número inteiro n, n > 1, imprimir sua decomposição em fatores primos,
# indicando também a multiplicidade em cada fator, exemplo:
#
# 8 = 2 * 2 * 2
# 20 = 2 * 2 * 5
# 1000 = 2^3 * 5^3
#
# Exercício feito em conjunto com o professor.
def fatoresPrimos():
    n = int(input('Digite um número inteiro > 1: '))

    fator = 2
    multiplicidade = 0

    while n > 1:
        while (n % fator) == 0:
            multiplicidade += 1
            n = n / fator
        if multiplicidade > 0:
            print('Fator', fator, 'multiplicidade =', multiplicidade)
        fator += 1
        multiplicidade = 0

def numeroPrimo():
    n = int(input('Digite um número inteiro: '))
    while n > 0:
        if primo(n):
            print(n,'é primo.')
        else:
            print(n,'não é primo.')
        n = int(input('Digite um número inteiro: '))

def primo(x):
    fator = 2
    if x == 2:
        return True
    while (x % fator) != 0 and fator <= (x / 2):
        fator += 1
    if (x % fator) == 0:
        return False
    else:
        return True
    
numeroPrimo()