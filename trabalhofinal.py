import random as r
vit = 0
der = 0
emp = 0
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
    matriz = [ [[' ',' ',' ']for i in range(3)]for j in range(3) ]

    tem_vencedor = False

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
        return (vitoria_jogador(), imprimir_tabuleiro())

    # Condição de vitória do jogador

    def vit_jog_entb_diag():
        global tem_vencedor, vit
        if matriz[1][1][1] == caractere_player:
            if matriz[0][0][0] == caractere_player and matriz[2][2][2] == caractere_player:
                tem_vencedor = True
                vit += 1
                return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))

            elif matriz[0][0][2] == caractere_player and matriz[2][2][0] == caractere_player:
                tem_vencedor = True
                vit += 1
                return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))

            elif matriz[0][2][0] == caractere_player and matriz[2][0][2] == caractere_player:
                tem_vencedor = True
                vit += 1
                return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))

            elif matriz[0][2][2] == caractere_player and matriz[2][0][0] == caractere_player:
                tem_vencedor = True
                vit += 1
                return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))

    def vit_jog_entb_mc():
        z = 0
        global tem_vencedor, vit
        for i in range (0, 3):
            if matriz[z+1][z+1][i] == caractere_player:
                if matriz[z][z][i] == caractere_player and matriz[z+2][z+2][i] == caractere_player:
                    tem_vencedor = True
                    vit += 1
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                
                elif matriz[z+2][z][i] == caractere_player and matriz[z][z+2][i] == caractere_player:
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
              
        vit_jog_entb_diag()
    
    def vit_jog_entb_g():
        z = 0
        global tem_vencedor, vit
        for i in range (0, 3):
            if matriz[z+1][i][z+1] == caractere_player:
                if matriz[z][i][z] == caractere_player and matriz[z+2][i][z+2] == caractere_player:
                    tem_vencedor = True
                    vit += 1
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                
                elif matriz[z][i][z+2] == caractere_player and matriz[z+2][i][z] == caractere_player:
                    tem_vencedor = True
                    vit  += 1
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
            
        vit_jog_entb_mc()
    
    def vitoria_jogador_entb():
        global tem_vencedor, vit
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[z][i][j] == caractere_player:
                    if matriz[z+1][i][j] == caractere_player and matriz[z+2][i][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                
                elif matriz[z+1][i][j] == caractere_player:
                    if matriz[z][i][j] == caractere_player and matriz[z+2][i][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                
                elif matriz[z+2][i][j] == caractere_player:
                    if matriz[z][i][j] == caractere_player and matriz[z+1][i][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
        vit_jog_entb_g()
    
    def vitoria_jogador_diag():
        global tem_vencedor, vit
        for i in range(0, 3):
            z = 0
            if matriz[i][1][1] == caractere_player:
                if matriz[i][0][0] == caractere_player and matriz[i][2][2] == caractere_player:
                    tem_vencedor = True
                    vit += 1
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                
                if matriz[i][0][2] == caractere_player and matriz[i][2][0] == caractere_player:
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))

        vitoria_jogador_entb()
    
    def vitoria_jogador_lin():
        global tem_vencedor, vit
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][z][j] == caractere_player:
                    if matriz[i][z+1][j] == caractere_player and matriz[i][z+2][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                    
                elif matriz[i][z+1][j] == caractere_player:
                    if matriz[i][z][j] == caractere_player and matriz[i][z+2][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                    
                elif matriz[i][z+2][j] == caractere_player:
                    if matriz[i][z][j] == caractere_player and matriz[i][z+1][j] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
        vitoria_jogador_diag()
    
    def vitoria_jogador():
        global tem_vencedor, vit
        for i in range (0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][j][z] == caractere_player:
                    if matriz[i][j][z+1] == caractere_player and matriz[i][j][z+2] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                    
                elif matriz[i][j][z+1] == caractere_player:
                    if matriz[i][j][z] == caractere_player and matriz[i][j][z+2] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
                    
                elif matriz[i][j][z+2] == caractere_player:
                    if matriz[i][j][z] == caractere_player and matriz[i][j][z+1] == caractere_player:
                        tem_vencedor = True
                        vit += 1
                        return (imprimir_tabuleiro(), print('VOCÊ VENCEU'))
        vitoria_jogador_lin()

    # endd

    
    # Função para a quinta condição da jogada do computador
    def jogada_do_computador_cod_5():
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


    def jogada_do_computador_cod_4():
        casas_pode_jogar = [[[True, True, True]for i in range(3)]for j in range(3) ]
        
        # Verificando em quais casas pode-se jogar
        for i in range(0, 3):
            for j in range(0, 3):
                for k in range(0, 3):
                    if matriz[i][j][k] != ' ':
                        casas_pode_jogar[i][j][k] = False
                        # Para uma mesma camada
                        if j == 0:
                            casas_pode_jogar[i][j+1][k] = False
                            casas_pode_jogar[i][j+2][k] = False
                        elif j == 1:
                            casas_pode_jogar[i][j-1][k] = False
                            casas_pode_jogar[i][j+1][k] = False
                        else:
                            casas_pode_jogar[i][j-2][k] = False
                            casas_pode_jogar[i][j-1][k] = False
                        
                        if k == 0:
                            casas_pode_jogar[i][j][k+1] = False
                            casas_pode_jogar[i][j][k+2] = False

                            if j == k:
                                casas_pode_jogar[i][j+1][k+1] = False
                                casas_pode_jogar[i][j+2][k+2] = False


                        elif k == 1:
                            casas_pode_jogar[i][j][k-1] = False
                            casas_pode_jogar[i][j][k+1] = False

                            if j == k:
                                casas_pode_jogar[i][j-1][k-1] = False
                                casas_pode_jogar[i][j+1][k+1] = False


                                casas_pode_jogar[i][j-1][k+1] = False
                                casas_pode_jogar[i][j+1][k-1] = False

                        else:
                            casas_pode_jogar[i][j][k-2] = False
                            casas_pode_jogar[i][j][k-1] = False


                            if j == k:
                                casas_pode_jogar[i][j-2][k-2] = False
                                casas_pode_jogar[i][j-1][k-1] = False

                        # Entre camadas
                        if i == 0:
                            casas_pode_jogar[i+1][j][k] = False
                            casas_pode_jogar[i+2][j][k] = False

                            if j == 0:
                                casas_pode_jogar[i+1][j+1][k] = False
                                casas_pode_jogar[i+2][j+2][k] = False

                                if k == 0:
                                    casas_pode_jogar[i+1][j+1][k+1] = False
                                    casas_pode_jogar[i+2][j+2][k+2] = False
                                
                                elif k == 2:
                                    casas_pode_jogar[1][1][1] = False
                                    casas_pode_jogar[2][2][0] = False

                            elif j == 2:
                                casas_pode_jogar[i+1][j-1][k] = False
                                casas_pode_jogar[i+2][j-2][k] = False

                                if k == 0:
                                    casas_pode_jogar[1][1][1] = False
                                    casas_pode_jogar[2][0][2] = False

                                elif k == 2:
                                    casas_pode_jogar[1][1][1] = False
                                    casas_pode_jogar[2][0][0] = False
                        

                        elif i == 1:
                            casas_pode_jogar[i-1][j][k] = False
                            casas_pode_jogar[i+1][j][k] = False

                            if j == 1:
                                casas_pode_jogar[i-1][j+1][k] = False
                                casas_pode_jogar[i-1][j-1][k] = False

                                casas_pode_jogar[i+1][j+1][k] = False
                                casas_pode_jogar[i+1][j-1][k] = False

                                if k == 1:
                                    casas_pode_jogar[0][0][0] = False
                                    casas_pode_jogar[0][2][0] = False
                                    casas_pode_jogar[0][0][2] = False
                                    casas_pode_jogar[0][2][2] = False

                                    casas_pode_jogar[2][0][2] = False
                                    casas_pode_jogar[2][2][0] = False
                                    casas_pode_jogar[2][0][0] = False
                                    casas_pode_jogar[2][2][2] = False

                                    casas_pode_jogar[0][1][0] = False
                                    casas_pode_jogar[0][1][2] = False
                                    casas_pode_jogar[2][1][0] = False
                                    casas_pode_jogar[2][1][2] = False
                            
                        
                        else:
                            casas_pode_jogar[i-2][j][k] = False
                            casas_pode_jogar[i-1][j][k] = False

                            if j == 0:
                                casas_pode_jogar[i-1][j+1][k] = False
                                casas_pode_jogar[i-2][j+2][k] = False

                            elif j == 2:
                                casas_pode_jogar[i-1][j-1][k] = False
                                casas_pode_jogar[i-2][j-2][k] = False

                            
                        

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if casas_pode_jogar[i][j][k] == True:
                        matriz[i][j][k] = caractere_computer
                        return imprimir_tabuleiro()
        jogada_do_computador_cod_5()
  




























    #jogada do cmoputador opção 2
    def jog_maq_entb_diag():
        if matriz[1][1][1] == ' ':
            if matriz[0][0][0] == caractere_player and matriz[2][2][2] == caractere_player:
                matriz[1][1][1] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][0][2] == caractere_player and matriz[2][2][0] == caractere_player:
                matriz[1][1][1] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][2][0] == caractere_player and matriz[2][0][2] == caractere_player:
                matriz[1][1][1] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][2][2] == caractere_player and matriz[2][0][0] == caractere_player:
                matriz[1][1][1] = caractere_computer
                return imprimir_tabuleiro()
        elif matriz[1][1][1] == caractere_player:
            if matriz[0][0][0] == ' ' and matriz[2][2][2] == caractere_player:
                matriz[0][0][0] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][0][0] == caractere_player and matriz[2][2][2] == ' ':
                matriz[2][2][2] = caractere_computer
                return imprimir_tabuleiro()
            
            elif matriz[0][0][2] == ' ' and matriz[2][2][0] == caractere_player:
                matriz[0][0][2] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][0][2] == caractere_player and matriz[2][2][0] == ' ':
                matriz[2][2][0] = caractere_computer
                return imprimir_tabuleiro()
            
            elif matriz[0][2][0] == ' ' and matriz[2][0][2] == caractere_player:
                matriz[0][2][0] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][2][0] == caractere_player and matriz[2][0][2] == ' ':
                matriz[2][0][2] = caractere_computer
                return imprimir_tabuleiro()
            
            elif matriz[0][2][2] == ' ' and matriz[2][0][0] == caractere_player:
                matriz[0][2][2] = caractere_computer
                return imprimir_tabuleiro()
            elif matriz[0][2][2] == caractere_player and matriz[2][0][0] == ' ':
                matriz[2][0][0] = caractere_computer
                return imprimir_tabuleiro()

        jogada_do_computador_cod_4()
        
    
    def jog_maq_entb_mc():
        z = 0
        for i in range (0, 3):
            if matriz[z+1][z+1][i] == ' ':
                if matriz[z][z][i] == caractere_player and matriz[z+2][z+2][i] == caractere_player:
                    matriz[z+1][z+1][i] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z+2][z][i] == caractere_player and matriz[z][z+2][i] == caractere_player:
                    matriz[z+1][z+1][i] = caractere_computer
                    return imprimir_tabuleiro()
            elif matriz[z+1][z+1][i] == caractere_player:
                if matriz[z][z][i] == ' ' and matriz[z+2][z+2][i] == caractere_player:
                    matriz[z][z][i] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z+2][z+2][i] == ' ' and matriz[z][z][i] == caractere_player:
                    matriz[z+2][z+2][i] = caractere_computer
                    return imprimir_tabuleiro()
                
                elif matriz[z+2][z][i] == ' ' and matriz[z][z+2][i] == caractere_player:
                    matriz[z+2][z][i] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z][z+2][i] == ' ' and matriz[z+2][z][i] == caractere_player:
                    matriz[z][z+2][i] = caractere_computer
                    return imprimir_tabuleiro()
        jog_maq_entb_diag()
    
    
    def jog_maq_entb_g():
        z = 0
        for i in range (0, 3):
            if matriz[z+1][i][z+1] == ' ':
                if matriz[z][i][z] == caractere_player and matriz[z+2][i][z+2] == caractere_player:
                    matriz[z+1][i][z+1] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z][i][z+2] == caractere_player and matriz[z+2][i][z] == caractere_player:
                    matriz[z+1][i][z+1] = caractere_computer
                    return imprimir_tabuleiro()
            elif matriz[z+1][i][z+1] == caractere_player:
                if matriz[z][i][z] == ' ' and matriz[z+2][i][z+2] == caractere_player:
                    matriz[z][i][z] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z+2][i][z+2] == ' ' and matriz[z][i][z] == caractere_player:
                    matriz[z+2][i][z+2] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z][i][z+2] == ' ' and matriz[z+2][i][z] == caractere_player:
                    matriz[z][i][z+2] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[z+2][i][z] == ' ' and matriz[z][i][z+2] == caractere_player:
                    matriz[z+2][i][z] = caractere_computer
                    return imprimir_tabuleiro()
        jog_maq_entb_mc()
    
    def jogada_maquina_entb():
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[z][i][j] == ' ':
                    if matriz[z+1][i][j] == caractere_player and matriz[z+2][i][j] == caractere_player:
                        matriz[z][i][j] = caractere_computer
                        return imprimir_tabuleiro()
                elif matriz[z+1][i][j] == ' ':
                    if matriz[z][i][j] == caractere_player and matriz[z+2][i][j] == caractere_player:
                        matriz[z+1][i][j] = caractere_computer
                        return imprimir_tabuleiro()
                elif matriz[z+2][i][j] == ' ':
                    if matriz[z][i][j] == caractere_player and matriz[z+1][i][j] == caractere_player:
                        matriz[z+2][i][j] = caractere_computer
                        return imprimir_tabuleiro()
        jog_maq_entb_g()
    
    def jogada_maquina_diag():
        for i in range(0, 3):
            z = 0
            if matriz[i][1][1] == ' ':
                if matriz[i][0][0] == caractere_player and matriz[i][2][2] == caractere_player:
                    matriz[i][1][1] = caractere_computer
                    return imprimir_tabuleiro()
                if matriz[i][0][2] == caractere_player and matriz[i][2][0] == caractere_player:
                    matriz[i][1][1] = caractere_computer
                    return imprimir_tabuleiro()
            elif matriz[i][1][1] == caractere_player:
                if matriz[i][0][0] == caractere_player and matriz[i][2][2] == ' ':
                    matriz[i][2][2] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[i][2][2] == caractere_player and matriz[i][0][0] == ' ':
                    matriz[i][0][0] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[i][0][2] == caractere_player and matriz[i][2][0] == ' ':
                    matriz[i][2][0] = caractere_computer
                    return imprimir_tabuleiro()
                elif matriz[i][2][0] == caractere_player and matriz[i][0][2] == ' ':
                    matriz[i][0][2] = caractere_computer
                    return imprimir_tabuleiro()
        jogada_maquina_entb()
    
    def jogada_maquina_lin():
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][z][j] == ' ':
                    if matriz[i][z+1][j] == caractere_player and matriz[i][z+2][j] == caractere_player:
                        matriz[i][z][j] = caractere_computer
                        return imprimir_tabuleiro()
                elif matriz[i][z+1][j] == ' ':
                    if matriz[i][z][j] == caractere_player and matriz[i][z+2][j] == caractere_player:
                        matriz[i][z+1][j] = caractere_computer
                        return imprimir_tabuleiro()
                elif matriz[i][z+2][j] == ' ':
                    if matriz[i][z][j] == caractere_player and matriz[i][z+1][j] == caractere_player:
                        matriz[i][z+2][j] = caractere_computer
                        return imprimir_tabuleiro()
        jogada_maquina_diag()
    
    def jogada_maquina_2():
        for i in range (0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][j][z] == ' ':
                    if matriz[i][j][z+1] == caractere_player and matriz[i][j][z+2] == caractere_player:
                        matriz[i][j][z] = caractere_computer
                        return (imprimir_tabuleiro())
                elif matriz[i][j][z+1] == ' ':
                    if matriz[i][j][z] == caractere_player and matriz[i][j][z+2] == caractere_player:
                        matriz[i][j][z+1] = caractere_computer
                        return imprimir_tabuleiro()
                elif matriz[i][j][z+2] == ' ':
                    if matriz[i][j][z] == caractere_player and matriz[i][j][z+1] == caractere_player:
                        matriz[i][j][z+2] = caractere_computer
                        return imprimir_tabuleiro()
        jogada_maquina_lin()


    #jogada do computador opção 1
    def vit_maq_entb_diag():
        global tem_vencedor
        if matriz[1][1][1] == ' ':
            if matriz[0][0][0] == caractere_computer and matriz[2][2][2] == caractere_computer:
                matriz[1][1][1] = caractere_computer
                
                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][0][2] == caractere_computer and matriz[2][2][0] == caractere_computer:
                matriz[1][1][1] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][2][0] == caractere_computer and matriz[2][0][2] == caractere_computer:
                matriz[1][1][1] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][2][2] == caractere_computer and matriz[2][0][0] == caractere_computer:
                matriz[1][1][1] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        elif matriz[1][1][1] == caractere_computer:
            if matriz[0][0][0] == ' ' and matriz[2][2][2] == caractere_computer:
                matriz[0][0][0] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][0][0] == caractere_computer and matriz[2][2][2] == ' ':
                matriz[2][2][2] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            
            elif matriz[0][0][2] == ' ' and matriz[2][2][0] == caractere_computer:
                matriz[0][0][2] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][0][2] == caractere_computer and matriz[2][2][0] == ' ':
                matriz[2][2][0] = caractere_computer
    
                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            
            elif matriz[0][2][0] == ' ' and matriz[2][0][2] == caractere_computer:
                matriz[0][2][0] = caractere_computer
      
                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][2][0] == caractere_computer and matriz[2][0][2] == ' ':
                matriz[2][0][2] = caractere_computer
       
                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            
            elif matriz[0][2][2] == ' ' and matriz[2][0][0] == caractere_computer:
                matriz[0][2][2] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[0][2][2] == caractere_computer and matriz[2][0][0] == ' ':
                matriz[2][0][0] = caractere_computer

                tem_vencedor = True
                return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        jogada_maquina_2()
    
    def vit_maq_entb_mc():
        z = 0
        global tem_vencedor
        for i in range (0, 3):
            if matriz[z+1][z+1][i] == ' ':
                if matriz[z][z][i] == caractere_computer and matriz[z+2][z+2][i] == caractere_computer:
                    matriz[z+1][z+1][i] = caractere_computer
            
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+2][z][i] == caractere_computer and matriz[z][z+2][i] == caractere_computer:
                    matriz[z+1][z+1][i] = caractere_computer
                    
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[z+1][z+1][i] == caractere_computer:
                if matriz[z][z][i] == ' ' and matriz[z+2][z+2][i] == caractere_computer:
                    matriz[z][z][i] = caractere_computer
                    
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+2][z+2][i] == ' ' and matriz[z][z][i] == caractere_computer:
                    matriz[z+2][z+2][i] = caractere_computer
                   
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                
                elif matriz[z+2][z][i] == ' ' and matriz[z][z+2][i] == caractere_computer:
                    matriz[z+2][z][i] = caractere_computer
                  
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z][z+2][i] == ' ' and matriz[z+2][z][i] == caractere_computer:
                    matriz[z][z+2][i] = caractere_computer
                   
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))    
        vit_maq_entb_diag()
    
    def vit_maq_entb_g():
        z = 0
        global tem_vencedor
        for i in range (0, 3):
            if matriz[z+1][i][z+1] == ' ':
                if matriz[z][i][z] == caractere_computer and matriz[z+2][i][z+2] == caractere_computer:
                    matriz[z+1][i][z+1] = caractere_computer
                   
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z][i][z+2] == caractere_computer and matriz[z+2][i][z] == caractere_computer:
                    matriz[z+1][i][z+1] = caractere_computer
                    
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[z+1][i][z+1] == caractere_computer:
                if matriz[z][i][z] == ' ' and matriz[z+2][i][z+2] == caractere_computer:
                    matriz[z][i][z] = caractere_computer
                   
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+2][i][z+2] == ' ' and matriz[z][i][z] == caractere_computer:
                    matriz[z][i][z] = caractere_computer
                  
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z][i][z+2] == ' ' and matriz[z+2][i][z] == caractere_computer:
                    matriz[z][i][z+2] = caractere_computer
                
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+2][i][z] == ' ' and matriz[z][i][z+2] == caractere_computer:
                    matriz[z+2][i][z] = caractere_computer
              
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        vit_maq_entb_mc()
    
    def vitoria_maquina_entb():
        global tem_vencedor
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[z][i][j] == ' ':
                    if matriz[z+1][i][j] == caractere_computer and matriz[z+2][i][j] == caractere_computer:
                        matriz[z][i][j] = caractere_computer
                    
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+1][i][j] == ' ':
                    if matriz[z][i][j] == caractere_computer and matriz[z+2][i][j] == caractere_computer:
                        matriz[z+1][i][j] = caractere_computer
                        
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[z+2][i][j] == ' ':
                    if matriz[z][i][j] == caractere_computer and matriz[z+1][i][j] == caractere_computer:
                        matriz[z+2][i][j] = caractere_computer
                        
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        vit_maq_entb_g()
    
    def vitoria_maquina_diag():
        global tem_vencedor
        for i in range(0, 3):
            z = 0
            if matriz[i][1][1] == ' ':
                if matriz[i][0][0] == caractere_computer and matriz[i][2][2] == caractere_computer:
                    matriz[i][1][1] = caractere_computer
                 
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                if matriz[i][0][2] == caractere_computer and matriz[i][2][0] == caractere_computer:
                    matriz[i][1][1] = caractere_computer
                    
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
            elif matriz[i][1][1] == caractere_computer:
                if matriz[i][0][0] == caractere_computer and matriz[i][2][2] == ' ':
                    matriz[i][2][2] = caractere_computer
                   
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][2][2] == caractere_computer and matriz[i][0][0] == ' ':
                    matriz[i][0][0] = caractere_computer
                  
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][0][2] == caractere_computer and matriz[i][2][0] == ' ':
                    matriz[i][2][0] = caractere_computer
               
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][2][0] == caractere_computer and matriz[i][0][2] == ' ':
                    matriz[i][0][2] = caractere_computer
                 
                    tem_vencedor = True
                    return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        vitoria_maquina_entb()
    
    def vitoria_maquina_lin():
        global tem_vencedor
        for i in range(0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][z][j] == ' ':
                    if matriz[i][z+1][j] == caractere_computer and matriz[i][z+2][j] == caractere_computer:
                        matriz[i][z][j] = caractere_computer
                       
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][z+1][j] == ' ':
                    if matriz[i][z][j] == caractere_computer and matriz[i][z+2][j] == caractere_computer:
                        matriz[i][z+1][j] = caractere_computer
                    
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][z+2][j] == ' ':
                    if matriz[i][z][j] == caractere_computer and matriz[i][z+1][j] == caractere_computer:
                        matriz[i][z+2][j] = caractere_computer
                       
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        vitoria_maquina_diag()
    
    def jogada_maquina():
        global tem_vencedor
        for i in range (0, 3):
            for j in range (0, 3):
                z = 0
                if matriz[i][j][z] == ' ':
                    if matriz[i][j][z+1] == caractere_computer and matriz[i][j][z+2] == caractere_computer:
                        matriz[i][j][z] = caractere_computer
                   
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][j][z+1] == ' ':
                    if matriz[i][j][z] == caractere_computer and matriz[i][j][z+2] == caractere_computer:
                        matriz[i][j][z+1] = caractere_computer
                       
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
                elif matriz[i][j][z+2] == ' ':
                    if matriz[i][j][z] == caractere_computer and matriz[i][j][z+1] == caractere_computer:
                        matriz[i][j][z+2] = caractere_computer
                      
                        tem_vencedor = True
                        return (imprimir_tabuleiro(), print('VITÓRIA DO COMPUTADOR'))
        vitoria_maquina_lin()





    # Primeira jogada do usuário
    jogada_do_usuario()


    # Primeira jogada do computador
    jogada_maquina()
    '''
    # Segunda jogada do usuário
    jogada_do_usuario()

    # Segunda jogada do computador

    jogada_maquina()
    # jogada_maquina()
    '''
    while tem_vencedor == False:
        jogada_do_usuario()
        if tem_vencedor == True:
            break
        else:
            jogada_maquina()



    # Pergunta-se ao usuário se ele deseja continuar jogando
    cj = input("Deseja continuar jogando? (Digite S para sim e N para não): ")
    while cj != "N" and cj != "S":
        print("Erro, tente novamente.")
        cj = input("Deseja continuar jogando? (Digite S para sim e N para não): ")
    if cj == "N":
        continuar_jogando = False

