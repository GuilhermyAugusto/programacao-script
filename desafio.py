numero= int(input ("Insira um número: "))
anterior=-1
atual=numero
calculo=-1
while(atual/10!=0):
    anterior=int(atual%10)
    atual=int(atual/10)
    calculo=int(atual%10)
    if(calculo==anterior):
        print('Existem números em sequência.')
        break
    elif(atual/10==0):
        print('Não existem números em sequência.')