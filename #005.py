# Faça um programa que leia um número e mostre na tela o seu antecessor e o seu sucessor.

x = int(input('Digite um número inteiro: '))

ant = x - 1
suc = x + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(x, ant, suc))