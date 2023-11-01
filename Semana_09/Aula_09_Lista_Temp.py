# Passo a passo do último exercício do professor
# 
# 1- Quebrar o problema em problemas menores
# 2- Testes automatizados
# 3- Refatoração

def MinMax(temperaturas):
    print('A menor temperatura foi: ', minima(temperaturas), 'C.')
    print('A maior temperatura foi: ', maxima(temperaturas), 'C.')

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

def testePontualMinima(temp, valorEsperado):
    valorCalc = minima(temp)
    if valorCalc != valorEsperado:
        print('Valor errado para array ', temp)
        print(
            'Valor esperado ', valorEsperado, '. Valor calculado ', valorCalc
        )
    else:
        print('Teste ok!')

def testa_minima():
    print('Iniciando os testes')
    testePontualMinima([0], 0)
    testePontualMinima([0, 0, 0, 0, 0, 0], 0)
    testePontualMinima([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0)
    testePontualMinima([30, 31, 32, 30, 24, 25, 26, 27, 28, 29, 26], 24)
    testePontualMinima([-12, -15, 0, 5, 2], -15)  
    print('Finalizando os testes')

def testePontualMaxima(temp, valorEsperado):
    valorCalc = maxima(temp)
    if valorCalc != valorEsperado:
        print('Valor errado para array ', temp)
        print(
            'Valor esperado ', valorEsperado, '. Valor calculado ', valorCalc
        )
    else:
        print('Teste ok!')

def testa_maxima():
    print('Iniciando os testes')
    testePontualMaxima([0], 0)
    testePontualMaxima([0, 0, 0, 0, 0, 0], 0)
    testePontualMaxima([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
    testePontualMaxima([30, 31, 32, 30, 24, 25, 26, 27, 28, 29, 26], 32)
    testePontualMaxima([-12, -15, 0, 5, 2], 5)  
    print('Finalizando os testes')

# testa_minima()

# testa_maxima()

MinMax([30, 31, 32, 30, 24, 25, 26, 27, 28, 29, 26, 0, -2, 55, -15])