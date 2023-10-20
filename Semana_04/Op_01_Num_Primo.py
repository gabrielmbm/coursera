# Exercício 1
# Escreva um programa que receba um número inteiro positivo
# na entrada e verifique se é primo. Se o número for primo,
# imprima "primo". Caso contrário, imprima "não primo".

x = int(input('Digite um número inteiro: '))
i = 0
anterior = x
y = 0

while anterior >= 1 or i < 2:
    y = x % anterior
    if y == 0:
        i += 1
        anterior -= 1
    else:
        anterior -= 1

if i == 2:
    print('primo')
else:
    print('não primo')