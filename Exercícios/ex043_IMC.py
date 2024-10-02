# faça um programa que calcule o IMC:

h = float(input('Digite aqui sua altura: '))
peso = float(input('Digite aqui seu peso em kg: '))

imc = peso / h ** 2
print('Seu IMC deu {:.2f} e você está '.format(imc), end='')
if imc < 17:
    print('MUITO ABAIXO DO PESO.')
elif imc < 18.5:
    print('ABAIXO DO PESO.')
elif imc < 25:
    print('PESO NORMAL.')
elif imc < 30:
    print('ACIMA DO PESO.')
elif imc < 35:
    print('OBESIDADE GRAU I.')
elif imc < 40:
    print('OBESIDADE GRAU II.')
else:
    print('OBESIDADE GRAU III.')
