
perguntas = [
    {
        "Pergunta" : "Quanto é 2+2?",
        "Opções" : ["1", "3", "4", "5"],
        "resposta" : "4",
    },
    {
        "Pergunta" : "Quanto é 5*5?",
        "Opções" : ["25", "55", "10", "51"],
        "resposta" : "25",
    },
    {
         "Pergunta" : "Quanto é 10/2",
        "Opções" : ["4","5","2","1"],
        "resposta" : "5",
    },

]

for Pergunta in perguntas:
    print("Pergunta: ", Pergunta.get("Pergunta"))
    
    