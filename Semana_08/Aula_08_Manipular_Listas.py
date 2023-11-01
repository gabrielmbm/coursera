# Clonar listas

lista1 = ['vermelho', 'verde', 'azul']

lista2 = lista1[:]
 
lista2[0] = 'rosa'

print(lista1)
print(lista2)

# Retorna um False ou True se o objeto está na lista
'rosa' in lista2

# Concatenar listas
a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

# Remoção de listas
c= [1, 2, 3, 4, 5, 6]
print(c)
del c[0]
print(c)