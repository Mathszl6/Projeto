from utils import gerar_codigoORG,ler,gerar_estatisticas
from dados.organizador import organizadores as dados_organizador
from funcoes.func_eventos import listar_eventos_programados,cadastrar_evento,atualizar_dados_evento
from funcoes.func_participantes import buscar_cod_participante,buscar_email_participante

def menu_org():
    while True:
        print("\n\nBem vindo ao menu de Organizador do Gerenciamento de Eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print(f'\nOpção 1 - Cadastrar-se.\nOpção 2 - Fazer login.\nOpção 3 - Sair.')

        opcao_menu_org = input('\nInsira a opção desejada: ')

        if opcao_menu_org == '1':
            print('\nOpção de cadastrar organizador selecionada!\n\nPor favor,')
            nome = input('Insira o seu nome: ')
            email = input('Insira o seu email: ')
            senha = input('Insira a senha desejada: ')
            cadastrar_org(nome, email, senha)

        elif opcao_menu_org == '2':
            print('\nOpção de fazer login selecionada!\n\nPor favor,')
            codigo_org = input('Insira o código de organizador cadastrado: ')
            senha = input('Insira a senha: ')
            organizador_logado = login_org(codigo_org, senha)
            if organizador_logado:
                while True:
                    print('\nSelecione uma das opções a seguir:')
                    print(f'\nOpção 1 - Listar Eventos Programados.\nOpção 2 - Listar participantes por evento.\nOpção 3 - Verificar informações de participante.\nOpção 4 - Cadastrar evento.\nOpção 5 - Gerar estatisticas.\nOpção 6 - Atualizar dados de evento.\nOpção 7 - Voltar ao Menu de Organizador.')

                    opcao_org = input('\nPor favor insira a opção desejada: ')
                    if opcao_org == '1':
                        listar_eventos_programados()

                    elif opcao_org == '2':
                        evento = ler('dados/eventos.py')
                        for event in evento:
                            print(f'\nA quantidade de participantes do evento {event["nome"]} é: {len(event['participantes'])}.')

                    elif opcao_org == '3':
                        print('\nDeseja verificar informações com código de participante ou email?')
                        print(f'\nOpção 1 - Busca por código de participante.\nOpção 2 - Busca por email de participante.')
                        escolha = input('\nInsira a opção desejada: ')
            
                        if escolha == '1':
                            print('\nVerificar informações via código de participante selecionado!\n\nPor favor,')
                            codigo = input('Insira o código de participante: ')
                            buscar_cod_participante(codigo)
                            continuar = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar.lower() != 's':
                                print('Até mais!\n')
                                break
                        elif escolha == '2':
                            print('\nVerificar informações via email de participante selecionado!\n\nPor favor,')
                            email = input('Insira o email: ')
                            buscar_email_participante(email)
                            continuar = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar.lower() != 's':
                                print('Até mais!\n')
                                break
                        else:
                            print('\nInsira uma opção válida.')
                            continuar = input('\nDeseja escolher outra opção? (s/n): ')
                            if continuar.lower() == 's':
                                print('Até mais!\n')
                                break

                    elif opcao_org == '4':
                        print('\nOpção de cadastro de evento selecionada!\n\nPor favor,')
                        nome = input('Insira o nome do evento: ')
                        data = input('Insira a data do evento: ')
                        tema = input('Insira o tema do evento: ')
                        cadastrar_evento(nome,data,tema)
                    
                    elif opcao_org == '5':
                        gerar_estatisticas()

                    elif opcao_org == '6':
                        print('\nOpção de atualizar dados selecionada!')
                        nome_evento = input('Digite o código de participante: ')
                        novo_tema = input('Digite o novo tema: ')
                        nova_data = input('Digite a nova data: ')
                        atualizar_dados_participante(codigo=nome_evento, novo_tema= novo_tema, nova_data=nova_data)
                        
                    
                    elif opcao_org == '7':
                        print('Voltando..\n')
                        break

        elif opcao_menu_org == '3':
            print('Saindo..\n')
            break
        else:
            print('\nPor favor insira uma opção válida.')



def cadastrar_org(nome, email, senha):
    codigo_org = gerar_codigoORG()
    novo_org = {
        'codigo': codigo_org,
        'nome': nome,
        'email': email,
        'senha': senha
    }
    dados = dados_organizador.copy()
    orgs = ler('dados/organizador.py')
    for organizador in orgs:
        if organizador['email'] == novo_org['email']:
            print('\nEmail já cadastrado em outro organizador.')
            return False
        
    dados.append(novo_org)
    with open ('dados/organizador.py', 'w') as file:
        file.write(f'organizadores = {dados}')
    
    print(f'\nOrganizador {nome} cadastrado com sucesso!\nCódigo de Organizador: {codigo_org}')
    return True

def login_org(codigo_org,senha):
    orgs = ler('dados/organizador.py')
    for organizador in orgs:
        if organizador['codigo'] == codigo_org:
            if organizador['senha'] == senha:
                print(f'\nSeja bem vindo {organizador['nome']}.')
                return organizador
            else:
                print('\nSenha incorreta.')
                return
    print('\nCódigo não encontrado.')