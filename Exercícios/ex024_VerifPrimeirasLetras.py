# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"

cid = input('Digite o nome da cidade que você nasceu: ').strip()
print(cid[:5].upper() == 'SANTO')