"""Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

print('{:~^60}'.format('CALCULADORA BÁSICA'))
print('Digite dois valores: ')
x = float(input('Primeiro valor: '))
y = float(input('Segundo valor: '))

opcao = 0

while opcao != 5:
    opcao = int(
        input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nOPÇÃO: '))
    if opcao > 5:
        print('Opção inválida.')
    if opcao == 1:
        resultado = x + y
        print('A soma de {} e {} é {}.'.format(x, y, resultado))
    elif opcao == 2:
        resultado = x * y
        print('O produto de {} e {} é {}.'.format(x, y, resultado))
    elif opcao == 3:
        if x > y:
            print('{} é maior que {}'.format(x, y))
        elif y > x:
            print('{} é maior que {}'.format(y, x))
        elif x == y:
            print('{} e {} são iguais'.format(x, y))
    if opcao == 4:
        print('Digite novos valores:')
        x = int(input('Primeiro valor: '))
        y = int(input('Segundo valor: '))
    print('=-=' * 10)
if opcao == 5:
    print('TCHAU TCHAU!')
