frutasexoticas = ['jabuticaba', 'cupuaçu', 'graviola']
for fruta in frutasexoticas:
    print ('Eu adoro ' + fruta)

print('')

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
for x in primos:
    print(x*x)

print('')

for i in range(20):
    print(i)

print('')

for i in range(10, 20):
    print(i)

print('')

for i in range(0, 100, 3):
    print(i)

print ('')

# Alterar valores numa lista com for

primos2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(primos2)

for i in range(len(primos)):
    primos2[i] = primos2[i]**3

print(primos2)