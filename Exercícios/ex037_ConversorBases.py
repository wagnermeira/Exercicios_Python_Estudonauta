# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 - Binário; 2 - Octal; 3 - hexadecimal;

num = int(input('Digite um número inteiro: '))
print('''Escolha agora qual base de conversão:
      [1] Binário
      [2] Octal
      [3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal {}'.format(num,hex(num)[2:]))
else:
    print('Opção Inválida')
