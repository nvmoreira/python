# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

x = float(input('Digite a largura da parede em metros: '))
y = float(input('Digite a altura da parede, em metros: '))

area = x * y
tinta = area/2

print('A área da parede é {} m² e são necessários {} litros de tinta para pintá-la.'.format(area, tinta))