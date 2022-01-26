def exercicio1():

    lista = (2, 3, 30, 20, 5, 2, 9)

    cont =0
    for i in lista: 
        if i%2== 0: 
            cont+=1 
    print('quantidade de pares: ',cont)

def exercicio2():

    nome = input('digite o nome:')
    for i in nome:
        print(i,'\n')

def exercicio3():

    lista_a = (2, 3, 30, 20, 5, 2, 9)
    lista_b = (1, 1, 1, 1, 1, 1, 1)


    c=[]
    for i in range(len(lista_a)):  
        c.append(lista_a[i]+ lista_b[i])       
    print(c)

def exercicio4():
    mes_duracao = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31,
        12:31
    }
    print(mes_duracao)
    print(type(mes_duracao))
    print(mes_duracao.keys())
    print(mes_duracao.values())
    print(mes_duracao.items())

    for chave in mes_duracao:
        print(f' {chave}: {mes_duracao[chave]}')
#exercicio1()
#exercicio2()
#exercicio3()
exercicio4()