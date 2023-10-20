#Faça um programa em Python que receba quatro notas, calcule
# e imprima a média aritmética. 

nota1 = input("Digite a primeira nota: ")
nota2 = input("Digite a segunda nota: ")
nota3 = input("Digite a terceira nota: ")
nota4 = input("Digite a quarta nota: ")

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

print("A média aritmética é", media)