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

    print(conjInverso)

def flores():
    # Imprimiu sem criar lista, utilizando o print
    flores = ["margarida", "rosa", "tulipa", "cravo"]
    tam = len(flores) - 1
    while tam >= 0:
        print(flores[tam], end=", ")
        tam = tam - 1

def alunos():
    aluno = ["Fulano de Tal", 25, "Rua xyz, 123", "São Paulo", 3, "Matemática", 7.5, "Português", 6.6, "Artes", 10]
    aluno[1] = aluno[1] + 1
    print(aluno)

alunos()