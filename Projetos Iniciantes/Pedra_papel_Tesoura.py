from termcolor import colored
import random
import os


options = ["r", "p", "t"]
#R = rocker(pedra), P= paper(papel), T= Tesoura
user_points = 0
computer_points = 0

while True:
    #Coletar resposta do usuario
    user_choice = input("Escolha [R] para Pedra, [P] para papel, [T] para tesoura e [Q] para desistir.\n").lower()

    #encerrar programa
    if user_choice == 'q':
        break

    #Verifica se o usuario digitou valor corretamente
    if user_choice not in options:
        (print("DIGITE UM VALOR VALIDO"))
        continue
        


    #gerar numero aleatorio
    computer_choice = random.randint(0, 2)
    computer_option = options[computer_choice]

    #empate
    if computer_option == user_choice:
        print("EMPATE")

    #Vitoria do jogador
    elif user_choice == "r" and computer_option == "t":
        print("VOÇÊ GANHOU")
        user_points += 1

    elif user_choice == "p" and computer_option == "r":
        print("VOÇÊ GANHOU")
        user_points += 1

    elif user_choice == "t" and computer_option == "p":
        print("VOÇÊ GANHOU")
        user_points += 1

    else:
        print("VOÇÊ PERDEU")
        computer_points += 1

    #Pontuação
    print(colored(f"A maquina escolheu: {computer_option}", "yellow"))
    print(colored(f"Sua pontuação é: {user_points}", "red"))
    print(colored(f"Pontuação da maquina é: {computer_points}", "green"))

    

    



