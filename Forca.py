# M1 - Introdução a Programação
# Jogo da Forca
# Versão Teste (Att 12/06/2022):

# Importação de Bibliotecas:
import random
import pandas as pd
import unidecode
import os
import time
from collections import Counter

# Declaração inicial das variáveis:
players = []
nivel = "Difícil"
numerros = 6
opc = 0

# Definição das Funções:
  ## Verificações dos inputs:
def verifyletter(user_input):
    while (len(user_input) != 1) or (user_input.isalpha() == False):
        user_input = input("Desculpe. Não entendi. Digite apenas uma letra alfabética: ")
    letter = unidecode.unidecode(user_input.lower())
    return letter
    ### Regra 3 (Indiferenciação entre maiúsculas e minúsculas).
    ### As verificações são feitas todas com variáveis em lower(), depois as impressões são feitas com as variáveis normais...
def verifyword(user_input):  # Verificar se a palavra é válida
    while (len(user_input) < 2) or (user_input.isalpha() == False):
        user_input = input("Palavra inválida. Digite uma palavra com o mínimo de dois caracteres (apenas letras do alfabeto): ")
    word = user_input
    return word
def transformword(user_input):  # Transformar a word em palavra (lower e sem acento)
    palavra = unidecode.unidecode(user_input.lower())
    return palavra
def verifyname(playername):
    while (len(playername) < 2) or (len(playername) > 12) or (playername.isalnum() == False):
        playername = input("Nome inválido. Digite um nome entre 2 e 12 caracteres (apenas letras e números): ")
    return playername
  ## Login:
def login():
    old = "n"
    while old in "Nn":
        playername = input("Nome do Jogador: ")
        playername = verifyname(playername)
        old = verifyplayers(playername)
    playerpoints = getpoints(playername)
    print("\nBoas vindas {}! \nLogin efetuado com sucesso. \nPontuação atual: {}".format(playername, playerpoints))  # Retornar a pontuação do arquivoBaseDadosSql?
    return playername
def login2():
    old = "n"
    print("\nPara isso, precisamos fazer o login do(a) Jogador(a) 2.")
    while old in "Nn":
        playername = input("Nome do Jogador 2: ")
        playername = verifyname(playername)
        old = verifyplayers(playername)
    playerpoints = getpoints(playername)
    print("\nBoas vindas {}! \nLogin efetuado com sucesso. \nPontuação atual: {}".format(playername, playerpoints))  # Retornar a pontuação do arquivoBaseDadosSql?
    return playername
    ### Verificação nos logins / Pontuações:
def verifyplayers(playername):
    c = 0
    with open("nomespontos.txt", "r", encoding="utf-8") as nomespontos:
        for line in nomespontos:
            if line.startswith(playername + ","):
                c += 1
    if c == 1:
        old = input("Já existe um(a) Jogador(a) chamado(a) {}. É você mesmo? \n"
                    "('S' para sim, 'N' para não)".format(playername))
        while old not in ["S", "s", "N", "n"]:
            old = input("Desculpe, não entendi. Caso sejas o(a) Jogador(a) {}, digite 'S'."
                        " Caso deseje entrar com outro nome, digite 'N'\n".format(playername))
        return old
    elif c == 0:
        new = input("Não temos registro de um(a) Jogador(a) chamado(a) {}. Deseja cadastrar-se como um(a) novo(a) Jogador(a)? \n"
                    "('S' para sim, 'N' para não)".format(playername))
        while new not in ["S", "s", "N", "n"]:
            new = input("Desculpe, não entendi. Caso deseje entrar como {}, digite 'S'."
                        " Caso deseje entrar com outro nome, digite 'N'\n".format(playername))
        if new in "Ss":
            writenewplayer(playername) # Cadastrar o novo jogador em nomespontos.txt
            old = "S"
            return old
        elif new in "Nn":
            old = "N"
            return old
    else:
        print("Erro: Mais de um nome..?")
        old = "N"
        return old
    ### Novo Cadastro:
def writenewplayer(playername):
    with open("nomespontos.txt", "a", encoding="utf-8") as nomespontos:
        nomespontos.write(playername + ", " + "0\n")
    ### Ler os pontos:
def getpoints(playername):
    points = 0
    with open("nomespontos.txt", "r", encoding="utf-8") as nomespontos:
        for line in nomespontos:
            if line.startswith(playername + ","):
                playerpoint = line.split(", ")
                points = int(playerpoint[1])
    return points
def writepoints(playername, gamepoints):
    count = -1
    with open("nomespontos.txt", "r", encoding="utf-8") as oldnomespontos:
        newnomespontos = oldnomespontos.readlines()
        for line in newnomespontos:
            count += 1
            if line.startswith(playername + ","):
                i = count
                playerpoint = line.split(", ")
                oldpoints = int(playerpoint[1])
                newpoints = oldpoints + gamepoints
                newnomespontos[i] = "{}, {}\n".format(playername, newpoints)
                break
    with open("nomespontos.txt", "w", encoding="utf-8") as oldnomespontos:
        oldnomespontos.writelines(newnomespontos)
    return print("\n{} pontos adicionados para {}.\n"
                 "Total de pontos: {}".format(gamepoints, playername, newpoints))
def escolhatema():
    listatemas = []
    listaescolhas = []
    for file in os.listdir("Temas/"):
        splited = file.split(".")
        listatemas.append(splited[0])
    while True:
        print("Temas:")
        for i in range(len(listatemas)):
            listaescolhas.append(i+1)
            print("{}. {};".format(i+1,listatemas[i]))
        escolha = int(input("\nSelecione o número referente ao tema escolhido: "))
        while escolha not in listaescolhas:
            escolha = int(input("Desculpe, não entendi. Digite apenas o número antes do tema escolhido: "))
        escolhido = listatemas[escolha-1]
        confirmacao = input("Tema escolhido: {}.\n"
              "Confirma a escolha? (\"S\" ou \"N\")".format(escolhido))
        while confirmacao not in ["S", "s", "N", "n"]:
            confirmacao = input("Desculpe, não entendi. Digite \"S\" caso deseje confirmar o tema {} ou \"N\" caso deseje escolher outro tema.".format(escolhido))
        if confirmacao in ["S", "s"]:
            return escolhido
