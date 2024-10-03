# Faça um programa que mostre na tela uma contagem regressiva para o estouro dos fogos de artifício, indo de 10 até 0, com uma causa de 1 segundo entre elas.

from time import sleep
for c in range(10, 0 - 1, -1):
    print(c)
    sleep(1)
print('FOGOS')