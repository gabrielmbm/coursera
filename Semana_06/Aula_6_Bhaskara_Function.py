import math

def main():
    a = float(input('Digite a: '))
    b = float(input('Digite b: '))
    c = float(input('Digite c: '))
    imprime_raizes(a, b, c)

def delta (a, b, c):
    return b**2 - (4*a*c)

def imprime_raizes(a, b, c):
    d = delta (a, b, c)
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

main()