def getrandomtema():
    temaslist = []
    for file in os.listdir("Temas/"):
        splited = file.split(".")
        temaslist.append(splited[0])
    tema = random.choice(temaslist)
    return tema
def getrandomword(escolhido):
    wordlist = []
    listaescolhas = []
    with open("Temas\{}.txt".format(escolhido), "r", encoding="utf-8") as words:
        for line in words:
            wordlist.append(line.strip())
    word = random.choice(wordlist)
    return word
def tema1x1():
    opctema = int(input("\nDesejam selecionar um tema existente ou nomear um?\n"
                        "1. Selecionar um tema;\n"
                        "2. Digitar um tema próprio.\n"
                        "\n"
                        "Digite 1 ou 2: "))
    while opctema not in [1, 2]:
        opctema = int(input("Desculpe, não entendi. Digite \"1\" caso desejem selecionar um tema existente "
                            "ou \"2\" caso pretendam escrever o nome do tema para este jogo."))
    if opctema == 1:
        tema = escolhatema()
    else:
        while True:
            tema = input("Nome do tema: ")
            while (len(tema) < 2):
                tema = input("Tema inválido. Digite uma palavra com o mínimo de dois caracteres: ")
            opctema2 = input("Tema escolhido: {}.\n"
                             "Confirma que está correto? (\"S\" ou \"N\") ".format(tema))
            while opctema2 not in ["S", "s", "N", "n"]:
                opctema2 = input("Desculpe, não entendi. Digite \"S\" caso confirme que o tema {} está correto.\n"
                                 "Caso queira escrever novamente, digite \"N\"\n".format(tema))
            if opctema2 in ["S", "s"]:
                break
            else:
                continue
    return tema


  ## Menu Principal:
def menuprincipal():
    print('\nMenu Principal: \n'
          '1. Demostração \n'
          '2. Player_1 vs Computador \n'
          '3. Player_1 vs Player_2\n'
          '4. Registro de Pontuações\n'
          '5. Configurações\n'
          '6. Encerrar o Jogo\n')
    opc = input("Digite o número correspondente a opção desejada: ")
    while opc not in ["1", "2", "3", "4", "5", "6"]:
        opc = input("Desculpe, não entendi. Digite apenas o número que corresponde a opção desejada: ")
    return opc
  ## Menu Demonstrações:
def menudemos():
    print('\nDemonstrações: \n'
          '1. Tutorial (Funcionamento do Jogo)\n'
          '2. Demostração Aleatória\n'
          '3. Demonstração Inteligente\n'
          '4. Retornar ao Menu Principal\n')
    opcd = input("Digite o número correspondente a opção desejada: ")
    while opcd not in ["1", "2", "3", "4"]:
        opcd = input("Desculpe, não entendi. Digite apenas o número que corresponde a opção desejada: ")
    return opcd
    ### Tutorial:
def placardemo(playerdemo, wordstatus, t, a, e):
    e0 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |           " + "                         \n" + \
         "            |           " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e1 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |           " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e2 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /       " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e3 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   / \     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e4 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e5 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |   /       " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e6 = "Status: \n" + \
         " " * round(15 - (len(playerdemo) / 2)) + f"{playerdemo}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |   / \     " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    status = [e0, e1, e2, e3, e4, e5, e6]
    return print(status[e])
