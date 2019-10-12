"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta."""

# Ao invés de usar a dimensão do problema fiz o programa aceitando a dimensão que o usuário insere

matriz = []
dimensao = int(input('Digite a dimensão da matriz: '))
for i in range(dimensao):
    matriz.append([] * dimensao)
    for j in range(dimensao):
        x = int(input(f'Digite um valor para o elemento {i, j}: '))
        matriz[i].insert(j, x)
for i in range(dimensao):
    for j in range(dimensao):
        print(f'{matriz[i][j]:^5}', end='')
    print()
