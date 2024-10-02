# Crie um algoritmo que leia um número inteiro e mostre na tela se é pau ou ímpar

n = int(input('Digite um número qualquer: '))
r = n % 2

if r == 0:
    print('O número {} é par.'.format(n))
elif n == 3:
    print('{} é PAAAAARRRRR hahahahahah'.format(n))
else:
    print('O número {} é ímpar.'.format(n))