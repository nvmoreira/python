"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
 dessa progressão."""

x = int(input('Digite o primeiro termo da PA: '))
y = int(input('Digite a razão da PA: '))

print('Os dez primeiros termos da PA são:')
for i in range(0, 10):
    print(x, end='  ')
    x += y
