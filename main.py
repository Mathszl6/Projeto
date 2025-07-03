from funcoes.func_eventos import eventos_disponiveis, listar_eventos_programados, buscar_evento_por_tema, buscar_evento_por_data
from funcoes.func_participantes import cadastrar,login,inscricao_evento,buscar_cod_participante,buscar_email_participante, atualizar_dados_participante, remover_participante_e_atualizar_eventos
from funcoes.func_org import menu_org


def menu():
    while True:
        print("\nBem vindo ao Gerenciamento de eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print('\nOpção 1 - Cadastrar usuário.\nOpção 2 - Fazer login.\nOpção 3 - É um organizador? Selecione esta opção!\nOpção 4 - Verificar informações com código ou email de participante.\nOpção 5 - Sair.')

        opcao = input('\nInsira somente o número da opção desejada: ')

        if opcao == '1':
            print('\nOpção de cadastrar usuário selecionada!\n\nPor favor,')
            nome = input('Insira o seu nome: ')
            email = input('Insira o seu email: ')
            senha = input('Insira a senha desejada: ')
            preferencias = input('Insira suas preferências (separadas por vírgula): ').split(',')
            cadastrar(nome, email, senha, [preferencia.strip() for preferencia in preferencias])

        elif opcao == '2':
            print('\nOpção de login selecionada!\n\nPor favor,')
            email = input('Insira o email cadastrado: ')
            senha = input('Insira a senha: ')
            usuario_logado = login(email, senha)
            if usuario_logado:
                while True:
                    print('\nPor favor selecione uma das opções a seguir:')
                    print(f'\nOpção 1 - Cadastrar-se em evento.\nOpção 2 - Listar Eventos Programados.\nOpcão 3 - Atualizar dados.\nOpcão 4 - Buscar evento por tema ou data.\nOpcão 5 - Excluir conta.\nOpção 6 - Sair.')

                    opcao_user = input('\nInsira somente o número da opção desejada: ')

                    if opcao_user == '1':
                        print('\nOpção de cadastrar-se em evento selecionada!')
                        eventos_disponiveis()
                        print('\nPor favor,')
                        nomeEvento = input('Insira o nome do evento desejado: ')
                        codigo = input('Insira seu código de participante: ')
                        inscricao_evento(nomeEvento,codigo)
                    elif opcao_user == '2':
                        print('\nOpção de listar eventos programados selecionada!')
                        listar_eventos_programados()
                    elif opcao_user == '3':
                        print('\nOpção de atualizar dados selecionada!')
                        codigo_participante = input('Digite o código de participante: ')
                        novo_email = input('Digite o novo email: ')
                        nova_senha = input('Digite a nova senha: ')
                        atualizar_dados_participante(codigo=codigo_participante, novo_email= novo_email, nova_senha=nova_senha)
                    elif opcao_user == '4':
                        print('\nOpção de filtrar eventos por tema ou data selecionada!')
                        print('\nDeseja filtrar os eventos por tema ou por data?')
                        print('\nOpção 1 - Filtrar por tema de evento.\nOpção 2 - Filtrar por data de evento.')
                        opcao_filtro = input('\nInsira somente o número da opção desejada: ')
                        if opcao_filtro == '1':
                            print('\nOpção de filtrar eventos por tema selecionada!\n\nPor favor,')
                            tema_user = input('Digite o tema do evento: ')
                            buscar_evento_por_tema(tema=tema_user)
                            continuar_filtro = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar_filtro.lower() != 's':
                                print('Até mais!\n')
                                break    
                        elif opcao_filtro == '2':
                            print('\nOpção de filtrar eventos por data selecionada!\n\nPor favor,')       
                            data = input('Digite a data: ')
                            buscar_evento_por_data(data=data)
                            continuar_filtro = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar_filtro.lower() != 's':
                                print('Até mais!\n')
                                break
                        else:
                            print('\nInsira uma opção válida.')
                            continuar_filtro = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar_filtro.lower() != 's':
                                print('Até mais!\n')
                                break
                    elif opcao_user == '5':
                        print('\nOpção de excluir conta selecionada!')  
                        cod_participante = input('\nDigite o código de participante: ')
                        resposta_user = input('\nVocê tem certeza? (s/n)') 
                        if resposta_user == 's':
                            remover_participante_e_atualizar_eventos(codigo_participante=cod_participante)
                            break
                    elif opcao_user == '6':
                        print(f'Até mais, {usuario_logado["nome"]}!\n')
                        break

        elif opcao == '3':
            menu_org()

        elif opcao == '4':
            print('\n\nDeseja verificar informações com código de participante ou email?')
            print('\nOpção 1 - Busca por código de participante.\nOpção 2 - Busca por email de participante.')
            opcao = input('\nInsira a opção desejada: ')
            if opcao == '1':
                print('\nVerificar informações via código de participante selecionado!\n\nPor favor,')
                codigo = input('Insira o código de participante: ')
                buscar_cod_participante(codigo)
                continuar = input('\nDeseja escolher outra opção? (s/n): ')
                if continuar.lower() == 's':
                    menu()
                else:
                    print('Até mais!\n')
                    break
            elif opcao == '2':
                print('\nVerificar informações via email de participante selecionado!\n\nPor favor,')
                email = input('Insira o email: ')
                buscar_email_participante(email)
                continuar = input('\nDeseja escolher outra opção? (s/n): ')
                if continuar.lower() == 's':
                    menu()
                else:
                    print('Até mais!\n')
                    break
            else:
                print('\nInsira uma opção válida.')
                continuar = input('\nDeseja escolher outra opção? (s/n): ')
                if continuar.lower() == 's':
                    menu()
                else:
                    print('Até mais!\n')
                    break
   
        elif opcao == '5':
            print('Até outra hora!\n')
            break
        else:
            print('\nPor favor insira uma opção válida.\n')

if __name__ == "__main__": #verifica se o nome executado é igual a "main", se for igual ele executa se n for ele n executa, pra evitar erro de execucao e importacao 
    menu()

