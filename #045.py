# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('{:=^40}'.format('JO-KEN-PO!!!!!'))
x = int(input("""As opções são:
1 - Pedra
2 - Papel
3 - Tesoura
Escolha a  sua: """))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!')
sleep(1)

jkp = ['pedra', 'papel', 'tesoura']
pc = random.choice(jkp[:])

if x == 1:
    escolha = 'pedra'
elif x == 2:
    escolha = 'papel'
else:
    escolha = 'tesoura'

if x == 1 and pc == 'papel' or x == 2 and pc == 'tesoura' or x == 3 and pc == 'pedra':
    print('Você escolheu {} e o computador escolheu {}. Você perdeu!'.format(escolha.upper(), pc.upper()))
elif escolha == pc:
    print('Você e o computador escolheram {}. Empate!'.format(escolha.upper()))
elif x == 1 and pc == 'tesoura' or x == 2 and pc == 'pedra' or x == 3 and pc == 'papel':
    print('Você escolheu {} e o computador escolheu {}, Você ganhou!'.format(escolha.upper(), pc.upper()))
else:
    print('Jogada inválida!')