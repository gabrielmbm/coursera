# Exercício 2 - Desafio do vídeo "Repetição com while"
# Escreva um programa que receba um número inteiro na entrada e
# verifique se o número recebido possui ao menos um dígito com um
# dígito adjacente igual a ele. Caso exista, imprima "sim"; se não existir,
# imprima "não".

x = int(input('Digite um número inteiro: '))
algarismo = True
anterior = x % 10
y = 0

while x != 0 and algarismo:
    x = x // 10
    y = x % 10
    if y == anterior:
        algarismo = False
    else:
        anterior = y

if algarismo:
    print('não')
else:
    print('sim')