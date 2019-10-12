# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))
z = float(input('Digite o terceiro número: '))

"""lista = [x, y, z]

maior = max(lista)
menor = min(lista)

print('O maior número é {} e o menor número é {}.'.format(maior, menor))"""

if x > y and x > z:
    maior = x
elif y > x and y > z:
    maior = y
else:
    maior = z

if x < y and x < z:
    menor = x
elif y < x and y < z:
    menor = y
else:
    menor = z
print('O maior número é {} e o menor número é {}'.format(maior, menor))
