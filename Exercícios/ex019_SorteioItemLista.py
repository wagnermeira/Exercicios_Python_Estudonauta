# Um professor quer sortear um dos seus 4 aluinos para apagar o quadro, faça um programa que ajude ele,  lendo o nome deles e escrevendo o nome do escolhido.

import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print('O Aluno escolhido foi {}'.format(escolhido))