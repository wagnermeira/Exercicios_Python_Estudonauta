# Faça um programa que calcule a soma entre todos os números ímpares múltiplos de 3 e que se encontram no intervalo de 1 a 50.
s = 0
x = 0
for c in range (1, 500):
    if (c % 2) != 0 and (c % 3) == 0: 
        s = s + c
        x += 1
print('A soma dos {} valores solicitados é {}'.format(x, s))
