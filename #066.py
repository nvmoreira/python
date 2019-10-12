"""Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas
(desconsiderando o flag)."""

i = 0
soma = 0

while True:
    x = int(input('Digite um número [999 para parar]: '))
    if x == 999:
        break
    i += 1
    soma += x
print(f'A soma dos {i} números digitados é {soma}')