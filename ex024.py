#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
ci= input('Em que cidade voce nasceu? ').strip().title()

print(ci[0:5] == 'Santo')
