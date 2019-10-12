"""Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos."""

x = int(input('Digite o primeiro termo da PA: '))
y = int(input('Digite a razão da PA: '))

i = 0
termos = 10
count = 0

print('Os dez primeiros termos da PA são: ', end='')

while i != termos:
    print(x, '→ ', end='')
    x += y
    i += 1
    count += 1
    if termos == i:
        i = 0
        termos = int(input('\nQuanto termos você quer mostrar a mais? '))
    if termos == 0:
        print('{} termos foram exibidos \nFim do programa'.format(count))
