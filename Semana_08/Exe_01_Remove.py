def remove_repetidos(lista):
    lista.sort()
    semRepeteco = []
    for i in lista:
        if i not in semRepeteco:
            semRepeteco.append(i)
    return semRepeteco