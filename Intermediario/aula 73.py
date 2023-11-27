"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg, nome):
   return f"{msg}, {nome}"

def executar(funcao, *arg):
   return funcao(*arg)

print(executar(saudacao, "Bom dia", "Junio")) 
print(executar(saudacao, "Boa noite", "Lucas")) 