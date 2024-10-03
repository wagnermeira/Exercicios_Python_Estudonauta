# Crie um program que faça o computador jogar jokenpô com você

from random import randint
from time import sleep

print('-=-' * 10)
print('Vamos jogar JOKENPÔ')
print('-=-' * 10)
print('''Esolha uma das opções de jogada:
      [1] PEDRA
      [2] PAPEL
      [3] TESOURA''')
jogador = int(input('Qual sua jogada? '))
pc = randint(1,3)
print('-=-' * 5)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('-=-' * 5)
sleep(1)

if pc == 1:
    if jogador == 1:
        print('EMPATOU')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 3:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2:
    if jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATOU')
    elif jogador == 3:
        print('JOGADOR VENCEU')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 3:
    if jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
    elif jogador == 3:
        print('EMPATOU')
    else:
        print('JOGADA INVÁLIDA')
else:
    print('JOGADA INVÁLIDA')
