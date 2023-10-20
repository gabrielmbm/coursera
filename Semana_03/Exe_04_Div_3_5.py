# Verifica se o número é divisível por 3 e por 5
num = int(input("Digite o número: "))
rest1 = num % 3
rest2 = num % 5

if rest1 == 0 and rest2 == 0:
    print('FizzBuzz')
else:
    print(num)