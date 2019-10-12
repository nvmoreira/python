"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

x = int(input('Digite um número: '))
y = int(input('Digite mais um número: '))
z = int(input('Digite outro número: '))
w = int(input('Digite o último número: '))

tupla = (x, y, z, w)
while True:
    if 9 in tupla:
        print(f'O número 9 aparece {tupla.count(9)} vezes.')
    if 3 in tupla:
        print(f'A primeira aparição do número 3 é na posição {tupla.index(3)}.')
    print('Temos os seguintes números pares: ', end='')
    for n in tupla:
        if n % 2 == 0:
            print(n, end=' ')
    break
