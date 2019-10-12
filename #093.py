"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato."""

dados = {'jogador': input('Jogador: ').strip().capitalize()}
gols = []
partidas = int(input('Nº de partidas: '))
for i in range(partidas):
    gols.append(int(input(f'Gols na partida {i}: ')))
dados['gols'] = gols[:]
dados['total'] = sum(gols)

print('='*50)
print(dados)
print('='*50)
for k, v in dados.items():
    print(f'- O campo {k} tem o valor {v}')
print('='*50)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for i in range(partidas):
    print(f'=> Na partida {i} fez {gols[i]} gols')
print(f'Foi um total de {dados["total"]} gols.')
