#Escreva um programa que conversa uma temperatura digitada em °C e converta para °F.
c = float(input('Digite a temperatura em °C: '))
f = c * 1.8 + 32
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))
