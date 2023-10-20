# Escreva a função maior_primo que recebe um número inteiro maior
# ou igual a 2 como parâmetro e devolve o maior número primo menor
# ou igual ao número passado à função
#
# Exemplos de execução no shell do Python:
# >>> maior_primo(100)
# 97
# >>> maior_primo(7)
# 7

def primo (x):
    i = y = 0
    anterior = x

    while anterior >= 1 or i < 2:
        y = x % anterior
        anterior -= 1
        if y == 0:
            i += 1
    
    if i == 2:
        return x

def maior_primo (z):
    if primo(z) == z:
        return z
    else:
        ant = z - 1
        while primo(ant) != ant:
            ant -= 1
    return ant
    
def test_01():
    assert maior_primo(100) == 97

def test_02():
    assert maior_primo(7) == 7

# print(maior_primo(100))
# print(maior_primo(7))