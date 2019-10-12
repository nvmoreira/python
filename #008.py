# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros.

x = float(input('Digite um valor em metros: '))

cm = x * 100
mm = x * 1000

print('O valor {} metros é igual a {:.1f} centímetros e {:.0f} milímetros.'.format(x, cm, mm))
