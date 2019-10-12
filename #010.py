# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Dado para conversão: US$1 = R$3,27

x = float(input('Digite a quantidade de dinheiro que você possui na carteira: '))

y = x / 3.27

print('Você pode comprar US${:.2f}.'.format(y))