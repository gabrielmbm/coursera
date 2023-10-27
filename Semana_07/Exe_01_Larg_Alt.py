largura = int(input('Digite a largura: '))
while largura <= 0:
    largura = int(input('Digite a largura: '))
larg = largura

altura = int(input('Digite a altura: '))
while altura <= 0:
    altura = int(input('Digite a altura: '))

while altura > 0:
    while larg > 0:
        print('#', end='')
        larg -= 1
    print()
    altura -= 1
    larg = largura