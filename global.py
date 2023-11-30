import json
from datetime import datetime


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


def carregar_dados_usuarios():
    with open('usuarios.json', 'r') as arquivo:
        dados_usuarios = json.load(arquivo)
    return dados_usuarios


def realizar_login():
    dados_usuarios = carregar_dados_usuarios()
    print('\n>>>>> Realizar o Login <<<<<')
    login = input(' Digite o login: ')
    senha = input(' Digite a senha: ')

    if login in dados_usuarios and senha == dados_usuarios[login]['senha']:
        print(' Login efetuado com sucesso!')
        menu_ocorrencia(login)

    else:
        print(' Usuário ou senha incorreta. Não foi possível efetuar o login.')

    return login


def esqueci_a_senha():
    dados_usuarios = carregar_dados_usuarios()
    print('\n>>>>> Esqueci a Senha <<<<<')

    email = input('Digite o e-mail associado ao seu login: ')

    for login, info_usuario in dados_usuarios.items():
        if info_usuario['email'].lower() == email.lower():
            nova_senha = input('Digite a nova senha: ')

            # Vai verificar se a senha é diferente da original
            if nova_senha == info_usuario['senha']:
                print('A nova senha não pode ser igual à senha atual. Tente novamente.')
                return

            dados_usuarios[login]['senha'] = nova_senha
            with open('usuarios.json', 'w') as arquivo:
                json.dump(dados_usuarios, arquivo, indent=2)
            print('Senha alterada com sucesso!')
            return

    print('E-mail não encontrado. Não foi possível alterar a senha.')


def menu_ocorrencia(login):
    while True:
        print('\n====== Menu de Ocorrências =====')
        print(' [1] Registrar Ocorrência')
        print(' [2] Alterar Ocorrência')
        print(' [3] Listar todas as Ocorrências')
        print(' [0] Sair do Programa')
        print('===============================')

        op = input(' Digite uma opção: ')

        if op == '1':
            registrar_ocorrencia(login)
        elif op == '2':
            alterar_ocorrencias()
        elif op == '3':
            listar_ocorrencias()
        elif op == '0':
            exit()
        else:
            print(' Opção inválida, digite novamente.\n')


def registrar_ocorrencia(login):
    print('\n>>>>> Realizar Ocorrência <<<<<')
    with open('ocorrencias.json', 'r') as arquivo_ocorrencias:
        ocorrencias = json.load(arquivo_ocorrencias)

    nova_ocorrencia = {'tipoOcorrencia': input(' Digite o tipo da ocorrência: '),
                       'data': datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                       'local': input(' Digite o local da ocorrência: '), 'status': True,
                       'observacoes': input(' Digite as observações da ocorrência: '), 'login': login}

    ocorrencias.append(nova_ocorrencia)

    with open('ocorrencias.json', 'w', encoding='utf-8') as arquivo_ocorrencias:
        json.dump(ocorrencias, arquivo_ocorrencias, indent=2, ensure_ascii=False)

    print(' Ocorrência registrada com sucesso!')


def alterar_ocorrencias():
    print('\n>>>>> Alterar Ocorrência <<<<<')
    with open('ocorrencias.json', 'r', encoding='utf-8') as arquivo_ocorrencias:
        ocorrencias = json.load(arquivo_ocorrencias)

    if not ocorrencias:
        print(' Não há ocorrências para alterar.')
        return

    for i, ocorrencia in enumerate(ocorrencias):
        print(f"{i + 1}. Tipo: {ocorrencia['tipoOcorrencia']}, Data: {ocorrencia['data']},"
              f" Status: {'Aberta' if ocorrencia['status'] else 'Fechada'}")

    num_ocorrencia = input('Digite o número da ocorrência que deseja alterar (ou \'0\' para cancelar): ')

    if num_ocorrencia == '0':
        return

    try:
        num_ocorrencia = int(num_ocorrencia) - 1
        if 0 <= num_ocorrencia < len(ocorrencias):

            ocorrencia_selecionada = ocorrencias[num_ocorrencia]

            print(f'\nOcorrência Selecionada para Alteração:')
            print(f"Data: {ocorrencia_selecionada['data']}")
            print(f"Status: {'Aberta' if ocorrencia_selecionada['status'] else 'Fechada'}")
            print(f"Tipo: {ocorrencia_selecionada['tipoOcorrencia']}")
            print(f"Local: {ocorrencia_selecionada['local']}")
            print(f"Observações: {ocorrencia_selecionada['observacoes']}")
            print('----------------------------')

            # Solicita ao usuário qual dado deseja alterar
            op = input(' Digite o número correspondente ao dado que deseja alterar:'
                       '\n [1] Tipo da Ocorrência'
                       '\n [2] Local da Ocorrência'
                       '\n [3] Status da Ocorrência (Aberta/Fechada)'
                       '\n [4] Observações da Ocorrência'
                       '\n [0] Cancelar'
                       '\n Opção: ')

            if op == '1':
                ocorrencia_selecionada['tipoOcorrencia'] = input('Digite o novo tipo da ocorrência: ')
            elif op == '2':
                ocorrencia_selecionada['local'] = input('Digite o novo local da ocorrência: ')
            elif op == '3':
                ocorrencia_selecionada['status'] = not ocorrencia_selecionada['status']
            elif op == '4':
                ocorrencia_selecionada['observacoes'] = input('Digite as novas observações da ocorrência: ')
            elif op == '0':
                return
            else:
                print(' Opção inválida.')

            with open('ocorrencias.json', 'w', encoding='utf-8') as arquivo_ocorrencias:
                json.dump(ocorrencias, arquivo_ocorrencias, indent=2, ensure_ascii=False)

            print(' Ocorrência alterada com sucesso.')
        else:
            print(' Número de ocorrência inválido.')
    except ValueError:
        print('Digite um número válido.')


def listar_ocorrencias():
    print('\n>>>>> Listar Ocorrências <<<<<')
    with open('ocorrencias.json', 'r', encoding='utf-8') as arquivo_ocorrencias:
        ocorrencias = json.load(arquivo_ocorrencias)

    if not ocorrencias:
        print('Não há ocorrências para listar.')
        return

    for i, ocorrencia in enumerate(ocorrencias):
        print(f'\nOcorrência {i + 1}:')
        print(f"Data: {ocorrencia['data']}")
        print(f"Status: {'Aberta' if ocorrencia['status'] else 'Fechada'}")
        print(f"Tipo: {ocorrencia['tipoOcorrencia']}")
        print(f"Local: {ocorrencia['local']}")
        print(f"Observações: {ocorrencia['observacoes']}")
        print('----------------------------')


# Executando o Programa
menu_principal()
