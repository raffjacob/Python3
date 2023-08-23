""" 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input("Insira seu nome: ")

tamanho_nome = len(nome)
nome_curto = tamanho_nome <= 4
nome_medio = tamanho_nome >= 5 and tamanho_nome <= 6
nome_grande = tamanho_nome > 6

if nome_curto:
    print("Seu nome é curto")
elif nome_medio:
    print("Seu nome é medio")
else:
    print("Seu nome é grande")