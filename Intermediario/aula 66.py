"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

#função  Parâmetros
def soma(x, y, z):
    #Definição
    print(f"X={x} y={y} z={z}"," | ", "x + y + z=", x+y+z)

#execução
soma(1,2,3)
soma(1, y=2, z=5)

print(1,2,3, sep="-")