# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo:

n = int(input('Digite o número a ser analisado: '))
y = 0
for c in range (1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        y += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n O número {} foi divisível {} vezes'.format(n,y))
if y == 2:
    print('Logo ele é PRIMO')
else:
    print('Logo ele NÂO É PRIMO')

