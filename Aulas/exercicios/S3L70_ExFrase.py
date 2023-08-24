frase = "O Python é uma linguagem de programação " \
"multiparadigma. " \
"Python foi criado por Guido van Rossum."

i = 0
count_letra = 0
while i < len(frase):
    
    letra = frase[i]
    i += 1
    if letra == " ":
        continue
    if count_letra < frase.count(letra):
        
        count_letra = frase.count(letra)
        letra_encontrada = letra

print(f"A letra que apareceu mais vezes foi a: {letra_encontrada}")
