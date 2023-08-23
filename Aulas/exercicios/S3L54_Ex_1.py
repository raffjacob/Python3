""" 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    number = int(input("Digite um numero: "))
    
    if (number%2) == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
except:
    print("O valor informado nao é numerico")

# outra forma

number = input("Digite um numero inteiro: ")

if number.isdigit():
    if (int(number) % 2) == 0:
        print("O numero é par")
    else:
        print("O numero é impar")
else: 
    print("O valor informado nao é numerico")
