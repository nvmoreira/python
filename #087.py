"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""

matriz = []
pares = 0
for i in range(3):
    matriz.append([]*3)
    for j in range(3):
        x = int(input(f'Digite o valor do elemento {i, j}: '))
        matriz[i].insert(j, x)
        if x % 2 == 0:
            pares += x
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]
maior = max(matriz[1])
for i in range(3):
    for j in range(3):
        print(f'{matriz[i][j]:^5}', end='')
    print()
print(f'A soma dos números pares digitados é {pares}.')
print(f'A soma dos números da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
