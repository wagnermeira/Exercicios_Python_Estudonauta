# Escreva um algoritmo para aprovar emprestimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
vc = float(input('Digite o valor da casa: R$ '))
sal = float(input('Qual o salário do comprador: R$ '))
anos = float(input('Quantos anos pretende pagar: '))

parcela = vc / (anos * 12)
maximo = sal * 0.3

if parcela <= maximo:
    print('Parabêns, seu emprétimo foi aprovado com parcela de R$ {:.2f} mensais.'.format(parcela))
else:
    print('Infelizmente seu emprétimo foi negado, a parcela ficou {:.2f} e a máxima para seu salário seria R$ {}'.format(parcela, maximo))
