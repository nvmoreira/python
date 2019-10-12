"""Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um
atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER"""

from datetime import date

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = int(date.today().year) - ano

if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif 10 <= idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif 15 <= idade <= 19:
    print('A categoria do atleta é JÚNIOR')
elif 20 <= idade <= 25:
    print('A categoria do atleta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')
