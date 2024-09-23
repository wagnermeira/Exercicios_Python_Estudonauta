# Escreva m programa que leia um valor em metros e exiba convertido em centímetro e milímetros.
valor = float(input('Digite aqui o valor em (m) desejado para conversão: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print('''{} m convertido para todas as escalas fica:

= {} km
= {} hm
= {} dam
= {} dm
= {} cm
= {} mm'''.format(valor, km, hm, dam, dm, cm, mm))

