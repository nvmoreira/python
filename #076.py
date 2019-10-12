"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Arroz', 9.90, 'Feijão', 6.50, 'Macarrão', 3.40)

print('='*40)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*40)
for n in produtos:
    if type(n) == str:
        print(f'{n:.<30} R$', end=' ')
    else:
        print(f'{n:.2f}')
