"""Crie um programao onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista já na posição correta
(sem usar o sort. No final, mostre a lista ordenada na tela.)"""

numeros = []
while True:
    x = int(input('Digite um número: '))
    if len(numeros) == 0 or max(numeros) <= x:
        numeros.append(x)
    elif x <= min(numeros):
        numeros.insert(0, x)
    elif min(numeros) < x <= numeros[1]:
        numeros.insert(1, x)
    elif numeros[1] < x <= numeros[2]:
        numeros.insert(2, x)
    elif numeros[2] < x <= numeros[3]:
        numeros.insert(2, x)
    if len(numeros) == 5:
        print(f'Os números digitados, do menor para o maior, foram {numeros}')
        break
