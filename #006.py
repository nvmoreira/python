#Crie um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada.

x = float(input('Digite um número: '))

dobro = x * 2
triplo = x * 3
raiz = x**(1/2)

print('O número lido é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(x, dobro, triplo, raiz))
