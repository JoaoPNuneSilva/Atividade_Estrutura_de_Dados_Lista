lista_de_filmes = []
def mostrar_lista_de_filmes():
    if len(lista_de_filmes) == 0:
        print("Sua lista de filmes assistidos está vazia!")
    else:
        print("Sua lista de filmes assistidos:")
        for item in lista_de_filmes:
            print("- " + item)

def adicionar_item():
    item = input("Digite o filme que deseja adicionar: ")
    lista_de_filmes.append(item)
    print("O filme " + item + " foi adicionado à sua lista de filmes assistidos.")

def editar_item():
    mostrar_lista_de_filmes()
    indice = int(input("Digite o número do filme que deseja editar: "))
    novo_item = input("Digite o novo filme que será inserido: ")
    lista_de_filmes[indice-1] = novo_item
    print("O filme " + str(indice) + " foi alterado para o filme " + novo_item + ".")

def remover_item():
    mostrar_lista_de_filmes()
    indice = int(input("Digite o número do filme que deseja remover: "))
    item_removido = lista_de_filmes.pop(indice-1)
    print("O filme " + item_removido + " foi removido da sua lista de filmes assistidos.")
    
def menu():
    while True:
        print("\nMENUZIN:")
        print("1 - Mostrar lista de filmes assistidos")
        print("2 - Adicionar filme à lista")
        print("3 - Editar filme da lista")
        print("4 - Remover filme da lista")
        print("5 - Sair do programa")
        opcao = int(input("Digite o número da opção desejada: "))
        if opcao == 1:
            mostrar_lista_de_filmes()
        elif opcao == 2:
            adicionar_item()
        elif opcao == 3:
            editar_item()
        elif opcao == 4:
            remover_item()
        elif opcao == 5:
            print("Obrigado por usar o programa! Volte sempre que houver mais filmes par adicionar!")
            break
        else:
            print("OPÁ! Opção inválida meu amigo. Tente novamente.")
menu()