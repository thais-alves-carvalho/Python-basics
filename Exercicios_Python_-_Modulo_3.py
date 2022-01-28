import os 
import pandas as pd 
import csv
#exercicio 1 

def exercicio1():
    with open('alunos.csv', 'r') as arquivo:
        for linha in arquivo:
            print(linha)

def exercicio2():
    #lista = []

    with open('alunos.csv', 'r') as arquivolido:
        with open('copiateste.csv', 'w') as arquivocriado:
            for linha in arquivolido:
                arquivocriado.write(linha)

def exercicio3():
    
    with open('alunos.csv', 'r') as arquivolido:

        new_alunos=[]
        leitor = csv.reader(arquivolido, delimiter = ',') #criando um leitor
        for linha in leitor:
            new_alunos.append(linha)


    for i,linha in enumerate(new_alunos):
        if i != 0:
            lista =linha[2:-1]
            lista_float = [float(item) for item in lista]
            media = sum(lista_float)/len(lista_float)
            linha.append(media)
            print(linha)
        else:
            linha.append('Media')
    print(new_alunos)

    with open('new_alunos.csv', 'w') as arquivo:
        escritor = csv.writer(arquivo, delimiter = ';', lineterminator = '\n') #criando um escritor    
        escritor.writerows(new_alunos) # writerows escreve cada "sublista" da lista como uma linha


    
def exercicio4():
    url = "https://swapi.dev/api/people/4/"
    #"name" (nome), "height" 
    #(altura), "mass" (massa) e "birth_year" (ano de nascimento) e imprima cada 
    #dado em uma linha.

def exercicio5():
    url = "https://api.covid19api.com/country/brazil"
#exercicio1()
#exercicio2()
#exercicio3()
exercicio4()
