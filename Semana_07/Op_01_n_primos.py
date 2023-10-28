# Exercício 1 - Primos
# Escreva a função n_primos que recebe como argumento um número inteiro
# maior ou igual a 2 como parâmetro e devolve a quantidade de números primos
# que existem entre 2 e n (incluindo 2 e, se for o caso, n)
# 
# Exemplo:
# >>> n_primos(2)
# 1
# >>> n_primos(4)
# 2
# >>> n_primos(121)
# 30

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

def n_primos(n):
    i = 0
    while n >= 2:
        nPrimo = primo(n)
        if nPrimo == True:
            i += 1
        n -= 1
    print(i)
    return i