# Exercicios_Python_-_Modulo_1
# Exercicio 1

#valor = float(input("digite um valor monetario"))

#new = valor*0.85

#print('O novo valor é ',new)

# Exercicio 2
#def check(idade,salario,sexo):
#        while idade>150 or idade<0:
#            print('idade invalida')
#            idade= int(input('digite idade valida'))
#        while salario < 0: 
#            print('salario invalida')
#            salario= float(input('digite salario valido'))
#        while sexo !=  'M' and sexo !=  'F' and sexo !=  'Outro':
#            print('sexo invalido')
#            sexo= input('digite sexo valido')
#        return(idade,salario,sexo)
#
#idade = int(input('idade:'))
#salario = float(input('salario:'))
#sexo= str(input('sexo(M,F,ou Outro):'))
#
#[idade,salario,sexo] = check(idade,salario,sexo)
#
#print('*** Dados validos ***\n', 'IDADE: ',idade,'SALARIO: ',salario,'SEXO: ',sexo)



# Exercicio 3

a= input('Mora perto da vítima? (S/N)')
b= input('Já trabalhou com a vítima?(S/N)')
c= input('Telefonou para a vítima?(S/N)')
d= input('Esteve no local do crime?(S/N)')
e= input('Devia para a vítima?(S/N)')

cont = 0

lista = (a,b,c,d,e)

for i in lista:
    if i == 'S':
        cont+=1
        
print('pontos: ',cont)
if cont == 5: 
    print('assassino.')
elif cont == 4 or cont == 3: 
    print('cumplice.')
elif cont == 2: 
    print('suspeito, necessita investigar.')
else:
    print('liberado')

# Exercicio 4

#operador = 9 

#for i in range(10):
#    print(operador,' x ',i+1,' = ', (i+1)*operador)
