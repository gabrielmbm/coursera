# Indicadores de peasagem usando variáveis booleanas

dec = True
anterior = int(input('Digite o primeiro número: '))
valor = 1

while valor != 0 and dec:
    valor = int(input('Digite o próximo número: '))
    if valor > anterior:
        dec = False
    anterior = valor

if dec:
    print('A sequência está em ordem decrescente.')
else:
    print('A sequência não está em ordem descrescente.')