lista = []
soma = 0
tamanho = int(input("Quantos numeros voce quer na lista:"))
i = 0
maior = 0
procurar = 7

while i < tamanho: 
    print("Que Numero voce quer adicionar:")
    tarefa = input("")
    lista.append(tarefa)
    i+=1

print("Mostrando Lista")
for item in lista:
    print(item)

print("Fazendo Soma de Numeros")
for item in lista:
    soma += int(item)
print(soma)   

print("Mostrando o maior")
for item in lista:
    if int(item) > maior:
        maior = int(item)
print(maior)

print("Mostrando Pares:")
for item in lista:
    if int(item) % 2 == 0:
        print("è par:",item)

print("Procurando Numero 7 na lista")
for procura in lista:
    if procurar == int(procura):
        print("O numero 7 esta")


print("Que numero voce quer remover:")
qtd1 = int(input(""))
for remove in lista:
    if qtd1 == int(remove):
        lista.remove(remove)
        break
    
print("Mostrando a lista no final:")
for final in lista:
    print(final)