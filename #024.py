# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Escreva o nome de uma cidade: ').strip()

cidade = cidade.upper()

print(cidade[:6] == 'SANTO ')
