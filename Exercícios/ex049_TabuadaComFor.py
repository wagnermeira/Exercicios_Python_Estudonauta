# Refaça o exercício 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('-=-' * 6)
num = int(input('Digite aqui o número desejado: '))

for c in range (0, 11):
    print('{} x {} = {:2}'.format(num, c, c * num))
print('-=-' * 6)
