# -- coding: utf-8 --


# mensagem = "olá mundo"
# print (mensagem)

# var1 = 1 #variavel interira
# var2 = 1.1 #variavel float
# var3 = "Eu sou uma string" #variavel string
# var4 = True #Verdadeiro
# var4 = False #False

# print(var1)
# print(var2)
# print(var3)
#print(var4)


#OPERADORES RELACIONAIS
# == Igual
# != Diferente
# > Maior
# < Menor 
# >= Maior igual
# <= Menor igual 

x = 1
y = 300



# print(x == y or x == z)

#Operadores Lógicos
# and duas condiçoes verdadeiras
# or pelo menos uma condiçao True
# not inverte valor

# if x > y:
#     print ("O valor de x é maior que y")
# else:
#     print ("O valor de Y é maior")

a = 7
b = 8

if b > a:
    if b > 0:
        print("b é maior que a\nb é positivo")
    else:
        print ("b é negativo")
else:
    print ("b é menor que a")




# laço de repetição while
# x = 1
# while x < 10: 
#     print(x)
#     x = x+1 

lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo","!"]
lista3 = [0, "ola","biscoito","bolacha",9.99,True]

for i in range(10,20,2):
    print(i)