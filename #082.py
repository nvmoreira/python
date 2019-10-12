"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
listas geradas."""

listao = []
while True:
    x = int(input('Digite um número: '))
    listao.append(x)
    cont = input('Deseja continuar [S/N]? ').upper().strip()
    par = []
    impar = []
    while cont not in 'SN':
        print('Opção inválida.')
        cont = input('Deseja continuar [S/N]? ').upper().strip()
    if cont == 'N':
        for i in range(len(listao)):
            if i % 2 == 0:
                par.append(i)
            else:
                impar.append(i)
        print(f'Os números digitados foram: {listao}')
        print(f'Os números pares são: {par}')
        print(f'Os números ímpares são: {impar}')
        break
