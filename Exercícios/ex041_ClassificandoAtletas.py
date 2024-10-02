# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento do atleta e classifique ele. 
# Até 9 anos = Mirim
# Até 14 anos = Infantil
# Até 19 anos = Junior
# Até 25 anos = Sênior
# Acima de 25 anos = Master

from datetime import date
atual = date.today().year

ano = int(input('Digite seu ano de nascimento: '))

idade = atual - ano

if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade <= 14:
    print('Você está na categoria INFANTIL.')
elif idade <= 19:
    print('Você está na categoria JUNIOR.')
elif idade <= 25:
    print('Você está na categoria SÊNIOR.')
else:
    print('Você está na categoria MASTER.')
