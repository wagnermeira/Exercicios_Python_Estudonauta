# Escreva um programa que faça o computador "pensar" em um número inteiro de 0 a 5 e peça ao usuário tentar descobrir qual foi o número escolhdo pelo computador. O programa deverá escrever na tela se o usuário acertou ou não.

from random import randint
from time import sleep

comp = randint(0,5)

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tende adivinhar...')
print('-=-' * 20)

n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')

sleep(3)

if n == comp:
    print('Parabéns, você venceu.')
else:
    print('Eu venci, eu pensei no número {}'.format(comp))