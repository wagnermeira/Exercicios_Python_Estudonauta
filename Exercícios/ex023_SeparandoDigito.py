# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados: unidade, dezena, centena e milhar.

num = int(input('Digite o número desejado: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(' Analisando o número {}:'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
