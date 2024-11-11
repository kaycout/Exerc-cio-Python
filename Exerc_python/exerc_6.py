turno = input("Digite qual turno você estuda M, V, N: ")
turno = turno.upper()
matutino = "Bom dia!"
vespertino = "Boa tarde!"
noturno = "Boa noite!"

if turno == "M":
    print(matutino)

elif  turno == "V":
    print(vespertino)

elif turno == "N":
    print(noturno)
else:
    ("valor invalido")
    print("Turno não reconhecido")