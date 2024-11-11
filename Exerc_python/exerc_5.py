num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))

if num1 > num2 and num3:
    print("o 1 é maior do que 2 e o 3")
elif num2 > num1 and num3:
    print("o 2 é maior do que o 1 e o 3")
elif num3 > num1 and num2:
    print("o 3 é maior do que 1 e o 2")
else:
    print("Os números são iguais")