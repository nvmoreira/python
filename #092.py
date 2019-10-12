""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

from datetime import date
dados = {'nome': input('Nome: ')}
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['ctps'] = int(input('Nº CTPS (0 se não possui): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['contratacao'] - nascimento + 35
    print('='*30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
else:
    print('='*30)
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}.')
