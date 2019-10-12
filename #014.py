# Escreva um algoritmo que converta uma temperatura em Celsius para Fahrenheit
# Referência para conversão: C * 1,8 + 32 = F

x = float(input('Digite a temperatura na escala Celsius: '))

F = (x * 1.8) + 32

print('A temperatura em Fahrenheit é {}°.'.format(F))
