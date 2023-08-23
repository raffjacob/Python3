""" 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input("Insira a hora: "))

logic_bomdia = hora >= 0 and hora <= 11
logic_boatarde = hora >= 12 and hora <= 17
logic_boanoite = hora >= 18 and hora <= 23

if logic_bomdia:
    print("Bom dia")
elif logic_boatarde:
    print("Boa tarde")
elif logic_boanoite: 
    print("Boa noite")
else:
    print("")