print ("Qual temperatura você deseja converter?")
print("1-Celsius para Fahrenheit.")
print("2-Fahrenheit para Celsius.")
conversaostr = input("Opção desejada: ")
conversao= int(conversaostr)

if (conversao==1):
    temperaturastr = input("Insira a temperatura em Celsius: ")
    temperatura = float (temperaturastr)
    calculo = (temperatura*(9/5))+32
    print ("A temperatura convertida é ", calculo, " °F.")
elif(conversao==2):
    temperaturastr = input("Insira a temperatura em Fahrenheit: ")
    temperatura = float (temperaturastr)
    calculo = (temperatura-32)*(5/9)
    print ("A temperatura convertida é ", calculo, " °C.")
else:
     print ("Opção Inválida")