def listaInversa():
    # Imprimi criando uma lista
    n = int(input('Digite um número: '))
    conj = []
    conjInverso = []

    while n > 0:
        conj.append(n)
        n = int(input('Digite um número: '))

    comp = len(conj) - 1
    while comp >= 0:
        conjInverso.append(conj[comp])
        comp -= 1

    for i in conjInverso:
        print(i, end='\n')

listaInversa()