def demo1():
    # Reset das variáveis:
    numerros = 6
    playerdemo = "Fulano"
    pontos = 0
    demo1list = ["Braga", "Guarda", "Leiria"]
    tema = "Distritos de Portugal"
    word = random.choice(demo1list)
    palavra = word.lower()
    wordstatuslist = []
    for i in range(len(word)):
        wordstatuslist.extend("_")
    wordstatus = "".join(wordstatuslist)
    t = 0
    a = 0
    e = 0
    tentadas = []

    # Descrição inicial:
    print("\nTema: {}. \n"
          "Atenção: A palavra tem {} letras. Você pode errar até {} vezes."
          .format(tema, len(palavra), numerros - 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Descrição inicial: Antes de iniciar, você verá o Tema da palavra secreta, \n"
                        "a quantidade de letras e o número de erros possíveis antes do enforcamento.\n"
                        "----------------------- Digite <Enter> para continuar... -----------------------\n")
    placardemo(playerdemo, wordstatus, t, a, e)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Status: Em cada etapa, você poderá acompanhar a situação atualizada. \n"
                        "Nele constará seu nome (Fulano), a visualização da sua situação de enforcamento, \n"
                        " a palavra secreta ({}), o número de tentativas realizadas, o número de acertos \n"
                        "e o número de erros até o momento.\n"
                        "----------------------------------- <Enter> ------------------------------------\n"
                        .format(wordstatus))

    # Primeira tentativa: Exemplo de acerto simples
    print("{}ª tentativa: ".format(t + 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Tentativas: Chegou a hora de tentar acertar alguma letra da palavra secreta! \n"
                        "Só é possível digitar uma única letra de cada vez. \n"
                        "Vamos tentar a letra: \"{}\""
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[1]))
    letra = palavra[1]
    t += 1
    tentadas.extend(letra)
    for i in range(len(palavra)):
        if letra == palavra[i]:
            pontos += 1
            a += 1
            print("Acertou a letra " + word[i] + "!")
            wordstatuslist[i] = word[i]
            wordstatus = "".join(wordstatuslist)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Como a letra estava na palavra, apareceu a mensagem \"Acertou a letra " + word[1] + "!\n"
                        "Para cada acerto, você ganha 1 ponto."
                        "\n----------------------------------- <Enter> ------------------------------------\n")
    placardemo(playerdemo, wordstatus, t, a, e)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Após cada tentativa aparecerá o status atualizado. \n"
                        "Perceba que a palavra secreta agora mostra a letra encontrada. \n"
                        "O número de tentativas e acertos também foram atualizados."
                        "\n----------------------------------- <Enter> ------------------------------------\n")

    # Segunda tentativa: Exemplo de acerto duplo
    print("{}ª tentativa: ".format(t + 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Vamos tentar mais uma vez! \n"
                        "Que tal a letra \"{}\"?"
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[2]))
    letra = palavra[2]
    t += 1
    tentadas.extend(letra)
    for i in range(len(palavra)):
        if letra == palavra[i]:
            pontos += 1
            a += 1
            print("Acertou a letra " + word[i] + "!")
            wordstatuslist[i] = word[i]
            wordstatus = "".join(wordstatuslist)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Nossa! Agora apareceram duas mensagens de acerto!\n"
                        "Como a palavra possui a letra \"{}\" duas vezes, foram contados dois acertos."
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[2]))
    placardemo(playerdemo, wordstatus, t, a, e)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Perceba como o número de tentativas e o número de acertos estão diferentes."
                        "\n----------------------------------- <Enter> ------------------------------------\n")

    # Terceira tentativa: Erro simples
    print("{}ª tentativa: ".format(t + 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Pronto para mais uma? \n"
                        "Que tal agora a letra \"c\"?"
                        "\n----------------------------------- <Enter> ------------------------------------\n")
    letra = "c"
    t += 1
    tentadas.extend(letra)
    if letra not in palavra:
        print("Que pena, não acertou dessa vez...")
        e += 1
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Infelizmente não acertamos dessa vez...\n"
                        "A palavra secreta não possui a letra \"c\". Isso conta como uma tentativa errada."
                        "\n----------------------------------- <Enter> ------------------------------------\n")
    placardemo(playerdemo, wordstatus, t, a, e)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Perceba como agora sua cabeça está aparecendo na Forca.\n"
                        "O número de erros também foi atualizado no status."
                        "\n----------------------------------- <Enter> ------------------------------------\n")

    # Quarta tentativa: Letras repetidas, números ou mais de uma letra...
    print("{}ª tentativa: ".format(t + 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Vamos tentar novamente. \n"
                        "É preciso atenção na hora de digitar a letra. \n"
                        "O jogo não permite introduzir letras repetidas. \n"
                        "Quer testar? Vamos repetir a letra \"c\"."
                        "\n----------------------------------- <Enter> ------------------------------------\n")
    letra = "c"
    if letra in tentadas:
        print("Já digitou essa letra. Tente outra: ")
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Também não é possível digitar mais de uma letra. \n"
                        "Exemplo: \"{}\"."
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[4] + palavra[3]))
    letra = str(palavra[4] + palavra[3])
    if (len(letra) != 1) or (letra.isalpha() is False):
        print("Desculpe. Não entendi. Digite apenas uma letra alfabética: ")
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Logicamente, também não é possível digitar números. \n"
                        "Exemplo: \"5\"."
                        "\n----------------------------------- <Enter> ------------------------------------\n")
    letra = str(5)
    if (len(letra) != 1) or (letra.isalpha() is False):
        print("Desculpe. Não entendi. Digite apenas uma letra alfabética: ")

    # Ainda Quarta tentativa: Maiúscula ou Minúscula...
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Não desanime! Nenhuma tentativa inválida é contabilizada como erro. \n" \
                        "Vamos tentar mais uma vez! \n"
                        "Que tal agora a letra \"{}\"?"
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[0]))
    letra = palavra[0]
    t += 1
    tentadas.extend(letra)
    for i in range(len(palavra)):
        if letra == palavra[i]:
            pontos += 1
            a += 1
            print("Acertou a letra " + word[i] + "!")
            wordstatuslist[i] = word[i]
            wordstatus = "".join(wordstatuslist)
    placardemo(playerdemo, wordstatus, t, a, e)
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Finalmente acertamos mais uma!\n"
                        "A primeira letra da palavra secreta era \"{}\".\n"
                        "Mesmo colocando a letra no seu formato minúsculo (\"{}\"), contou como acerto.\n"
                        "Ou seja, o jogo não diferencia entre letras maiúsculas e minúsculas."
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(word[0], palavra[0]))

    # Completar o resto...
    print("{}ª tentativa: ".format(t + 1))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Já consegue descobrir qual a palavra secreta? Vamos seguir até completar!\n"
                        "A próxima letra deve ser \"{}\"."
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(palavra[3]))
    letra = palavra[3]
    t += 1
    tentadas.extend(letra)
    for i in range(len(palavra)):
        if letra == palavra[i]:
            pontos += 1
            a += 1
            print("Acertou a letra " + word[i] + "!")
            wordstatuslist[i] = word[i]
            wordstatus = "".join(wordstatuslist)
    placardemo(playerdemo, wordstatus, t, a, e)
    if a < len(palavra):
        msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                            "Estamos quase lá. Só mais uma!"
                            "\n----------------------------------- <Enter> ------------------------------------\n")
        print("{}ª tentativa: ".format(t + 1))
        if word == "Leiria":
            msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                                "A próxima letra só pode ser \"{}\"."
                                "\n----------------------------------- <Enter> ------------------------------------\n"
                                .format(palavra[5]))
            letra = palavra[5]
        elif word == "Guarda":
            msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                                "A próxima letra deve ser \"{}\"."
                                "\n----------------------------------- <Enter> ------------------------------------\n"
                                .format(palavra[4]))
            letra = palavra[4]
        t += 1
        tentadas.extend(letra)
        for i in range(len(palavra)):
            if letra == palavra[i]:
                pontos += 1
                a += 1
                print("Acertou a letra " + word[i] + "!")
                wordstatuslist[i] = word[i]
                wordstatus = "".join(wordstatuslist)
        placardemo(playerdemo, wordstatus, t, a, e)

    # Finalização:
    if a == len(palavra):
        print("Parabéns!! Você descobriu a palavra!!")
        pontos += 10  # Atualizar direto na base de dados SQL?
        msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                            "Agora que acertamos todas as letras da palavra, vamos a contagem dos pontos:\n"
                            "Você recebe 1 ponto para cada letra acertada.\n"
                            "Ainda soma-se mais 10 pontos se acertar a palavra e evitar o enforcamento.\n"
                            "Caso seja enforcado antes de acertar a palavra completa, perde-se 10 pontos."
                            "\n----------------------------------- <Enter> ------------------------------------\n")
    else:
        print("erro?")
    print("{}, você ganhou {} pontos nesta partida. Seu total de pontos é {}."
          .format(playerdemo, pontos, pontos))
    msgtutorial = input("\n----------------------------------- Tutorial -----------------------------------\n"
                        "Ganhamos {} pontos pelas {} letras acertadas.\n"
                        "Ganhamos mais 10 pontos por completar a palavra!\n\n"
                        "Pronto para a ação!?\n"
                        "Retorne ao Menu e inicie um jogo contra o computador ou contra um adversário!"
                        "\n----------------------------------- <Enter> ------------------------------------\n"
                        .format(a, a))
    return
    ### Demonstração 1 (Regra 9.1):

    ### Demonstração 2 (Regra 9.2):
