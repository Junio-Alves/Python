# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = "nome"

pessoa[chave] = "Luiz Otavio"
pessoa["sobrenome"] = "Miranda"

print(pessoa[chave])

pessoa[chave] = "Maria"

del pessoa["sobrenome"]
print(pessoa)
print(pessoa["nome"])

if pessoa.get("sobrenome") is None:
    print("Não Existe")
else:
    print(pessoa["sobrenome"])