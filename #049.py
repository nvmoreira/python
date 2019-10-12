# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

x = int(input('Escolha um número inteiro para mostrar a tabuada: '))

for i in range(0, 11):
    mult = x * i
    print('{} x {} = {}'.format(x, i, mult))
