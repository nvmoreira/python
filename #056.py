"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."""

from time import sleep

soma = 0
velho = ''
maior = 0
quant = 0

for i in range(1, 5):
    print('Dados da {}ª pessoa: '.format(i))
    nome = input('Nome: ').capitalize().strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [F/M]: ').upper().strip()
    soma = soma + idade
    if idade > maior and sexo == 'M':
        maior = idade
        velho = nome
    if sexo == 'F' and idade < 20:
        quant += 1
media = soma / 4
print('Analisando...')
sleep(2)
print("""A média de idade das pessoas é {:.2f}.
Há {} mulheres com menos de 20 anos.
O homem mais velho se chama {} e tem {} anos.""".format(media, quant, velho, maior))
