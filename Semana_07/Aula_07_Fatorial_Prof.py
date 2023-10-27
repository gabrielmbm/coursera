# Repetições encaixadas

# linha = 1
# coluna = 1

# while linha <= 10:
#     while coluna <= 10:
#         print(linha * coluna, end='\t')
#         coluna += 1
#     linha += 1
#     print('')
#     coluna = 1

# Analisar solução do profesor em relação ao meu.
def solucaoProfessor():
    n = int(input('Digite um número inteiro: '))
    while n >= 0:
        fatorial = 1
        while n > 1:
            fatorial = fatorial * n
            n -= 1
        print(fatorial)
        n = int(input('Digite um número inteiro: '))

def fatorialInterno(n):
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    return fatorial
    

def main ():
    n = int(input('Digite um número inteiro: '))
    while n >= 0:
        fatorial = fatorialInterno(n)
        print(fatorial)
        n = int(input('Digite um número inteiro: '))

main()