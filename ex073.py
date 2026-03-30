#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times= ('Flamengo','Palmeiras','Corinthians','Santos','Cruzeiro','Gremio','Atlético','Santos','Botafogo','Bahia','Internacional','Chapecoense','São Paulo','Bragantino','Fluminese','Mirassol')
timesalfa= sorted(times)

print(f'Lista de Times do brasileirão: {times}')
print('-='*25)
print(f'Os 5 primeiros são: {times[0:6]}')
print('-='*25)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética: {timesalfa}')
print('-='*25)
print(f'O Chapecoense está na {times.index ("Chapecoense")+1}ª posição')