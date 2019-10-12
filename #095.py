"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""

time = []
jogador = {}

while True:
    jogador = {'nome': input('Jogador: ').strip().capitalize()}
    gols = []
    partidas = int(input('Nº de partidas: '))
    for i in range(partidas):
        gols.append(int(input(f'Gols na partida {i + 1}: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        cont = input('Cadastrar outro jogador [S/N]? ').upper().strip()
        if cont in 'SN':
            break
        print('Opção inválida')
    if cont == 'N':
        break
print('='*50)

print(f'{"cod":<6}', end='')
for i in jogador.keys():  # cabeçalho
    print(f'{i:<15}', end='')
print()
print('=' * 50)
for i, j in enumerate(time):
    print(f'{i:<6}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('=' * 50)
while True:
    mostrar = int(input('Mostrar dados de qual jogador (999 interrompe)? '))
    if mostrar == 999:
        print('<FIM!>')
        break
    elif mostrar > len(time):
        print('ERRO! Jogador não cadastrado!')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {time[mostrar]["nome"]}:')
        for i, j in enumerate(time[mostrar]['gols']):
            print(f'No jogo {i + 1} fez {j} gols.')
        print('='*50)
