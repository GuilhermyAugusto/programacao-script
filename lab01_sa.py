import random

nome = input("Digite seu nome: ")
sorteado = hash(nome)%100

contador = 0

while True:

    contador = contador + 1

    palpite_str = input ("Qual o seu palpite? ")
    palpite = int (palpite_str)
    if (sorteado > palpite):
        print ("É um número maior")
    elif (sorteado == palpite):
        # Parar de perguntar / sair do laço (while)
        break
    else:
        print ("É um número menor.")
        
print("Parabéns,", nome, "você acertou o número", sorteado, "em", contador, "tentativas!")
