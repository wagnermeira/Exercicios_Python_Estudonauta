# Crie um programa que leia quantos reais a pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considerando que U$ 1.00 vale R$ 5.46
money = float(input('Quantos reais você tem na carteira: R$ '))
dol = money / 5.46
print('Com R$ {:.2f} você pode comprar U$ {:.2f}.'.format(money, dol))
