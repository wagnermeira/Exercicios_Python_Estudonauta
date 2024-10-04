# Desenvolva um program aque leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa PA.

t = float(input('Digite o termo da sua PA: '))
r = float(input('Digite a razão da sua PA: '))

for c in range (0, 10):
    t = t + r
    print(t - r, end=' -> ')
print('FIM')