def demoaleat():
    playerdemo = "Sicrano"
    nivel = "Difícil"  ## Se der tempo... Ir buscar o nivel fora e incluir como parametro?
    numerros = 6
    pontos = 0
    t = 0
    a = 0
    e = 0
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    tentadas = []
    wordstatuslist = []

    tema = getrandomtema()  # Buscar o tema aleatoriamente...
    word = getrandomword(tema)  # Escolher palavras aleatoriamente de acordo com o tema...
    palavra = transformword(word)  # Transformar em minuscula, sem acento...

    # Ajuste variáveis de verificação (wordstatuslist - lista) e de visualização (wordstatus - str)
    for i in range(len(word)):
        wordstatuslist.extend("_")
    wordstatus = "".join(wordstatuslist)

    # Preparação para o início do jogo:
    print("\nTema: {}. \n"  # Imprimir o tema da palavra antes da primeira tentativa (Regra 7)
          "Nível: {}. \n"
          "Atenção: A palavra tem {} letras. Você pode errar até {} vezes."
          .format(tema, nivel, len(palavra), numerros - 1))
    time.sleep(2)
    placardemo(playerdemo, wordstatus, t, a, e)
    time.sleep(2)

    # Loop do jogo em si (dentro do loop de configuração de um novo jogo):
    while a < len(palavra) and e < numerros:
        letter = random.choice(alfabeto)  # input aleatório do computador
        letra = verifyletter(letter)  # Função: verificacao letra
        print("{}ª tentativa: {}".format(t + 1, letra))
        time.sleep(1)
        while letra in tentadas:
            letra = verifyletter(random.choice(alfabeto))
            print("Já digitou essa letra. Tente outra: {}".format(letra))
            time.sleep(1)
        t += 1
        tentadas.extend(letra)
        if letra not in palavra:
            print("Não acertou...")
            time.sleep(1)
            e += 1
        elif letra in palavra:
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    pontos += 1
                    a += 1
                    print("Acertou a letra " + word[i] + "!")
                    wordstatuslist[i] = word[i]
                    wordstatus = "".join(wordstatuslist)
                    time.sleep(1)
                else:
                    continue
        placardemo(playerdemo, wordstatus, t, a, e)  # Visualização do placar
        time.sleep(1)
    # Ao sair do loop: Verificação do motivo para o final do jogo: Acertou a palavra / Enforcado
    if a == len(palavra):
        print("Parabéns!! Você descobriu a palavra e foi salvo da Forca!!")
        pontos += 10
    elif e == numerros:
        print("Que pena! Você foi enforcado antes de descobrir a palavra... \n"
              "A palavra era: {}.\n".format(word))
        pontos = pontos - 10
    print("\n{} pontos adicionados.\n".format(pontos))
    time.sleep(3)
def chuteinteligente(tema, wordstatuslist, tentadas):
    letraslist = []
    flist = []
    for w in wordstatuslist:
        w = w.lower()
    with open(f"Temas/{tema}.txt", "r", encoding="utf-8") as f:
        for line in f:
              flist.append(line.strip())
        if len(wordstatuslist) == wordstatuslist.count("_"):
            for word in flist:
                if len(word) == len(wordstatuslist):
                    for letter in word:
                        letra = letter.lower()
                        if (letra not in " \n") and (letra not in tentadas) and (letra not in wordstatuslist):
                            letraslist.append(letra)
        else:
            for word in flist:
                if len(word) == len(wordstatuslist):
                    for letter in word:
                        letra = letter.lower()
                        if (letra not in " \n") and (letra not in tentadas) and (letra not in wordstatuslist):
                            letraslist.append(letra)
                        else:
                            continue
    count = Counter(letraslist)
    chute = max(letraslist, key=count.get)
    return chute
def demointel():
    playerdemo = "Sicrano"
    nivel = "Difícil"  ## Se der tempo... Ir buscar o nivel fora e incluir como parametro?
    numerros = 6
    pontos = 0
    t = 0
    a = 0
    e = 0

    vogais = ["a", "e", "i", "o", "u"]
    consoantes1 = ["b", "c", "d", "f", "g", "h", "j", "l", "m", "n",
                   "p", "q", "r", "s", "t", "v"]
    consoantes2 = ["k", "w", "x", "y", "z"]

    tentadas = []
    wordstatuslist = []

    tema = getrandomtema()  # Buscar o tema aleatoriamente...
    word = getrandomword(tema)  # Escolher palavras aleatoriamente de acordo com o tema...
    palavra = transformword(word)  # Transformar em minuscula, sem acento...

    # Ajuste variáveis de verificação (wordstatuslist - lista) e de visualização (wordstatus - str)
    for i in range(len(word)):
        wordstatuslist.extend("_")
    wordstatus = "".join(wordstatuslist)

    # Preparação para o início do jogo:
    print("\nTema: {}. \n"  # Imprimir o tema da palavra antes da primeira tentativa (Regra 7)
          "Nível: {}. \n"
          "Atenção: A palavra tem {} letras. Você pode errar até {} vezes."
          .format(tema, nivel, len(palavra), numerros - 1))
    time.sleep(2)
    placardemo(playerdemo, wordstatus, t, a, e)
    time.sleep(2)

    # Loop do jogo em si (dentro do loop de configuração de um novo jogo):
    while a < len(palavra) and e < numerros:
        letra = chuteinteligente(tema, wordstatuslist, tentadas)  # Função: verificacao letra  # input inteligente do computador
        print("{}ª tentativa: {}".format(t + 1, letra))
        time.sleep(1)
        while letra in tentadas:
            letra = chuteinteligente(tema, wordstatuslist, tentadas)
            print("Já digitou essa letra. Tente outra: {}".format(letra))
            time.sleep(1)
        t += 1
        tentadas.extend(letra)
        if letra not in palavra:
            print("Não acertou...")
            time.sleep(1)
            e += 1
        elif letra in palavra:
            for i in range(len(palavra)):
                if letra == palavra[i]:
                    pontos += 1
                    a += 1
                    print("Acertou a letra " + word[i] + "!")
                    wordstatuslist[i] = word[i]
                    wordstatus = "".join(wordstatuslist)
                    time.sleep(1)
                else:
                    continue
        placardemo(playerdemo, wordstatus, t, a, e)  # Visualização do placar
        time.sleep(1)
    # Ao sair do loop: Verificação do motivo para o final do jogo: Acertou a palavra / Enforcado
    if a == len(palavra):
        print("Parabéns!! Você descobriu a palavra e foi salvo da Forca!!")
        pontos += 10
    elif e == numerros:
        print("Que pena! Você foi enforcado antes de descobrir a palavra... \n"
              "A palavra era: {}.\n".format(word))
        pontos = pontos - 10
    print("\n{} pontos adicionados.\n".format(pontos))
    time.sleep(3)

  ## Modo de Jogo - Player 1 vs PC:
    ### Placar - Player 1 vs PC: Tirar o nivel...
