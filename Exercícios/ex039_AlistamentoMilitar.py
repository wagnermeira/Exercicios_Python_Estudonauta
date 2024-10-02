# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora dde s alistar  ou se já passou do tempo do alistamento. Seu programa também deverá mostrar  o tempo que falta ou que já passou do prazo.

from datetime import date
atual = date.today().year

ano = int(input('Digite o ano do seu nascimento: '))
sexo = str(input('Digite M para masculino e F para feminino: ')).strip().upper()

idade = atual - ano
alis = ano + 18

if idade < 18 and sexo == 'M':
    print('Você tem {} anos e falta(m) {} ano(s) para se alistar.'.format(idade, alis - atual))
    print('Seu alistamento é em {}'.format(alis))
elif idade > 18 and sexo == 'M':
    print('Você tem {} anos e já passara(m) {} ano(s) do seu alistamento.'.format(idade, atual - alis))
    print('Seu alistamento era em {}'.format(alis))
elif idade == 18 and 'M':
    print('Você tem 18 anos e precisa se alistar o mais rápido possivel')
else:
    print('O alistamento é obrigatório para o sexo masculino, você pode ficar tranquila.')
