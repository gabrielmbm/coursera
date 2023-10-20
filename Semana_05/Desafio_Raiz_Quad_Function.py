# O programa deve receber os parâmetros 
# a, b e c da equação de segundo grau respectivamente,
# e imprimir o resultado na saída da seguinte maneira:
# Quando não houver raízes reais imprima:
# esta equação não possui raízes reais
# Quando houver apenas uma raiz (ou seja, uma raiz com multiplicidade 2) imprima:
# a raiz desta equação é X
# ou
# a raiz dupla desta equação é X
# onde X é o valor da raiz dupla
# Quando houver duas raízes reais imprima:
# as raízes da equação são X e Y
# onde X e Y são os valor das raízes.
# Além disso, no caso de existirem 2 raízes reais distintas,
# elas devem ser impressas em ordem crescente. Exemplos:
# as raízes da equação são 1.0 e 2.0
# as raízes da equação são -2.0 e 0.0

import math

a = int(input('Digite a: '))
b = int(input('Digite b: '))
c = int(input('Digite c: '))

d = b**2 - (4*a*c)

if d < 0:
    print('Esta equação não possui raízes reais.')
elif d == 0:
    x = (-b)/(2*a)
    print('A raiz desta equação é',x)
else:
    x1 = ((-b)+math.sqrt(d))/(2*a)
    x2 = ((-b)-math.sqrt(d))/(2*a)
    if x2 > x1:
        print('As raízes da equação são',x1,'e',x2)
    else:
        print('As raízes da equação são',x2,'e',x1)