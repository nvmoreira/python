"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
 foi multado. A multa vai custar R$7,00 por cada Km acima do limite."""

v = float(input('Escreva a velocidade atual do carro: '))

if v > 80:
    multa = (v - 80) * 7
    print('Você excedeu o limite de 80Km/h e foi MULTADO! Pague R${:.2f} para continuar dirigindo!'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade! Dirija com segurança!')
