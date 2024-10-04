#Faça um programa que leia o peso de 5 pessoas. No final mostre qual foi o maior e o menor peso.

maior = 0
menor = 0

for c in range (0,6):
    peso = float(input('Digite o peso em kg: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} kg, e o menor peso é {} kg.'.format(maior,menor))
