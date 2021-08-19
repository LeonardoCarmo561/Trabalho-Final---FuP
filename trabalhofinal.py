import random as r

continuar_jogando = True
while (continuar_jogando):
    caractere_player = input("Deseja jogar com X ou O? ")

    # Verificando o caractere digitado é válido
    while (caractere_player != 'X') and (caractere_player != 'O'):
        print('Digite um caractere válido: "X" ou "O"')
        caractere_player = input("Deseja jogar com X ou O? ")

    if caractere_player == 'X':
        caractere_computer = "O"
    else:
        caractere_computer = 'X'

    # Criando o tabuleiro
    matriz = [ [[' '] * 3 for i in range(3)] * 3 for j in range(3) ]

    def imprimir_tabuleiro():
        print("  CAMADA  1       CAMADA  2       CAMADA  3")
        print("  1   2   3       1   2   3       1   2   3")
        print("1 %s | %s | %s 1   1 %s | %s | %s 1   1 %s | %s | %s 1" % (matriz[0][0][0], matriz[0][0][1], matriz[0][0][2], matriz[1][0][0], matriz[1][0][1], matriz[1][0][2], matriz[2][0][0],matriz[2][0][1], matriz[2][0][2]))
        print(" ---+---+---     ---+---+---     ---+---+---")
        print("2 %s | %s | %s 2   2 %s | %s | %s 2   2 %s | %s | %s 2" % (matriz[0][1][0], matriz[0][1][1], matriz[0][1][2], matriz[1][1][0], matriz[1][1][1], matriz[1][1][2], matriz[2][1][0],matriz[2][1][1], matriz[2][1][2]))
        print(" ---+---+---     ---+---+---     ---+---+---")
        print("3 %s | %s | %s 3   3 %s | %s | %s 3   3 %s | %s | %s 3" % (matriz[0][2][0], matriz[0][2][1], matriz[0][2][2], matriz[1][2][0], matriz[1][2][1], matriz[1][2][2], matriz[2][2][0],matriz[2][2][1], matriz[2][2][2]))
        print()

    def jogada_do_usuario():
        aceitavel = True
        while(aceitavel):
            print("Execute sua jogada: ")
            a, b, c = input().split(',')
            a = int(a.strip())
            b = int(b.strip())
            c = int(c.strip())

            # Verificando se é uma entrada válida
            if (a >= 1 and a <= 3) and (b >= 1 and b <= 3) and (c >= 1 and c <= 3):
                aceitavel = False
            else:
                print("Erro, tente novamente.")

            # Verificando se a casa escolhida está vazia
            if (matriz[a-1][b-1][c-1] != ' '):
                print("Esta casa encontra-se preenchida, tente de novo.") 
                aceitavel = True
        
        # Atribuindo ao tabuleiro a jogada do usuário
        matriz[a-1][b-1][c-1] = caractere_player
        print() 

        # Mostrando o tabuleiro
        print("Dentro da jogada do usuario")
        imprimir_tabuleiro()

    jogada_do_usuario()





    def condicao_2_diag():
        for i in range (0, 3):
            z = 0
            if matriz[i][z][z] == ' ':
                if matriz[i][z+1][z+1] == matriz[i][z+2][z+2] and matriz[i][z+1][z+1] != ' ':
                    matriz[i][z][z] = caractere_computer
                    return imprimir_tabuleiro();
            else:
                if matriz[i][z][z] == matriz[i][z+1][z+1] and matriz[i][z+2][z+2] == ' ':
                    matriz[i][z+2][z+2] = caractere_computer
                    return imprimir_tabuleiro();
                elif matriz[i][z][z] == matriz[i][z+2][z+2] and matriz[i][z+1][z+1] == ' ':
                    matriz[i][z+1][z+1] = caractere_computer
                    return imprimir_tabuleiro();


    #Função para olhar condição 2 entre as linhas e mesma tabela
    def condicao_2_lin():
        for i in range (0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][z][j] == ' ':
                    if matriz[i][z+1][j] == matriz[i][z+2][j] and matriz[i][z+1][j] != ' ':
                        matriz[i][z][j] = caractere_computer
                        return imprimir_tabuleiro();
                else:
                    if matriz[i][z][j] == matriz[i][z+1][j] and matriz[i][z+2][j] == ' ':
                        matriz[i][z+2][j] = caractere_computer
                        return imprimir_tabuleiro();
                    elif matriz[i][z][j] == matriz[i][z+2][j] and matriz[i][z+1][j] == ' ':
                        matriz[i][z+1][j] = caractere_computer
                        return imprimir_tabuleiro();
        condicao_2_diag()

    #Função para olhar a condição 2 entre colunas e na mesma tabela
    def condicao_2_col():
        for i in range (0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][j][z] == ' ':
                    if matriz[i][j][z+1] ==  matriz[i][j][z+2] and matriz[i][j][z+1] != ' ':
                        matriz[i][j][z] = caractere_computer
                        return imprimir_tabuleiro();
                else:
                    if matriz[i][j][z] == matriz[i][j][z+1] and matriz[i][j][z+2] == ' ':
                        matriz[i][j][z+2] = caractere_computer
                        return imprimir_tabuleiro();
                    elif matriz[i][j][z] == matriz[i][j][z+2] and matriz[i][j][z+1] == ' ':
                        matriz[i][j][z+1] = caractere_computer
                        return imprimir_tabuleiro();
                    
        condicao_2_lin()
















    # Primeira jogada do computador, verificando se a casa se encontra vazia
    aceitavel = True
    while (aceitavel):
        a = r.randint(0, 2)
        b = r.randint(0, 2)
        c = r.randint(0, 2)

        if (matriz[a][b][c] != ' '):
            aceitavel = True
        else:
            aceitavel = False
            matriz[a][b][c] = caractere_computer

    imprimir_tabuleiro()

    # Segunda jogada do usuário
    jogada_do_usuario()
    condicao_2_col()


    jogada_do_usuario()
    condicao_2_col()

    jogada_do_usuario()
    condicao_2_col()

    jogada_do_usuario()
    condicao_2_col()

    jogada_do_usuario()
    condicao_2_col()

    # Pergunta-se ao usuário se ele deseja continuar jogando
    cj = input("Deseja continuar jogando? (Digite S para sim e N para não): ")
    while cj != "N" and cj != "S":
        print("Erro, tente novamente.")
        cj = input("Deseja continuar jogando? (Digite S para sim e N para não): ")
    if cj == "N":
        continuar_jogando = False





#Função para olhar condição 2 entre as linhas e mesma tabela
