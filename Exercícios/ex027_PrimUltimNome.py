# Faça  um programa aque leia o nome completo de uma pessoa e mostre o primeiro e ultimo nome separadamente.
n = str(input('Digite seu nome completo: '))
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
