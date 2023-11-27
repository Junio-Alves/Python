# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

def criar_multiplicacao(multiplicador):
    def multiplica(n):
        return n*multiplicador
    return multiplica
    
duplicar = criar_multiplicacao(2)
triplicar = criar_multiplicacao(3)
quadruplicar = criar_multiplicacao(4)

print(duplicar(3))
print(triplicar(6))
    
    
