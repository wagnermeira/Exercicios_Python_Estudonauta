# Crie um programa que leia duas notas e calcule sua média. Média abaixo de 5.0: Reprovado, Entre 5.0 e 6.9: Recuperação e 7 ou superior: Aprovado.

n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

media = (n1 + n2) / 2

if 7 > media >= 5:
    print('Sua média foi {:.2f} e você esté em RECUPERAÇÃO'.format(media))
elif media < 5:
    print('Sua média foi {:.2f} e você está REPROVADO'.format(media))
else:
    print('Parabéns, sua média foi {:.2f} e você está APROVADO'.format(media))
