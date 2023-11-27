"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
refatorar : editar seu codigo
"""
                #valornulo
def soma(x, y , z=None):
    #se z não for um valor "nulo"
    if z is not None:
        print(f"{x=} {y=} {z=}", x+y+z)
    else:
        print(f"{x=} {y=}")

soma(1,2)
soma(3,5)
soma(100,200)
soma(7,9,0)
soma(y=9,z=0,x=7)
