# Desenvolva um programa que leia  as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Digite aqui a primeira nota: '))
nota2 = float(input('Digite aqui a segunda nota: '))
media = (nota1 + nota2) / 2
print('A média do aluno é {:.1f}.'.format(media))
