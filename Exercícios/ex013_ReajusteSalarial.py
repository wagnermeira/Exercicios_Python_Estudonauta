#13 Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite aqui seu salário: R$ '))
novo = salario + (salario * 15 / 100)
print('Seu salário era {}, com o aumento de 15% ficará de R$ {}.'.format(salario,novo))
