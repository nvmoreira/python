"""Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""

from time import sleep

print('ATENÇÃO PARA A CONTAGEM REGRESSIVA:')

for i in range(0, 11).__reversed__():
    print(i)
    sleep(1)
print('PRA')
sleep(1)
print('PRA PRA PRA')
sleep(1)
print('PRA PRA PRA PRA PRA PRA PRA')
sleep(1)
print('POOOOOOOOOOOOOOOOOOW')
