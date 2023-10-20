# Verifica se o número digitado possui dois algarimos iguais em sequência, exemplo:
# 123321 -> Possui o 3 repetido
# 1234626246 -> Não possui algarismos repetidos

x = int(input('Digite o número: '))
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
    print('Número não contém algarismos iguais em sequência.')
else:
    print('Número contém algarismos iguais em sequência.')