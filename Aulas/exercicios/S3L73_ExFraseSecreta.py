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

palavra_secreta = "Meteora"
palavra_oculta = ""

for letra in palavra_secreta:
    palavra_oculta += "*"

palavra_oculta_bkp = palavra_oculta
tentativas = 0

#emjogo = True

while True:
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
        for letra in palavra_secreta:
            if letra == letra_digitada:
                
                for letra2 in palavra_oculta_bkp:
                    if letra2 == "*":
                        palavra_oculta += letra
                    else:
                        palavra_oculta += letra2
                palavra_oculta += letra_digitada
            else:
                palavra_oculta += "*"
        continue
    else:
        print(f"Letra '{letra_digitada}' não foi encontrada. Tente novamente!")
        tentativas += 1
    if tentativas == 10:
        print(f"Você atingiu o número máximo de tentativas! Game over.")
        break
