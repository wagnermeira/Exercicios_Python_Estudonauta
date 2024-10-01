# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin,cos, tan, radians

a = float(input('Digite o valor do ângulo desejado: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print('''Para o ângulo de {}:
      Seno     = {:.2f}
      Cosseno  = {:.2f}
      Tangente = {:.2f}'''.format(a,s,c,t))
