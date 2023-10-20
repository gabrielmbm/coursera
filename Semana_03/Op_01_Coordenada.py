# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem
# corresponder, respectivamente, às coordenadas x e y de um ponto em um
# plano cartesiano. Os dois últimos devem corresponder, respectivamente,
# às coordenadas x e y de um outro ponto no mesmo plano.
# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, imprima
# longe
#Caso o contrário, quando a distância for menor que 10, imprima
# perto

import math

x1 = int(input('Digite a coordenada X1: '))
y1 = int(input('Digite a coordenada Y1: '))

x2 = int(input('Digite a coordenada X2: '))
y2 = int(input('Digite a coordenada Y2: '))

d = math.sqrt((x1-x2)**2 + (y1-y2)**2)

if d >= 10:
    print('longe')
else:
    print('perto')