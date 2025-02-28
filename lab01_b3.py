pesostr = input("Insira seu peso(em kg): ")
peso = float (pesostr)
alturastr = input("Insira sua altura(em metros): ")
altura = float (alturastr)

imc = peso/(altura*altura)

print ("Seu imc é: ", imc)
if (imc>30):
    print ("Alerta! Seu IMC indica obesidade.")
elif (imc<16.4):
    print ("Alerta! Seu IMC indica magreza.")