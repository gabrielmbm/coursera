# Verifica se o número é divisível por 3
num = int(input("Digite o número: "))
rest = num % 3

if rest == 0:
    print('Fizz')
else:
    print(num)