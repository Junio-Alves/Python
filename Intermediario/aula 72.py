# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.


def multiplier (*Multiplier):
    Mult = 1
    for multiplier in Multiplier:
        Mult *= multiplier
    
    return Mult

Multiplicador1 = multiplier(2,5,2)
print(Multiplicador1)

def parimpar (N):
    ParOuImpar = N % 2
    if ParOuImpar == 0:
        return (f"O NUMERO {N}, É PAR")
    return (f"O NUMERO {N}, É IMPAR")

print(parimpar(5))



        