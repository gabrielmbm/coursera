# Testa se o número é par ou ímpar
num = int(input("Digite o número: "))
rest = num % 2

if rest == 0:
    print('par')
else:
    print('ímpar')