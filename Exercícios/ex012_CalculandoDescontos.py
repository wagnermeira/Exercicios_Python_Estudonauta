# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
p = float(input('Digite o preço do produto: R$ '))
desconto = p - (p * 5 / 100)
print('O preço do produto era R$ {:.2f}, mas com o desconto de 5% fica por R$ {:.2f}.'.format(p, desconto))
