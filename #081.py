"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

numeros = []
while True:
    x = int(input('Digite um número inteiro: '))
    numeros.append(x)
    cont = input('Deseja continuar [S/N]? ').upper().strip()
    while cont not in 'SN':
        print('Opção inválida.')
        cont = input('Deseja continuar? [S/N]? ').upper().strip()
    if cont == 'N':
        numeros.sort(reverse=True)
        print(f'Foram digitados {len(numeros)} números. \nA lista em ordem decrescente é: \n{numeros}')
        if 5 in numeros:
            print(f'O número 5 aparece na lista {numeros.count(5)} vezes.')
        else:
            print('O número 5 não está na lista.')
        break
