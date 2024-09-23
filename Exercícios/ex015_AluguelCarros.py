# Escreva um programa que pergunte a quantidade de km percorrido por um carro e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que a diária do carro custa R$ 60.00 e R$ 0,15 por km rodado.
dias = int(input('Digite a quatidade de dias alugados: '))
km = int(input('Digite a quantidade de km rodados: '))
valor = (dias * 60) + (km * 0.15)
print('O valor do aluguel do carro é de R$ {:.2f}'.format(valor))