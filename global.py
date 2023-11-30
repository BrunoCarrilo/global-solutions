def menu_principal():
    while True:
        print('======= DesfibrilaDrone =======')
        print(' [1] Menu Usuário')
        print(' [2] Menu Administrador')
        print(' [0] Sair do Programa')
        print('===============================')

        op = input(' Digite uma opção: ')

        if op == '1':
            menu_usuario()
        elif op == '2':
            menu_administrador()
        elif op == '0':
            print(' Encerrando o programa...')
            break
        else:
            print(' Opção inválida, digite novamente.\n')


def menu_usuario():
    while True:
        print('\n>>>>> MENU USUÁRIO <<<<<')
        print(' [1] O que é DesfibrilaDrone')
        print(' [2] Missão e Objetivos')
        print(' [3] Funcionalidades Principais')
        print(' [4] Como Funciona')
        print(' [5] Benefícios')
        print(' [0] Voltar ao menu principal')
        print('------------------------------')

        op = input(' Digite uma opção: ')

        if op == '1':
            print('\n>>>>> O que é DesfibrilaDrone? <<<<<')
            print('Bem-vindo ao DesfibrilaDrone, um projeto revolucionário que redefine a abordagem no atendimento a '
                  '\nemergências cardíacas. Este drone inteligente, equipado com tecnologia de ponta, foi'
                  '\nmeticulosamente projetado para agir rapidamente em situações críticas, onde cada segundo é '
                  '\nvital. Acreditamos que a vida é preciosa, e a rapidez na resposta a emergências pode ser a '
                  '\ndiferença entre a vida e a perda irreparável. ')

        elif op == '2':
            print('\n>>>>> Missão e Objetivos <<<<<')
            print('O DesfibrilaDrone surge como resposta à necessidade urgente de reduzir o tempo de atendimento em '
                  '\nsituações críticas de parada cardiorrespiratória. Nosso objetivo é proporcionar uma intervenção '
                  '\nrápida e eficaz, aumentando significativamente as chances de sobrevivência para aqueles que '
                  '\nnecessitam de assistência imediata.')

        elif op == '3':
            print('\n>>>>> Funcionalidades Principais <<<<<')
            print('O DesfibrilaDrone é um drone inteligente equipado com um Desfibrilador Externo Automático (DEA) e '
                  '\noutros dispositivos médicos essenciais. Controlado remotamente por médicos capacitados, '
                  '\neste dispositivo inovador é projetado para chegar rapidamente ao local da emergência, '
                  '\nindependentemente das barreiras físicas.')

        elif op == '4':
            print('\n>>>>> Como Funciona <<<<<')
            print('Após ser registrado a ocorrência, o drone é acionado imediatamente ao local utilizando rotas'
                  '\notimizadas evitando obstáculos. A intervenção médica remota ocorre com médicos capacitados'
                  '\nassumindo o controle, avaliando a situação por transmissões de vídeo em tempo real. Equipado'
                  '\ncom um Desfibrilador Externo Automático (DEA), possibilita intervenções imediatas no local,'
                  '\ntornando-se crucial para situações críticas.')

        elif op == '5':
            print('\n>>>>> Benefícios <<<<<')
            print('1. Redução do Tempo de Resposta:')
            print('O DesfibrilaDrone encurta significativamente o tempo entre o alerta e a intervenção médica, '
                  '\ncrucial em casos de parada cardiorrespiratória.')

            print('\n2. Aumento das Taxas de Sobrevivência:')
            print('A intervenção precoce, combinada com a orientação remota de profissionais de saúde, '
                  '\naumenta substancialmente as chances de sobrevivência.')

            print('\n3. Integração com Serviços de Emergência:')
            print('Nosso projeto é desenvolvido em colaboração com serviços de emergência, integrando-se '
                  '\nperfeitamente aos protocolos existentes.')

            print('\n4. Acesso a Locais Remotos:')
            print('O DesfibrilaDrone supera barreiras geográficas, garantindo atendimento de emergência em áreas de '
                  '\ndifícil acesso.')

        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')


def menu_administrador():
    while True:
        print('\n>>>>> MENU ADMINISTRADOR <<<<<')
        print(' [1] Realizar Login')
        print(' [2] Esqueci a senha')
        print(' [0] Voltar ao menu anterior')
        print('-------------------------------')

        op = input(' Digite uma opção: ')

        if op == '1':
            realizar_login()
            break
        if op == '2':
            esqueci_a_senha()
            break
        elif op == '0':
            break
        else:
            print(' Opção inválida, digite novamente.')