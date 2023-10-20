# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os n primeiros
# números ímpares naturais. Para a saída, siga o formato do exemplo abaixo.
# Exemplo:
# Digite o valor de n: 5
# 1
# 3
# 5
# 7
# 9

x = int(input('Digite o valor de n: '))

if x == 0:
    print('Sequência inválida.')
else:
    i = 1
    j = i

    while i <= x:
        print(j)
        i += 1
        j += 2