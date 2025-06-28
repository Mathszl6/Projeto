from funcoes.utils import gerar_codigoORG, ler_org, ler_eventos,gerar_estatisticas
from dados.organizador import organizadores as dados_organizador
from funcoes.func_eventos import listar_eventos_programados,cadastrar_evento
from funcoes.func_participantes import buscar_cod_participante,buscar_email_participante

def menu_org():
    while True:
        print("Bem vindo ao menu de Organizador do Gerenciamento de Eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print(f'Opção 1 - Cadastrar-se.\nOpção 2 - Fazer login.\nOpção 3 - Sair.')

        opcao_menu_org = input('Insira a opção desejada: ')

        if opcao_menu_org == '1':
            nome = input('Insira o seu nome: ')
            email = input('Insira o seu email: ')
            senha = input('Insira a senha desejada: ')
            cadastrar_org(nome, email, senha)

        elif opcao_menu_org == '2':
            codigo_org = input('Insira o código de organizador cadastrado: ')
            senha = input('Insira a senha: ')
            organizador_logado = login_org(codigo_org, senha)
            if organizador_logado:
                while True:
                    print('Selecione uma das opções a seguir:')
                    print(f'Opção 1 - Listar Eventos Programados.\nOpção 2 - Listar participantes por evento.\nOpção 3 - Verificar informações de participante.\nOpção 4 - Cadastrar evento.\nOpção 5 - Gerar estatisticas.\nOpção 6 - Voltar ao menu de Organizador.')

                    opcao_org = input('Por favor insira a opção desejada: ')
                    if opcao_org == '1':
                        listar_eventos_programados()

                    elif opcao_org == '2':
                        evento = ler_eventos()
                        for event in evento:
                            print(f'A quantidade de participantes do evento {event["nome"]} é: {len(event['participantes'])}.')

                    elif opcao_org == '3':
                        print('Deseja verificar informações com código de participante ou email?')
                        print(f'Opção 1 - Busca por código de participante.\nOpção 2 - Busca por email de participante.')
                        escolha = input('Insira a opção desejada: ')
            
                        if escolha == '1':
                            codigo = input('Insira o código de participante: ')
                            buscar_cod_participante(codigo)
                            continuar = input('Deseja escolher outra opção? (s/n): ')
                        if continuar.lower() == 's':
                            menu_org()
                        else:
                            print('Até mais!')
                            break
                        if escolha == '2':
                            email = input('Insira o email: ')
                            buscar_email_participante(email)
                            continuar = input('Deseja escolher outra opção? (s/n): ')
                            if continuar.lower() == 's':
                                menu_org()
                            else:
                                print('Até mais!')
                                break
                        else:
                            print('Insira uma opção válida.')
                            continuar = input('Deseja escolher outra opção? (s/n): ')

                    elif opcao_org == '4':
                        nome = input('Insira o nome do evento: ')
                        data = input('Insira a data do evento: ')
                        tema = input('Insira o tema do evento: ')
                        cadastrar_evento(nome,data,tema)
                    
                    elif opcao_org == '5':
                        gerar_estatisticas()
                    
                    elif opcao_org == '6':
                        print('Voltando..')
                        break

        elif opcao_menu_org == '3':
            print('Saindo..')
            break
        else:
            print('Por favor insira uma opção válida.')



def cadastrar_org(nome, email, senha):
    codigo_org = gerar_codigoORG()
    novo_org = {
        'codigo': codigo_org,
        'nome': nome,
        'email': email,
        'senha': senha
    }
    dados = dados_organizador.copy()
    orgs = ler_org()
    for organizador in orgs:
        if organizador['email'] == novo_org['email']:
            print('Email já cadastrado em outro organizador.')
            return False
        
    dados.append(novo_org)
    with open ('dados/organizador.py', 'w') as file:
        file.write(f'organizadores = {dados}')
    
    print(f'Organizador {nome} cadastrado com sucesso!\nCódigo de Organizador: {codigo_org}')
    return True

def login_org(codigo_org,senha):
    orgs = ler_org()
    for organizador in orgs:
        if organizador['codigo'] == codigo_org:
            if organizador['senha'] == senha:
                print(f'Seja bem vindo {organizador['nome']}.')
                return organizador
            else:
                print('Senha incorreta.')
                return
    print('Código não encontrado.')