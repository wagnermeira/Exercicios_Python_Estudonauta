# Faça um programa que leia um número inteiro qualquer e mostre sua tabuada na tela
print('-' * 15)
num = int(input('Digite aqui o número desejado: '))
print('''
{} x  0  = {:2}
{} x  1  = {:2}
{} x  2  = {:2}
{} x  3  = {:2}
{} x  4  = {:2}
{} x  5  = {:2}
{} x  6  = {:2}
{} x  7  = {:2}
{} x  8  = {:2}
{} x  9  = {:2}
{} x 10  = {:2}
'''.format(num, num * 0, num, num * 1, num, num * 2, num, num * 3, num, num * 4, num, num * 5, num, num * 6, num, num * 7, num, num * 8, num, num * 9, num, num * 10))
print('-)' * 15)
