# Crie um programa que leia um número e calcule o dobro, o triplo e a sua raiz quadrada.
from math import sqrt
num = float(input('Digite aqui o número que você quer os resultados: '))
print('Após analisar o número {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}'.format(num, num * 2, num * 3, sqrt(num)))
