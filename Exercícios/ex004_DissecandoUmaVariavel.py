# Crie um programa que leia algo e mostre na tela o seu tipo primitivo e todas informações possíceis sobre ele.
a = input('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está maiúscula? ', a.isupper())
print('Está minúsculo? ', a.islower())
print('Está capitalizado? ', a.istitle())
