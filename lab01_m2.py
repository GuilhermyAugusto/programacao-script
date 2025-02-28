notastr = input("Insira a sua nota (entre 0 e 100): ")
nota= int(notastr)

if (nota>=0 and nota<=100):
    if(nota>=90):
        print("A nota ", nota, " traduz-se para o conceito A.")
    elif(nota>=75 and nota<90):
        print("A nota ", nota, " traduz-se para o conceito B.")
    elif(nota>=60 and nota<75):
        print("A nota ", nota, " traduz-se para o conceito C.")
    elif(nota>=40 and nota<60):
        print("A nota ", nota, " traduz-se para o conceito D.")
    else:
       print("A nota ", nota, " traduz-se para o conceito F.") 
else:
    print("Nota Inválida, insira uma nota entre 0 e 100.")