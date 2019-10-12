# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

x = input('Digite algo: ')

print('Tipo primitivo:', type(x))
print('É alfanumérico?', x.isalnum())
print('É alfabético?', x.isalpha())
print('É ASCII?', x.isascii())
print('É decimal?', x.isdecimal())
print('É um dígito?', x.isdigit())