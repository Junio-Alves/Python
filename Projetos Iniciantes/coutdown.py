import time
z = 0
t = input("Digite o tempo(em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada invalida")
    quit()

#quando (t), for igual a 0, ele vira false
#while t:
    #minutes, seconds = divmod(t, 60)
    #timer = "{:02d}:{:02d}".format(minutes,seconds)
    #print(timer, end="\r")
    #time.sleep(1)
    #t -= 1






#CONTADOR DE 0 ATE O VALOR DEFINIDO EM SEGUNDOS    

#DEFINE O VALOR MAXIMO EM MINUTOS
minutes, seconds = divmod(t,60)
timer = "{:02d}:{:02d}".format(minutes, seconds)
while t:
    
    #COMEÇA CONTAR APARTIR DE 0
    minutes1, seconds1 = divmod(z,60)
    timer1 = "{:02d}:{:02d}".format(minutes1, seconds1)
    
    print(timer1, end="\r")
    time.sleep(1)
    
    z += 1

    #QUANDO O CONTADOR ANTIGIR O VALOR MAXIMO PRE-DEFINIDO, ELE PARA A CONTAGEM.
    if timer1 == timer: 
        time.sleep(3)
        print("TEMPO ACABOU")
        break


