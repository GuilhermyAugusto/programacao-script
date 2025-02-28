#Recepção de variáveis
diastr = input("Insira o dia: ")
dia = int (diastr)
messtr = input("Insira o mês(número): ")
mes = int (messtr)
anostr = input("Insira o ano: ")
ano = int (anostr)
somadias=dia


#Soma de dias e verificação de ano bissexto
while (mes>0 and mes<12):
    mes=mes-1
    if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12):
        somadias=somadias+31
    elif(mes==2):
        if (ano%4==0 and ano%100!=0 or ano%400==0):
            fevereiro=29
        else:
            fevereiro=28  
    else:
        somadias=somadias+30
 

#Cálculo de Conway
valorano= ano%1000
calculo= int((((valorano%100)*11)+somadias)/30)


#Verificação da fase da lua
if (calculo>=0 and calculo<=1 or calculo==30):
    print("Lua Nova")
elif (calculo>=2 and calculo<=4):
    print ("Lua Crescente") 
elif (calculo>=5 and calculo<=8):
    print ("Quarto Crescente")
elif (calculo>=9 and calculo<=12):
    print ("Crescente Gibosa")
elif (calculo>=13 and calculo<=16):
    print ("Lua Cheia")
elif (calculo>=17 and calculo<=20):
    print ("Minguante Gibosa")
elif (calculo>=21 and calculo<=24):
    print ("Quarto Minguante")
elif (calculo>=25 and calculo<=29):
    print ("Lua Minguante")