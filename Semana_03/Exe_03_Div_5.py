# Verifica se o número é divisível por 5
num = int(input("Digite o número: "))
rest = num % 5

if rest == 0:
    print('Buzz')
else:
    print(num)