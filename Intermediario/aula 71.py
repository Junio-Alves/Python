"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
 """
 #Lembre-te de desempacotamento

x , y, *resto = 1,2,3,4
print(x,y,resto)

def soma(*args):
    total = 0
    for number in args:
        print(f"Total: { total}, Numero: { number}")
        total += number
        print(f"Total{total}")
    print(total)

#soma(1,2,3,4,5,6,7,8,9,10)

def names (*Names):
    for names in Names:
        print(names)
    
names ("pedro","caio","junio")
names ("Lucas")
