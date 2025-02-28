#Código para somar um número a todos os seus antecessores
n=int(input('Qual o número: '))
soma=0
c=0
while(c<=n):
    soma=soma+c
    c +=1
print(soma)
