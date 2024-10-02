# Desenvolva um programa que leia o comprimento de três retas e diga se podem ou não formar um triângulo e fale se é ESCALENO, ISOSCELES ou EQUILÁTERO.

r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))

if r1 == r2 == r3:
    print('As retas podem formar um triângulo EQUILÁTERO')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and (r1 == r2 or r1 == r3 or r2 == r3):
    print('As retas formam um triângulo ISÓSCELES')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triângulo ESCALENO')
else:
    print('As retas não podem formar um triângulo')