# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

print('CONTAGEM DE PARES ATÉ 50:')

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
        sleep(0.3)

#Programa do Guanabara
"""for i in range (2, 52, 2):
    print(i)"""