# Exercício 1
# Escreva um programa que receba um número
# natural n na entrada e imprima n! (fatorial) na saída.
# Exemplo:
# Digite o valor de n: 5
# 120
# Dica: lembre-se que o fatorial de 0 vale 1!

x = int(input('Digite o valor de n: '))

if x == 0:
    print(1)
else:
    y = 1
    while x != 0:
        y = x * y
        x -= 1
    print(y)