def placarupdate(player1, wordstatus, t, a, e):
    e0 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |           " + "                         \n" + \
         "            |           " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e1 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |           " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e2 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /       " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e3 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   / \     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e4 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |           " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e5 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |   /       " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    e6 = "Status: \n" + \
         " " * round(15 - (len(player1) / 2)) + f"{player1}" + "\n" + \
         "            ______      " + f"{wordstatus}" + "       \n" + \
         "            |    |      " + "                         \n" + \
         "            |    O      " + "                         \n" + \
         "            |   /|\     " + "Tentativas:" + f"{t}" + "\n" + \
         "            |   / \     " + "Acertos:" + f"{a}" + "   \n" + \
         "           /|\          " + "Erros:" + f"{e}" + "     \n"
    status = [e0, e1, e2, e3, e4, e5, e6]
    return print(status[e])
    ### Mecânica do Jogo 1 vs PC: Ainda falta atualizar: Integração BaseDados / tirar o nivel...
def jogo1x0(player1):
    # Loop para configuração de um novo jogo:
    while True:
        # Reset das variáveis por ocasião de um novo jogo:
        nivel = "Difícil"  ## Se der tempo... Ir buscar o nivel fora e incluir como parametro?
        numerros = 6
        pontos = 0
        t = 0
        a = 0
        e = 0
        tentadas = []
        wordstatuslist = []

        tema = escolhatema()  # Buscar o tema da palavra escolhida (Regra 7)...
        word = getrandomword(tema)  # Escolher palavras aleatoriamente de acordo com o tema...
        palavra = transformword(word)  # Transformar em minuscula, sem acento...

        # Ajuste variáveis de verificação (wordstatuslist - lista) e de visualização (wordstatus - str)
        for i in range(len(word)):
            wordstatuslist.extend("_")
        wordstatus = "".join(wordstatuslist)

        # Preparação para o início do jogo:
        print("\nTema: {}. \n"  # Imprimir o tema da palavra antes da primeira tentativa (Regra 7)
              "Nível: {}. \n"
              "Atenção: A palavra tem {} letras. Você pode errar até {} vezes."
              .format(tema, nivel, len(palavra), numerros - 1))
        placarupdate(player1, wordstatus, t, a, e)

        # Loop do jogo em si (dentro do loop de configuração de um novo jogo):
        while a < len(palavra) and e < numerros:
            letter = input("{}ª tentativa: ".format(t + 1))
            letra = verifyletter(letter)  # Função: verificacao letra
            while letra in tentadas:
                letra = verifyletter(input("Já digitou essa letra. Tente outra: "))
            t += 1
            tentadas.extend(letra)
            if letra not in palavra:
                print("Não acertou...")
                e += 1
            elif letra in palavra:
                for i in range(len(palavra)):
                    if letra == palavra[i]:
                        pontos += 1
                        a += 1
                        print("Acertou a letra " + word[i] + "!")
                        wordstatuslist[i] = word[i]
                        wordstatus = "".join(wordstatuslist)
                    else:
                        continue
            placarupdate(player1, wordstatus, t, a, e)  # Visualização do placar
        # Ao sair do loop: Verificação do motivo para o final do jogo: Acertou a palavra / Enforcado
        if a == len(palavra):
            print("Parabéns!! Você descobriu a palavra e foi salvo da Forca!!")
            pontos += 10
        elif e == numerros:
            print("Que pena! Você foi enforcado antes de descobrir a palavra... \n"
                  "A palavra era: {}.\n".format(word))
            pontos = pontos - 10
        #Gravar os pontos no arquivo nomespontos.txt
        writepoints(player1, pontos)

        # Verificar opção para jogar novamente: Reiniciar o loop de configuração ou (interromper e voltar ao Menu Principal)
        opc1 = input("Deseja jogar novamente? \n"
                     "('S' para sim, 'N' para não.)")
        while opc1 not in ["S", "s", "N", "n"]:
            opc1 = input("Desculpe, não entendi. Caso deseje jogar novamente, digite 'S'."
                         " Caso deseje retornar ao Menu Principal, digite 'N'\n")
        if opc1 in "Nn":
            break
        else:
            continue
  ## Modo de Jogo - Player 1 vs Player 2:
    ### Placar - Player 1 vs Player 2:
