# Faça um programa que leia o comprimento do cateto oposto e do adjacente de um triângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hip = sqrt(co ** 2 + ca ** 2)

print('A hipotenusa vai medir {:.2f}'.format(hip))
