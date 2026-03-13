tarefas = []

def menu():
    print("Bem Vindo ao sua Lista de Tarefa")
    escolha = int(input("1-Adicionar Tarefa \n2-Listar Tarefa \n3-Remover Tarefa \n4-Sair \n"))

    if escolha == 1:
        Adicionar()
    elif escolha == 2:
        Listar()
    elif escolha == 3:
        remover()
    else:
        sair()

def Adicionar():
    print("\nQue tarefa você deseja adicioanr:\n")
    tarefa = input("")
    tarefas.append(tarefa)
    print("\nA tarefa ",tarefa," foi adicionado na lista")
    menu()

def Listar():
    print("\nMostrando Lista: \n")
    
    for i, tarefa in enumerate(tarefas):
        print(i + 1, "-", tarefa)
    menu()

def remover():
    print("\nQual item voce deseja remover:")

    for i, tarefa in enumerate(tarefas):
        print(i + 1, "-", tarefa)
    
    remove = int(input("\nEscolha em Numero qual voce quer remover:"))
    tarefas.pop(remove - 1)
        
    print("\nSua lista ficou:")    
    for i, tarefa in enumerate(tarefas):
        print(i + 1, "-", tarefa)
    
    menu()

def sair():
    print("\nObrigado, Até Logo")

def main():
    menu()

main()    