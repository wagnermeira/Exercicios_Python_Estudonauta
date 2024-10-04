# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas e mostre no final a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres tem menos de 20 anos

somaidade = 0
homem = 0
nomehomem = ''
mulher = 0

for c in range(1, 5):
    print('-=-' * 10)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Digite o seco (M/F): ')).upper().strip()
    somaidade += idade

    if c == 1 and sexo == 'M':
        homem = idade
        nomehomem = nome

    if idade > homem and sexo == 'M':
        homem = idade
        nomehomem = nome
    if sexo == 'F' and idade < 20:
        mulher += 1

print('-=-' * 15)
print('A média de idade do grupo é de {} anos.'.format(somaidade / 4))
print('O {} é o homem mais velho com {} anos.'.format(nomehomem, homem))
print('Temos {} mulher(es) com menos de 20 anos.'.format(mulher))

