#Soma dos digitos de um número digita, exemplo:
#6532 -> 6 + 5 + 3 + 2 = 16

x = int(input('Digite o número: '))
y = 0

while x != 0:
    y = (x % 10) + y
    x = x // 10

print(y)