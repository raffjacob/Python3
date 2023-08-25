"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = "Meteora"
palavra_oculta = ""

for letra in palavra_secreta:
    palavra_oculta += "*"

palavra_oculta_bkp = palavra_oculta
tentativas = 0

#emjogo = True

while True:

    if "*" not in palavra_oculta:
        print("Parabéns! Você encontrou a palavra secreta!")
        print(f"A palavra secreta era: {palavra_oculta}")
        break

    print("Encontre a palavra secreta digitando uma letra por vez!")
    print(f"Você tem 10 tentativas. Tentativa atual: {tentativas}")
    print(f"A palavra a ser descoberta é: {palavra_oculta}")
    
    letra_digitada = input("Digite uma letra: ")

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra!")
        continue    
    if letra_digitada in palavra_secreta:
        print(f"Letra '{letra_digitada}' encontrada!")
        palavra_oculta = ""
        cont_palavra_secreta = 0
        indices_encontrados = ""
        
        for letra in palavra_secreta:
            if letra == letra_digitada:
                indices_encontrados += str(cont_palavra_secreta)
            cont_palavra_secreta += 1
        for indice in indices_encontrados:
            cont_indices = 0
            palavra_oculta = ""
            for letra in palavra_oculta_bkp:
                
                if letra == "*":
                    if cont_indices == int(indice):
                        palavra_oculta += letra_digitada
                    else:
                        palavra_oculta += "*"
                else:
                    palavra_oculta += letra
                    
                cont_indices += 1
            palavra_oculta_bkp = palavra_oculta
        continue
    else:
        print(f"Letra '{letra_digitada}' não foi encontrada. Tente novamente!")
        tentativas += 1
    if tentativas == 10:
        print(f"Você atingiu o número máximo de tentativas! Game over.")
        break
