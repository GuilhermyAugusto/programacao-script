numerostr = input("Digite um número positivo inteiro: ")
numero = int (numerostr)

if(numero>=0):
    fatorial=numero-1
    calculo=numero
    while (fatorial<numero and fatorial>1):
        calculo = calculo*fatorial
        fatorial=fatorial-1
    
    print(numero, "! =", calculo)
    
else:
    print("Número Inválido.")