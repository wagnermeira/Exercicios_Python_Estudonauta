# Escreva um programa que pergunte qual o salário do funcionário e calcule o valor do seu aumento: Sal <= R$ 1250,00 aumento de 15%, para maiores aumento de 10%.

sal = float(input('Digite aqui o valor do salário atual: R$ '))

if sal <= 1250:
    print('Seu novo salário com aumento de 15%  é de R$ {:.2f}'.format(sal + (sal * 15 / 100)))
else:
    print('Seu novo salário com aumento de 10% é de R$ {:.2f}'.format(sal + (sal * 10 / 100)))