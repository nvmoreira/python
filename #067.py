"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

while True:
    x = int(input('Digite um número para ver a tabuada: '))
    if x < 0:
        print('Número inválido!')
        break
    for i in range(1, 11):
        print(f'{x} x {i} = {x*i}')   # programa do Guanabara
    print('~'*30)
