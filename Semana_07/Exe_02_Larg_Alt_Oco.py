largura = int(input('Digite a largura: '))
while largura <= 0:
    largura = int(input('Digite a largura: '))
larg = largura

altura = int(input('Digite a altura: '))
while altura <= 0:
    altura = int(input('Digite a altura: '))
alt = altura

while alt > 0:
    if alt == altura:
        while larg > 0:
            print('#', end='')
            larg -= 1
        print()
        #alt -= 1
        larg = largura
    elif alt == 1:
        while larg > 0:
            print('#', end='')
            larg -= 1
        print()
        #alt -= 1
        larg = largura
    else:
        while larg > 0:
            if larg == largura:
                print('#', end='')
            elif larg == 1:
                print('#', end='')
                print()
            else:
                print(' ', end='')
            #print()
            larg -= 1
        larg = largura
    alt -= 1