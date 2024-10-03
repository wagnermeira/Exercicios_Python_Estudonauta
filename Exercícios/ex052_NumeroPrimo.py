# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo:

n = int(input('Digite o número a ser analisado: '))
y = 0
for c in range (1, n + 1):
    x = n % c
    y += x
    print(x)