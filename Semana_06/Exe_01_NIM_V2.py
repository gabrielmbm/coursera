def computador_escolhe_jogada(n, m):
    if m >= n:
        retiraPecas = n
        #print(retiraPecas)
        return retiraPecas
    else:
        retiraPecas = m
        multiplo = m + 1
        sobraPecas = n - m
        sobraMult = sobraPecas % multiplo
        if sobraMult == 0:
            #print(retiraPecas)
            return retiraPecas
        else:
            passComp = True
            while sobraMult != 0 or passComp == True:
                retiraPecas -= 1
                sobraPecas = n - retiraPecas
                sobraMult = sobraPecas % multiplo
                if retiraPecas == 0:
                    passComp = False
                    if m >= n:
                        retiraPecas = n
                    else:
                        retiraPecas = m
            #print(retiraPecas)
            return retiraPecas
    
def usuario_escolhe_jogada(n, m):
    retiraPecas = int(input('Quantas peças você vai tirar? '))
    if n <= m:
        if retiraPecas >= 1 and retiraPecas <= n:
            #print(retiraPecas)
            return retiraPecas
        else:
            while retiraPecas < 1 or retiraPecas > n:
                print('')
                print('Oops! Jogada inválida! Tente de novo.')
                print('')
                retiraPecas = int(input('Quantas peças você vai tirar? '))
            #print(retiraPecas)
            return retiraPecas
    else:
        if retiraPecas >= 1 and retiraPecas <= m:
            #print(retiraPecas)
            return retiraPecas
        else:
            while retiraPecas < 1 or retiraPecas > m:
                print('')
                print('Oops! Jogada inválida! Tente de novo.')
                print('')
                retiraPecas = int(input('Quantas peças você vai tirar? '))
            #print(retiraPecas)
            return retiraPecas

def teste():
    n = int(input('Digite N: '))
    m = int(input('Digite M: '))
    #computador_escolhe_jogada(n, m)
    #usuario_escolhe_jogada(n, m)

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print('')
    pecasRetira = 0
    computador = False

    if n % (m + 1) == 0:
        print('Você começa!')
        print('')

        while n != 0:
            pecasRetira = (usuario_escolhe_jogada(n, m))
            n -= pecasRetira
            print('Você tirou', pecasRetira, 'peças.')
            print('Agora restam', n, 'peças no tabuleiro.')
            print('')

            pecasRetira = (computador_escolhe_jogada(n, m))
            n -= pecasRetira
            if n == 0:
                print('O computador tirou', pecasRetira,'peças.')
                print('Fim do jogo! O computador ganhou!')
                computador = True
            else:
                print('O computador tirou', pecasRetira,'peças.')
                print('Agora restam', n, 'peças no tabuleiro.')
                print('')

    else:
        print('Computador começa!')
        print('')

        while n != 0:
            pecasRetira = (computador_escolhe_jogada(n, m))
            n -= pecasRetira
            if n == 0:
                print('O computador tirou', pecasRetira,'peças.')
                print('Fim do jogo! O computador ganhou!')
                #print('O computador ganhou!')
                computador = True
            else:
                print('O computador tirou', pecasRetira,'peças.')
                print('Agora restam', n, 'peças no tabuleiro.')
                print('')
            
            if computador == False:
                pecasRetira = (usuario_escolhe_jogada(n, m))
                n -= pecasRetira
                print('Você tirou', pecasRetira, 'peças.')
                print('Agora restam', n, 'peças no tabuleiro.')
                print('')
            #else:
                #print('Fim do jogo! O computador ganhou!')

def campeonato():
    i = 1

    while i <= 3:
        print('')
        print('**** Rodada', i, '****')
        print('')
        partida()
        i += 1
    
    print('')
    print('**** Final do campeonato! ****')
    print('')
    print('Placar: Você 0 X 3 Computador')

def main():
    print('')
    print('Bem-vindo ao jogo do NIM! Escolha:')
    print('')
    print('1 - para jogar uma partida isolada ')
    escolha = int(input('2 - para jogar um campeonato '))

    if escolha == 1:
        print('')
        print('Voce escolheu uma partida isolada!')
        print ('')
        partida()
    elif escolha == 2:
        print('')
        print('Voce escolheu um campeonato!')
        campeonato()

main()