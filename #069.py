"""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

homem = 0
maior = 0
mulheres = 0
cadastro = 'S'
while True:
    if cadastro not in 'SN':
        print('Opção inválida')
    elif cadastro == 'N':
        print(f"""Quantas pessoas tem mais de 18 anos? {maior}
        Quantos homens foram cadastrados? {homem}
        Quantas mulheres tem menos de 20 anos? {mulheres}""")
        break
    while cadastro == 'S':
        print('Digite os dados para cadastro')
        idade = int(input('Idade: '))
        sexo = input('Sexo [F/M]: ').upper().strip()
        if sexo not in 'FM':
            print('Opção inválida.')
        if idade >= 18:
            maior += 1
        if idade < 20 and sexo == 'F':
            mulheres += 1
        if sexo == 'M':
            homem += 1
        cadastro = input('Deseja fazer um cadastro? [S/N]: ').strip().upper()
