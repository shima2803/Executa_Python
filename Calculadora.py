def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplica(a,b):
    return a * b

def divisao(a,b):
    
    if b == 0:
        print("Divisão com 0 está errado")
    
    return a / b
    
def menu():
    
    print("Bem Vindo a minha Calculadora\n Qual tipo de conta voê deseja fazer:")
    calculo = int(input("1-Somar \n 2-Subtrair \n 3-Dividir \n 4-Multiplicar \n Digite aqui de 1-4 o valor:"))
    num1 = int(input("Primeiro Numero:"))
    num2 = int(input("Segundo Numero:"))
    sair = False

    while sair == False:
        if calculo == 1:
            total = soma(num1,num2)
        elif calculo == 2:
            total = subtracao(num1,num2)
        elif calculo == 3:
            total = divisao(num1,num2)
        else:
            total = multiplica(num1,num2)

        print("O valor da conta é:",total)

        final = int(input("O que deseja fazer: \n 1-outra conta \n 2-Sair \n"))
        
        if final == 1:
            sair == True
        else:
            return


def main():
    
    menu()

main()
