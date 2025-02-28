import random

sorteado = random.randint(0, 100)

palpite_str = input ("Qual o seu palpite? ")
palpite = int (palpite_str)


while ( palpite != sorteado ):

    if (palpite>sorteado):
        print ("É um número menor.")
    
    elif(palpite<sorteado):
        print ("É um número maior")
    
    palpite_str = input ("Qual o seu palpite? ")
    palpite = int (palpite_str)
print ( "Acertou!" )