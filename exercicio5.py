numero1= int(input("digite um numero: "))
numero2 = int(input("digite outro numero: "))
sinal = input("digite um sinal de +, -, *: ")

if sinal == '-':
    resultado = (numero1 - numero2)
    print(resultado)
elif sinal == '+':
    resultado = (numero1 + numero2)
    print(resultado)
elif sinal == '*':
    resultado = (numero1 * numero2)
    print(resultado)
elif sinal == '/':
    if numero2 != 0:
        resultado = (numero1 / numero2)
        print(resultado)
else:
    resultado = "sinal invalido"

print(f"o resultado da operaçao é: {resultado}")
