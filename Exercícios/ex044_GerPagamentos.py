# Faça um programa que que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de apagamento:
# A vista - dinheiro/cheque: 10% de desconto
# A vista - cartão - 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais - 20% de juros

prod = float(input('Digite o valor do produto: '))
print(''' Escolha a forma de pagamento:
      [1] Dinheiro/Pix:
      [2] A vista no Cartão:
      [3] 2x no cartão:
      [4] 3x ou mais no cartão:''')
opcao = int(input('Digite a opção de pagamento: '))

if opcao == 1:
    print('Para esta forma de pagamento você tem 10% de desconto, você pagará R$ {:.2f} pelo produto.'.format(prod - (prod * 10 / 100)))
elif opcao == 2:
    print('Para esta forma de pagamento você tem 5% de desconto, você pagará R$ {:.2f} pelo produto.'.format(prod - (prod * 5 / 100)))
elif opcao == 3:
    print('Para esta forma de pagamento você não tem desconto, você pagará 2 x R$ {:.2f} no cartão.'.format(prod - (prod / 2)))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas você deseja: '))
    novo = prod + (prod * 20 / 100)
    print('Você escolheu pagar em {}, logo terá um juros de 20%, ficando assim um total de R$ {:.2f}. Você pagará em {} x R$ {:.2f}.'.format(parcelas, novo, parcelas, novo / parcelas))
else:
    print('OPÇÃO INVÁLIDA DE PAGAMENTO')