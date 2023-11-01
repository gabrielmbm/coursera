# Objetos e referências
# Variáveis com o mesmo conteúdo de string e inteiro, apontam para a mesma região de memória
# Comando is verifica tal afimação retornando True ou False

a = 'banana'
b = 'banana'
c = 'maçã'
a is b
a is c

# Repetições e referências

origList = [45, 76, 34, 55]
newList = [origList] * 3
print(origList)
print(newList)
origList[1] = 99
print(origList)
print(newList)