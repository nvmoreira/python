"""Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random

print('{:~^60}'.format('JOGO DA ADIVINHAÇÃO'))
print('Estou pensando em um número inteiro entre 0 e 10. Consegue adivinhar qual é?')
x = int(input('Digite um número: '))
pc = random.randint(0, 10)
palpite = 1

while x != pc:
    if x > pc:
        x = int(input('Você errou! Tente um número menor: '))
        palpite += 1
    else:
        x = int(input('Você errou! Tente um número maior: '))
        palpite += 1
if x == pc:
    print('Parabéns, você acertou em {} tentativas!!! \nEstava pensando no número {}.'.format(palpite, x))
