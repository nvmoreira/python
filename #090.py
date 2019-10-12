"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela."""

cad = {'nome': input('Nome: '), 'média': float(input('Média: '))}

if cad['média'] < 5:
    cad['situacao'] = 'reprovado'
elif 5 < cad['média'] < 7:
    cad['situacao'] = 'recuperação'
else:
    cad['situacao'] = 'aprovado'
print('='*40)
for k, v in cad.items():
    print(f'- {k} é igual a {v}')
