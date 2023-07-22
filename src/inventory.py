
itens = [
    [1, 'Espada'],
    [2, 'Chave'],
    [3, 'Escudo']
]

def display():
    print("\t-----------")
    print("\tInventário")
    print("\t1 - Mostrar Itens")
    print("\t2 - Sair")

def mostrar_tudo():
    print("Numero\tItem")
    for item in itens:
        print ("{0}\t{1}".format(item[0], item[1]))

while(True):
    display()
    escolha = int(input())
    if escolha == 1:
        mostrar_tudo()
    elif escolha == 2:
        print ("Tchau")
        break