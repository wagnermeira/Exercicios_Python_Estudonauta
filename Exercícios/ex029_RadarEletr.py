# Escreva um algoritmo que leia a velocidade de um carro. se ele ultrapassar 80km/h, mostre uma mensagem falando qeue ele foi multado. A multa custará R$ 7,00 por cada km ultrapassado.

v = float(input('Qual a velocidade medida: '))

if v <= 80:
    print('Boa viagem, você está dentro do limite permitido.')
else:
    print('Você ultrapassou {} km do permitido, sua multa será de R$ {:.2f}.'.format(v - 80,(v - 80) * 7))
