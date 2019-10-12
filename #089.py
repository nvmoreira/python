"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""


lista = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    inserir = input('Deseja inserir um aluno [S/N]? ').upper().strip()
    if inserir == 'N':
        break
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>10}')
for i, j in enumerate(lista):
    print(f'{i:<4}{j[0]:<10}{j[2]:>10}')
print('-'*30)
while True:
    indice = int(input('Mostrar notas de qual aluno? [999 interrompe]: '))
    if indice == 999:
        print('Até a próxima!')
        break
    print(f'As notas do aluno {lista[indice][0]} foram {lista[indice][1]}.')
