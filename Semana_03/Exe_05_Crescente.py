# Pede para digitar 3 número e verifica se estão em ordem crescente
 
num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))

if num3 > num2 and num2 > num1:
    print('crescente')
else:
    print('não está em ordem crescente')