def placarupdate2(player1, player2, wordstatus1, wordstatus2, t1, a1, e1, t2, a2, e2):
    e10 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |           " + (" " * 15) + "\n" + \
          "      |           " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |           " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e11 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |           " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |           " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e12 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |   /       " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |           " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e13 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |   / \     " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |           " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e14 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |   /|\     " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |           " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e15 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |   /|\     " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |   /       " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e16 = "Status: \n" + \
          "                  " + f"{player1}" + (" " * (15 - len(player1))) + "\n" + \
          "      ______      " + (" " * 15) + "\n" + \
          "      |    |      " + f"{wordstatus1}" + (" " * (15 - (len(wordstatus1)))) + "\n" + \
          "      |    O      " + (" " * 15) + "\n" + \
          "      |   /|\     " + "Tentativas: " + f"{t1}" + "  \n" + \
          "      |   / \     " + "Acertos: " + f"{a1}" + "     \n" + \
          "     /|\          " + "Erros: " + f"{e1}" + "       \n"

    e20 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "           | \n" + \
          "  Tentativas: " + f"{t2}" + "           |  \n" + \
          "     Acertos: " + f"{a2}" + "           |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e21 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "           |  \n" + \
          "     Acertos: " + f"{a2}" + "           |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e22 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "     /     |  \n" + \
          "     Acertos: " + f"{a2}" + "           |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e23 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "     / \   |  \n" + \
          "     Acertos: " + f"{a2}" + "           |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e24 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "     /|\   |  \n" + \
          "     Acertos: " + f"{a2}" + "           |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e25 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "     /|\   |  \n" + \
          "     Acertos: " + f"{a2}" + "     /     |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    e26 = "\n" + \
          (" " * (15 - len(player2))) + f"{player2}" + "             \n" + \
          (" " * 15) + "      ______ \n" + \
          (" " * (15 - (len(wordstatus2)))) + f"{wordstatus2}" + "      |    | \n" + \
          (" " * 15) + "      O    | \n" + \
          "  Tentativas: " + f"{t2}" + "     /|\   |  \n" + \
          "     Acertos: " + f"{a2}" + "     / \   |  \n" + \
          "       Erros: " + f"{e2}" + "          /|\ \n"

    status1 = [e10, e11, e12, e13, e14, e15, e16]
    status2 = [e20, e21, e22, e23, e24, e25, e26]
    status = [status1[e1], status2[e2]]
    printlist = [0, 1]
    linhas = [status[i].splitlines() for i in printlist]
    for l in zip(*linhas):
        print(*l, sep='         ')
    ### Mecânica do Jogo 1 vs PC: Ainda falta atualizar: Integração BaseDados /
def jogo1x1(player1, player2):
    while True:
        tema = tema1x1() # Definição do tema para a partida

        word1 = verifyword(input("\nPrimeiro, {} vai escolher uma palavra para {} tentar acertar!\n"
                      "{}, feche os olhos enquanto {} digita a palavra: ".format(player2, player1, player1, player2)))  # Player 2 escolhe a palavra1 para o player 1 acertar...
        palavra1 = transformword(word1) # Transformar

        word2 = verifyword(input("\nAgora, {} vai escolher uma palavra para {} tentar acertar!\n"
                      "{}, feche os olhos enquanto {} digita a palavra: ".format(player1, player2, player2, player1)))  # Player 1 escolhe a palavra2 para o player 2 acertar...  Escolher palavras aleatoriamente de categorias mais dificeis...
        palavra2 = transformword(word2) # mesmo do anterior

        pontos1 = 0
        t1 = 0
        a1 = 0
        e1 = 0
        tentadas1 = []
        wordstatuslist1 = []

        pontos2 = 0
        t2 = 0
        a2 = 0
        e2 = 0
        tentadas2 = []
        wordstatuslist2 = []

        print("\nTema: {}. \n"  # Imprimir o tema da palavra antes da primeira tentativa...
              "Nível: {}. \n"
              "{}, a palavra escolhida por {} tem {} letras. Você pode errar até {} vezes.\n"
              "{}, a palavra escolhida por {} tem {} letras. Você pode errar até {} vezes."
              .format(tema, nivel, player1, player2, len(palavra1), numerros - 1,
                      player2, player1, len(palavra2), numerros - 1))

        for i in range(len(word1)):
            wordstatuslist1.extend("_")
        wordstatus1 = "".join(wordstatuslist1)

        for i in range(len(word2)):
            wordstatuslist2.extend("_")
        wordstatus2 = "".join(wordstatuslist2)

        placarupdate2(player1, player2, wordstatus1, wordstatus2, t1, a1, e1, t2, a2, e2)

        while a1 < len(palavra1) and a2 < len(palavra2) and e1 < numerros and e2 < numerros:
            letter1 = input("\n{}ª tentativa para {}: ".format(t1+1, player1))
            letra1 = verifyletter(letter1)  # Função: verificacao letra
            while letra1 in tentadas1:
                letra1 = verifyletter(input("Já digitou essa letra. Tente outra: "))
            t1 += 1
            tentadas1.extend(letra1)
            if letra1 not in palavra1:
                print("Não acertou...")
                e1 += 1
            elif letra1 in palavra1:
                for i in range(len(palavra1)):
                    if letra1 == palavra1[i]:
                        pontos1 += 1
                        a1 += 1
                        print("Acertou a letra " + word1[i] + "!")
                        wordstatuslist1[i] = word1[i]
                        wordstatus1 = "".join(wordstatuslist1)
                    else:
                        continue
            placarupdate2(player1, player2, wordstatus1, wordstatus2, t1, a1, e1, t2, a2, e2)
            if a1 == len(palavra1):
                print("Parabéns {}!! Você descobriu a palavra e salvou-se da Forca!!".format(player1))
                pontos1 += 10
            elif e1 == numerros:
                print("Que pena! Você foi enforcado antes de descobrir a palavra... \n"
                      "A palavra era: {}.\n".format(word1))
                pontos1 = pontos1 - 10

            letter2 = input("\n{}ª tentativa para {}: ".format(t2 + 1, player2))
            letra2 = verifyletter(letter2)  # Função: verificacao letra
            while letra2 in tentadas2:
                letra2 = verifyletter(input("Já digitou essa letra. Tente outra: "))
            t2 += 1
            tentadas2.extend(letra2)
            if letra2 not in palavra2:
                print("Não acertou...")
                e2 += 1
            elif letra2 in palavra2:
                for i in range(len(palavra2)):
                    if letra2 == palavra2[i]:
                        pontos2 += 1
                        a2 += 1
                        print("Acertou a letra " + word2[i] + "!")
                        wordstatuslist2[i] = word2[i]
                        wordstatus2 = "".join(wordstatuslist2)
                    else:
                        continue
            placarupdate2(player1, player2, wordstatus1, wordstatus2, t1, a1, e1, t2, a2, e2)
            if a2 == len(palavra2):
                print("Parabéns {}!! Você descobriu a palavra e salvou-se da Forca!!".format(player2))
                pontos2 += 10
            elif e2 == numerros:
                print("Que pena! Você foi enforcado antes de descobrir a palavra... \n"
                      "A palavra era: {}.\n".format(word2))
                pontos2 = pontos2 - 10

        if a1 == len(palavra1) and a2 == len(palavra2):
            print("Grande disputa! Os dois acertaram com o mesmo número de tentativas!")
        elif e1 == numerros and e2 == numerros:
            print("Jogo duro... Os dois foram enforcados com o mesmo número de tentativas...")
        elif a1 == len(palavra1) and a2 < len(palavra2):
            print("Uma salva de palmas para {}! Descobriu a palavra e salvou-se da Forca primeiro! ".format(player1))
        elif a2 == len(palavra2) and a1 < len(palavra1):
            print("Uma salva de palmas para {}! Descobriu a palavra e salvou-se da Forca primeiro!".format(player2))

        writepoints(player1, pontos1)
        writepoints(player2, pontos2)

        opc1 = input("Desejam jogar novamente? \n"
                     "('S' para sim, 'N' para não.)")
        while opc1 not in ["S", "s", "N", "n"]:
            opc1 = input("Desculpe, não entendi. Caso desejem jogar novamente, digite 'S'."
                         " Caso desejem retornar ao Menu Principal, digite 'N'\n")
        if opc1 in "Nn":
            break
        else:
            continue
  ## Registro dos nomes e pontuações (Regra 6.1):
