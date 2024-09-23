# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
l = float(input('Digie a largura da parede: '))
h = float(input('Digite a altura da parede: '))
area = l * h
tinta = area / 2
print('-' * 20)
print('''Sabendo que as dimensões da parede são {:.2f} x {:.2f}:
Area da Parede = {:.2f} m²
Necessário {:.2f} litros de tinta.'''.format(l, h, area, tinta))
print('-' * 20)
