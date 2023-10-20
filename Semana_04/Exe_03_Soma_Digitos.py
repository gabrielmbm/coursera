# Escreva um programa que receba um número inteiro na entrada,
# calcule e imprima a soma dos dígitos deste número na saída
# Exemplo:
# Digite um número inteiro: 123
# 6

x = int(input('Digite um número inteiro: '))
y = 0

while x != 0:
    y = (x % 10) + y
    x = x // 10

print(y)