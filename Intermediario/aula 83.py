# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
     "nome" : "aline",
     "altura" : "souza",
}

dados_pessoais = {
    "idade" : 16,
    "altura" : 1.60
}

pessoa_completa = {**pessoa, **dados_pessoais}

# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args,**kwargs):
    for chave,valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracao = {
    "arg1" : 1,
    "arg2" : 2,
    "arg3" : 3,
    "arg4" : 4,
    "arg5" : 5,

}

mostro_argumentos_nomeados(**configuracao)