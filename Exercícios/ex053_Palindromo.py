# Crie um programa que leia um frase qualquer e diga se ela é um palindromo, desconsiderando os espaços

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for l in range(len(junto) - 1, -1, -1):
    inverso += junto[l]
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
