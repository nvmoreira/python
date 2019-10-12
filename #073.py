"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""

times = ('Santos', 'Flamengo', 'São Paulo', 'Palmeiras', 'Corinthians', 'Atético MG', 'Bahia', 'Internacional',
         'Athlético PR', 'Botafogo', 'Grêmio','Ceará', 'Goiás', 'Vasco', 'Fortaleza', 'Cruzeiro', 'Chapecoense',
         'Fluminense', 'CSA', 'Avaí')
print(f'Os times que estão na série A do Brasileirão são: \n{times}')
print(f'Os cinco primeiros times são: \n{times[0:5]}')
print(f'Os últimos quatro colocados são: \n{times[16:21]}')
print(f'Times em ordem alfabética: \n{sorted(times)}')
print(f'A Chapecoense está na posição {times.index("Chapecoense") + 1}.')
