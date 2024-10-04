# Crie um programa que leia o ano de nascimento de sete pessoas e mostre quantas pessoas inda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range (0,7):
    pessoa = int(input('Digite seu ano de nascimento: '))
    if atual - pessoa < 18:
        menor += 1
    else:
        maior += 1
print('Temos {} menores de idade e {} pessoas na maioridade.'.format(menor,maior))
    