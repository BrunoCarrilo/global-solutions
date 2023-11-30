# DesfibrilaDrone   
## Introdução
Este projeto acadêmico foi idealizado com o intuito de abordar a problemática proposta pela Global Solution, em parceria com a FIAP e a Hapvida NotreDame Intermédica. O objetivo central é contribuir para a transformação do setor de saúde ao participar do desafio Tech Care For All, apresentando uma proposta de solução alinhada com as metas estabelecidas pela ODS 3.

Nesta etapa específica do projeto, integrada à disciplina "Computational Thinking Using Python", desenvolvemos o projeto DesfibrilaDrone. Este é um drone inteligente equipado com um Desfibrilador Externo Automático (DEA) e outros dispositivos médicos. Sob o controle remoto de médicos capacitados, esse dispositivo inovador responde rapidamente a emergências, superando obstáculos físicos. Após o registro da ocorrência, o drone é imediatamente acionado, seguindo rotas otimizadas. A intervenção médica remota ocorre com médicos avaliando a situação por meio de transmissões de vídeo em tempo real, possibilitando intervenções imediatas no local em situações críticas.


## Índice
- [DesfibrilaDrone](#desfibriladrone)
  - [Introdução](#introdução)
  - [Índice](#índice)
  - [Integrantes](#integrantes)
  - [Vídeo](#vídeo)
  - [Descrição](#descrição)
  - [Funcionalidades](#funcionalidades)
  - [Funções](#funções)
  - [Requisitos e Dependências](#requisitos-e-dependências)
 

## Integrantes
 -  **RM554086** - Bruno Carrilo de Moraes
 -  **RM552661** - Iago Santos Assis
 -  **RM552981** - Patricia Naomi Yamagishi
 
## Vídeo
Vídeo da explicação do projeto da Global Solution e o código em execução: [Link no YouTube ALTERAR LINK](https://www.youtube.com/watch?v=wS5WSZMN7d8&ab_channel=BrunoCarrilo)

## Descrição
O código adota um formato de menu interativo, possibilitando que os usuários executem diversas operações relacionadas ao DesfibrilaDrone e às ocorrências médicas. Um desses menus visa a interação com o usuário final, fornecendo informações detalhadas sobre o projeto, explicando sua finalidade, benefícios e funcionalidades. Já o segundo menu é destinado ao administrador, permitindo que, após o login, ele possa registrar, modificar e visualizar todas as ocorrências listadas no sistema do drone.

## Funcionalidades
1.  **Informação para Usuários:**
    
    -   Fornece informações detalhadas sobre o projeto DesfibrilaDrone, sua missão, objetivos, funcionalidades principais, operação e benefícios.
2.  **Gestão de Ocorrências para Administradores:**
    
    -   Permite que administradores realizem login, registrem, modifiquem e visualizem ocorrências médicas no sistema do drone.
3.  **Login e Recuperação de Senha:**
    
    -   Implementa um sistema de login para autenticação de administradores e uma opção para recuperar senha caso seja esquecida.
4.  **Registro e Alteração de Ocorrências:**
    
    -   Administra o registro e a alteração de ocorrências médicas, incluindo informações como tipo, data, local, status (aberta/fechada) e observações.
5.  **Listagem de Ocorrências:**
    
    -   Permite listar todas as ocorrências médicas registradas no sistema.
6.  **Persistência de Dados:**
    
    -   Armazena os dados de usuários e ocorrências em arquivos JSON (`usuarios.json` e `ocorrencias.json`).


[:arrow_double_up: voltar ao índice :arrow_double_up: ](#índice)

## Funções
1.  **menu_principal:**
    
    -   Este é o ponto de entrada do programa. Exibe um menu principal com opções para usuários e administradores. Dependendo da escolha do usuário, redireciona para os menus correspondentes ou encerra o programa.
2.  **menu_usuario:**
    
    -   Apresenta opções relacionadas a informações sobre o DesfibrilaDrone para usuários. Cada opção fornece informações específicas sobre o projeto, sua missão, funcionalidades, funcionamento, benefícios, ou permite voltar ao menu principal.
3.  **menu_administrador:**
    
    -   Oferece opções para administradores, como realizar login, recuperar senha ou voltar ao menu anterior.
4.  **carregar_dados_usuarios:**
    
    -   Lê os dados dos usuários de um arquivo JSON chamado `usuarios.json` e retorna esses dados.
5.  **realizar_login:**
    
    -   Solicita login e senha, verifica a autenticidade e, se bem-sucedido, direciona para o menu de ocorrências associado ao administrador logado.
6.  **esqueci_a_senha:**
    
    -   Permite que um administrador recupere sua senha através do e-mail associado ao login.
7.  **menu_ocorrencia:**
    
    -   Apresenta um menu de ocorrências para administradores, com opções para registrar uma nova ocorrência, alterar ocorrências existentes, listar todas as ocorrências ou sair do programa.
8.  **registrar_ocorrencia:**
    
    -   Registra uma nova ocorrência, coletando informações como tipo, data, local, status, observações e associando a ocorrência ao administrador que a registrou.
9.  **alterar_ocorrencias:**
    
    -   Permite que administradores visualizem, selecionem e alterem o status ou detalhes de ocorrências existentes.

9.  **listar_ocorrencias:**
    
    -   Apresenta uma lista de todas as ocorrências registradas, exibindo informações como tipo, data, status, local e observações.

    
[:arrow_double_up: voltar ao índice :arrow_double_up:](#índice)



 
## Requisitos e Dependências

Para executar este código, você precisará dos seguintes requisitos e dependências:

1.  **Python**: O código é escrito em Python, portanto, você precisa ter o Python instalado em seu sistema. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).
    
2.  **Arquivos de Dados**:
    
    -   `usuarios.json`: Um arquivo JSON que armazena informações sobre os usuários.
    -   `ocorrencias.json`: Um arquivo JSON que mantém o registro de ocorrências.
3.  **Módulos Python**:
    
    -   `json`: Este módulo é usado para ler e escrever dados JSON. Normalmente, ele já está incluído na instalação padrão do Python.
    -   `datetime`: Este módulo é usado para trabalhar com datas e horas. Também é parte da instalação padrão do Python.

Certifique-se de ter todos esses requisitos atendidos antes de executar o código. Além disso, os arquivos `usuarios.json` e `ocorrencias.json` devem existir no mesmo diretório do script ou fornecer caminhos absolutos corretos para esses arquivos.

[:arrow_double_up: voltar ao índice :arrow_double_up: ](#índice)
