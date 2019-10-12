"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média"""

lista = []
total = 0
soma = 0
media = 0
pessoa = {}
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize().strip()
    while True:
        pessoa['sexo'] = input('Sexo [F/M]: ').upper().strip()
        if pessoa['sexo'] in 'FM':
            break
        print('Opção inválida!')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    total += 1
    while True:
        cont = input('Deseja cadastrar outra pessoa [S/N]? ').upper().strip()
        if cont in 'SN':
            break
        print('Opção inválida!')
    if cont == 'N':
        media = soma / total
        print('='*40)
        print(f'Foram cadastradas {total} pessoas.')
        print(f'A média de idade é {media:.2f} anos.')
        print(f'As mulheres cadastradas foram', end=' ')
        for i in lista:
            if i['sexo'] == 'F':
                print(f'{i["nome"]}', end=' ')
        print(f'\nAs pessoas com idade acima da média são: ')
        for i in lista:
            if i['idade'] > media:
                for k, v in i.items():
                    print(f'{k} = {v};', end=' ')
                print()
        break
print('<<<ENCERRADO>>>')
