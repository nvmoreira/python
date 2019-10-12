"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros"""

print('{:=^40}'.format('NAT STORE'))
x = float(input('Digite valor das compras: '))
y = float(input("""Os métodos de pagamento disponíveis são:
1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal
4 - 3x ou mais no cartão: 20% de juros
Qual você prefere? """))

din = x * 10 / 100
deb = x * 5 / 100
tres = x * 20 / 100

if y == 1:
    preco = x - din
    print('O valor total é R${:.2f}'.format(preco))
elif y == 2:
    preco = x - deb
    print('O valor total é R${:.2f}'.format(preco))
elif y == 3:
    parc = x / 2
    print('O valor será parcelado em 2x de R${:.2f} e seu total é R${:.2f}'.format(parc, x))
else:
    preco = x + tres
    num = (int(input('Quantas parcelas você deseja? ')))
    parc = preco / num
    print('O valor será parcelado em {}x de R${:.2f} e seu total é R${:.2f}'.format(num, parc, preco))