def rankpoints(playername):
    df = pd.read_csv("nomespontos.txt", sep=",", header=None)
    df.columns = ["Nome", "Pontos"]
    df["Posição"] = df["Pontos"].rank(method="min", ascending=False)
    df["Posição"] = df["Posição"].astype(int)
    rankeddf = df.sort_values("Posição")
    rankeddf = rankeddf.reindex(columns=["Posição", "Nome", "Pontos"])
    top10 = rankeddf.head(10)
    playerposition = rankeddf.loc[df["Nome"] == playername]
    print("\nSua pontuação: \n\n", playerposition)
    x = input("\n--------------- <Enter> ----------------")
    print("\nMaiores pontuações: \n\n", top10)
    x = input("\n--------------- <Enter> ----------------")
  ## Menu Configurações:
def menuconfig():
    print('\nConfigurações: \n'
          '1. Edição de Temas\n'
          '2. Edição de Palavras\n'
          '3. Retornar ao Menu Principal\n')
    opcc = input("Digite o número correspondente a opção desejada: ")
    while opcc not in ["1", "2", "3"]:
        opcc = input("Desculpe, não entendi. Digite apenas o número que corresponde a opção desejada: ")
    return opcc

  ### Editor de Temas (Regra 8):
def edittemas():
    while True:
        opct = int(input("\nEdição de Temas:\n"
                         "1. Ver os temas existentes;\n"
                         "2. Acrescentar um novo tema;\n"
                         "3. Editar um tema existente; \n"
                         "4. Apagar um tema existente;\n"
                         "5. Retornar às configurações;\n"
                         "Digite o número da opção desejada: "))
        if opct == 5:
            break
        listatemas = []
        listaescolhas = [0, ]
        for file in os.listdir("Temas/"):
            splited = file.split(".")
            listatemas.append(splited[0])
        if opct == 1:
            print("Temas existentes:")
            for i in range(len(listatemas)):
                listaescolhas.append(i + 1)
                print("{}. {};".format(i + 1, listatemas[i]))
            espera = input("\n------------------ <Enter> ------------------\n")
        elif opct == 2:  #Criar novo arquivo
            while True:
                novotema = input("Digite o nome do tema: ")
                while novotema in listatemas:
                    novotema = input("O tema {} já existe. Digite outro tema: ".format(novotema))
                confirmacao = input("Confirma a criação do tema {}?\n"
                                    "(\"S\" ou \"N\")".format(novotema))
                while confirmacao not in ["S", "s", "N", "n"]:
                    confirmacao = input(
                        "Desculpe, não entendi.\n"
                        "Digite \"S\" caso deseje acrescentar o tema {} ou "
                        "\"N\" para reescrever o nome do tema".format(novotema))
                if confirmacao in ["S", "s"]:
                    f = open(f"Temas/{novotema}.txt", "w", encoding="utf-8")
                    f.close()
                    print("O tema {} foi acrescentado com sucesso!\n"
                          "Lembre de acrescentar palavras para este tema!".format(novotema))
                    break
                else:
                    break
        elif opct == 3:   # Editar                     # Continuar daqui...
            while True:
                print("Temas existentes:")
                for i in range(len(listatemas)):
                    listaescolhas.append(i + 1)
                    print("{}. {};".format(i + 1, listatemas[i]))
                escolhatemaedit = int(input("digite o número do tema escolhido: "))
                while escolhatemaedit not in listaescolhas:
                    escolhatemaedit = int(input("Desculpe, não entendi. Digite apenas o número referente ao tema escolhido: "))
                temaedit = listatemas[escolhatemaedit-1]
                confirmacao = input("Confirma a edição do tema {}?\n"
                                    "(\"S\" ou \"N\")".format(temaedit))
                while confirmacao not in ["S", "s", "N", "n"]:
                    confirmacao = input(
                        "Desculpe, não entendi.\n"
                        "Digite \"S\" caso deseje editar o tema {} ou "
                        "\"N\" para reescrever o nome do tema".format(temaedit))
                if confirmacao in ["S", "s"]:
                    novotemaedit = input("Digite o novo nome para o tema: ")
                    while novotemaedit in listatemas:
                        novotemaedit = input("O tema {} já existe. Digite outro tema: ".format(novotemaedit))
                    confirmacao = input("Confirma a substituição do tema {} por {}?\n"
                                        "(\"S\" ou \"N\")".format(temaedit, novotemaedit))
                    while confirmacao not in ["S", "s", "N", "n"]:
                        confirmacao = input(
                            "Desculpe, não entendi.\n"
                            "Digite \"S\" caso deseje substituir o tema {} por {} ou "
                            "\"N\" para cancelar".format(temaedit, novotemaedit))
                    if confirmacao in ["S", "s"]:
                        oldname = r"Temas/{}.txt".format(temaedit)
                        newname = r"Temas/{}.txt".format(novotemaedit)
                        os.rename(oldname, newname)
                        print("O tema {} foi alterado por {} com sucesso!".format(temaedit, novotemaedit))
                        break
                    else:
                        break
        elif opct == 4:  # Apagar
            print("Temas existentes:")
            for i in range(len(listatemas)):
                listaescolhas.append(i + 1)
                print("{}. {};".format(i + 1, listatemas[i]))
            escolhatemadel = int(input("digite o número do tema escolhido: "))
            while escolhatemadel not in listaescolhas:
                escolhatemadel = int(input("Desculpe, não entendi. Digite apenas o número referente ao tema escolhido: "))
            temadel = listatemas[escolhatemadel - 1]
            confirmacao = input("Confirma que deseja apagar o tema {}?\n"
                                "Todas as palavras deste tema serão eliminadas\n"
                                "(\"S\" ou \"N\")".format(temadel))
            while confirmacao not in ["S", "s", "N", "n"]:
                confirmacao = input(
                    "Desculpe, não entendi.\n"
                    "Digite \"S\" caso deseje apagar o tema {} ou "
                    "\"N\" para cancelar".format(temadel))
            if confirmacao in ["S", "s"]:
                listatemas.remove("{}".format(temadel))
                if os.path.exists("Temas/{}.txt".format(temadel)):
                    os.remove("Temas/{}.txt".format(temadel))
                    print("O arquivo {}.txt foi deletado com sucesso!".format(temadel))
                else:
                    print("Erro: Arquivo não encontrado...")
   ### Configurações - Editor de Palavras (Regra 8):
