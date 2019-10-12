"""Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""

numeros = [], []
num = 0
while num < 7:
    x = (int(input('Digite um número: ')))
    if x % 2 == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
    num += 1
print(f'Os números pares são: {sorted(numeros[0])}.')
print(f'Os números impares são: {sorted(numeros[1])}.')
