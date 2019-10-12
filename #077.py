"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
cada palavra, quais são as suas vogais."""

palavras = ('arroz', 'dia', 'link', 'almoço')

for i in palavras:
    print(f'\nAs vogais da palavra {i} são: ', end=' ')
    for vogal in i:
        if vogal in 'aeiou':
            print(vogal, end=' ')
