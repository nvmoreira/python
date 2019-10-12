"""Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep
jogos = []
x = int(input('Quantos jogos deseja sortear? '))

for i in range(x):
    jogos.append([]*x)
    for j in range(6):
        num = randint(1, 60)
        if num not in jogos[i]:
            jogos[i].append(num)
    print(f'Jogo 1: {i+1} são: {jogos[i]}.')
    sleep(1)
