def soma(n1,n2):
    return n1 + n2

def produto(n1,n2):
    return n1 * n2

def restoDivisão(n1,n2):
    return n1 % n2

def separarResultados(texto):
    print("--------------------------- O resto de "+texto+"---------------------------------")


print("Olá, seja bem vindo ao programa de calculos")
separarResultados("Multiplicacao")
print("O resultado da soma entre os números 5 e 10 é "+str(soma(5, 10)))
separarResultados("Resto da divisão")
print("Entre os números 5 e 10 é "+str(restoDivisão(5,10)))