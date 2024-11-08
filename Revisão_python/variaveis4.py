alimentos = ["Maça","Arroz","Feijão"]
categoria = ("Grãos", "Frutas", "Legumes")
pessoa = {"Nome":"Paula","Idade":"38","Altura":"1.65"}

print(alimentos)
print(type(alimentos))
print(len(alimentos))
# adicionar mais um elemento
alimentos.append("Macarrão")
print(alimentos)
print(len(alimentos))

print(categoria)
print(type(categoria))
print(len(categoria))

print(pessoa)
print(type(pessoa))
print(len(pessoa))
# adicionar um item a pessoa 
# adicionar uma nova chave com seu respectivo valor
# está sendo adicionado a chave email com o valor sendo o
# email da pessoa.
pessoa["email"]="paula@gmail.com"
print(pessoa)
print(len(pessoa))