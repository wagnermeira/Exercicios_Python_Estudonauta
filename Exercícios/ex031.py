# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

km = float(input('Digite aqui a distância da viagem: '))
if km <= 200:
    print('O preço a ser pago pela viagem será de R$ {:.2f}'.format(km * 0.50))
else:
    print('O preço a ser pago pela viagem será de R$ {:.2f}'.format(km * 0.45))