def editwords(tema):
    while True:
        opcp = int(input("\nEdição de Palavras no tema {}:\n"
                         "1. Ver as palavras do tema;\n"
                         "2. Acrescentar uma nova palavra;\n"
                         "3. Apagar uma palavra existente;\n"
                         "4. Retornar às configurações;\n"
                         "Digite o número da opção desejada: ".format(tema)))
        if opcp == 4:
            break
        with open(f"Temas/{tema}.txt", "r", encoding="utf-8") as words:
            listawords = []
            listaescolhas = [0, ]
            for line in words:
                listawords.append(line.strip())
        if opcp == 1:
            print("Palavras existentes:")
            for i in range(len(listawords)):
                listaescolhas.append(i + 1)
                print("{}. {};".format(i + 1, listawords[i]))
            espera = input("\n------------------ <Enter> ------------------\n")
        elif opcp == 2:  #Criação
            while True:
                novaword = input("Digite o nome da palavra: ")
                while novaword in listawords:
                    novaword = input("A palavra {} já existe. Digite outra Palavra: ".format(novaword))
                confirmacao = input("Confirma a criação da palavra {}?\n"
                                    "(\"S\" ou \"N\")".format(novaword))
                while confirmacao not in ["S", "s", "N", "n"]:
                    confirmacao = input(
                        "Desculpe, não entendi.\n"
                        "Digite \"S\" caso deseje acrescentar a palavra {} ou "
                        "\"N\" para reescrever a palavra".format(novaword))
                if confirmacao in ["S", "s"]:
                    listawords.append(novaword)
                    listawords.sort()
                    with open(f"Temas/{tema}.txt", "w", encoding="utf-8") as words:
                        for item in listawords:
                            words.writelines(item + "\n")
                    print("A palavra {} foi acrescentada com sucesso!".format(novaword))
                    break
                else:
                    break
        elif opcp == 3:   # Apagar
            print("Palavras existentes:")
            for i in range(len(listawords)):
                listaescolhas.append(i + 1)
                print("{}. {};".format(i + 1, listawords[i]))
            escolhaworddel = int(input("digite o número da palavra escolhida: "))
            while escolhaworddel not in listaescolhas:
                escolhaworddel = int(input("Desculpe, não entendi. Digite apenas o número referente a palavra escolhida: "))
            worddel = listawords[escolhaworddel - 1]
            confirmacao = input("Confirma que deseja apagar a palavra {}?\n"
                                "(\"S\" ou \"N\")".format(worddel))
            while confirmacao not in ["S", "s", "N", "n"]:
                confirmacao = input(
                    "Desculpe, não entendi.\n"
                    "Digite \"S\" caso deseje apagar a palavra {} ou "
                    "\"N\" para cancelar".format(worddel))
            if confirmacao in ["S", "s"]:
                listawords.remove("{}".format(worddel))
                with open(f"Temas/{tema}.txt", "w", encoding="utf-8") as words:
                    for item in listawords:
                        words.writelines(item + "\n")
                print("Palavra {} foi deletada com sucesso!".format(worddel))



# Entrada do Programa:
print("\nUPskill - Datawarehouse and Business Intelligence\n"
      "Módulo 1 - Introdução a Programação\n"
      "Jogo da Forca\n"  # Deixar maior?
      "Versão Teste (Última atualização em 12/06/2022)\n"
      "Desenvolvido por Dante Chung.\n")

# Login (Regra 6):
print("\nPrimeiro, façamos o login.")
player1 = login()

# Loop Geral do Programa:
while opc !=6:
    opc = int(menuprincipal()) #Regra 1 (Menu)
    if opc == 6:
        break
    elif opc == 1:
        opcd = int(menudemos())  # Explicação das Regras (Pontuação - Regra 2)
        if opcd == 1:
            demo1()
        elif opcd == 2:
            demoaleat()
        elif opcd == 3:
            demointel()
        else:
            continue
    elif opc == 2:
        jogo1x0(player1)
    elif opc == 3:
        player2 = login2()
        jogo1x1(player1, player2)
    elif opc == 4:
        rankpoints(player1)
    elif opc == 5:
        while True:
            opcc = int(menuconfig())
            if opcc == 1:
                edittemas()
            elif opcc == 2:
                tema = escolhatema()
                editwords(tema)
            else:
                break
    else:
        print("Erro desconhecido?")

# Mensagem Final:
print("\nObrigado por jogar conosco! \n"
      "Lembre-se de usar o mesmo nome da próxima vez! Sua pontuação ficará gravada.\n"
      "Até a próxima!")
