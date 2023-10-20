def fatorial (x):
    if x == 0:
        return 1
    elif x < 0:
        return KeyError
    else:
        y = 1
        while x != 0:
            y = x * y
            x -= 1
        return y
    
def testeFatorial ():
    if fatorial(1) == 1:
        print('Fat 1 - Ok')
    if fatorial(0) == 1:
        print('Fat 0 - Ok')
    if fatorial(5) == 120:
        print('Fat 5 - Ok')

def numeroBinomial (n, k):
    return fatorial(n) / (fatorial(k)*fatorial(n-k))

#testeFatorial()

n = int(input('Digite o n: '))
k = int(input('Digite o k: '))

print(numeroBinomial(n, k))