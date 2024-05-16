import random                                                           # importa o randomizador
numeroSecreto = random.randint(1,20)                              # A maquina seleciona um numero aleatoria
print("Seja Bem vindo(a), Tente adivinhar o numero que estou pensando") # inicia o programa dando boas vindas e explicando as regras
print("De 1 a 20")
print("voce tera 6 chances. Boa Sorte !!!")

for tentativas in range (1,7):                                          # entra no loop de erros ate que o jogador acerte o numero escolhido
    print("Diga um numero")
    numero = int(input())

    if numero < numeroSecreto:
        print("Chutou baixo, tente um pouco mais alto!!")

    elif numero > numeroSecreto:
        print("Chutou Alto, tente um pouco mais baixo!! ")

    else:
        break                                                          # encerra o loop caso jogador acerte o numero


if numero == numeroSecreto:                                           # Parabeniza o jogador e mostra o resultado
    if numero == numeroSecreto and tentativas == 1:
        print(f"Wow, Hoje voce esta cheio de sorte, acertou de primeira, meu numero é {numeroSecreto} Parabens !!")
    else:
        print(f"Na Mosca!!, O número que eu pensei e o {numeroSecreto}, voce acertou depois de {tentativas} Tentativas Parabens!!")

else:                                                                 # Caso nao acerte o numero e suas chances terminem
    print(f"Que pena, o numero que eu estava pensando é {numeroSecreto}, mais sorte na proxima!!!")
