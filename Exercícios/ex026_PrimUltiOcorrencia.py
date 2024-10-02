# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes a letra "a" aparece, em qual posição ela aparece a primeira vez e qual aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A') + 1))
