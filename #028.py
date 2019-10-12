"""Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
perdeu."""
import random

x = int(input('Estou pensando em um número de 1 a 5. Consegue adivinhar qual é? '))

sorteio = random.randint(1, 5)

if sorteio == x:
    print('Parabéns! Você acertou o número')
else:
    print("""O número era {}. Pobre humano, não consegue acertar um número hauhauahauahua""".format(sorteio))
