print("Informe o tamanho dos lados do triângulo:")
ladoastr = input("Qual o tamanho do lado A: ")
ladoa= int(ladoastr)
ladobstr = input("Qual o tamanho do lado B: ")
ladob= int(ladobstr)
ladocstr = input("Qual o tamanho do lado C: ")
ladoc= int(ladocstr)

if((ladoa+ladob)>ladoc):
    if(ladoa==ladob==ladoc):
        print("É um Triângulo Equilátero.")
    elif(ladoa==ladob!=ladoc or ladoa==ladoc!=ladob or ladoc==ladob!=ladoa):
        print("É um Triângulo Isóceles.")
    else:
        print("É um Triângulo Escaleno.")
else:
    print ("Esse Triângulo não existe!")