"""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. """

import random

i = 0
while True:
    x = int(input('Escolha: \n[0] Par \n[1] Ímpar \nPAR OU ÍMPAR? '))
    if x == 0:
        print('Você escolheu PAR')
    else:
        print('Você escolheu ÍMPAR')
    y = int(input('Escolha um número inteiro: '))
    pc = random.randint(0, 100)
    if (y + pc) % 2 == 0 and x == 0 or (y + pc) % 2 != 0 and x == 1:
        i += 1
        print('Você venceu!! Jogue novamente!')
        print('--'*20)
    else:
        print(f'Você perdeu essa partida, mas ganhou {i} partidas de um total de {i + 1}!')
        break
