"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla."""

import random

tupla = (random.randint(1,999), random.randint(1,999), random.randint(1,999), random.randint(1, 999), random.randint(1, 999))

print(f'A tupla possui os valores {tupla}')
print(f'O menor número é {min(tupla)}')
print(f'O maior número é {max(tupla)}')