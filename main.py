from funcoes.func_eventos import eventos_disponiveis, listar_eventos_programados
from funcoes.func_participantes import cadastrar,login,inscricao_evento,buscar_cod_participante,buscar_email_participante
from funcoes.func_org import menu_org


def menu():
    while True:
        print("Bem vindo ao Gerenciamento de eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print(f'Opção 1 - Cadastrar usuário.\nOpção 2 - Fazer login.\nOpção 3 - É um organizador? Selecione esta opção!\nOpção 4 - Verificar informações com código ou email de participante.\nOpção 5 - Sair.')

        opcao = input('Insira a opção desejada: ')

        if opcao == '1':
            nome = input('Insira o seu nome: ')
            email = input('Insira o seu email: ')
            senha = input('Insira a senha desejada: ')
            preferencias = input('Insira suas preferências (separadas por vírgula): ').split(',')
            cadastrar(nome, email, senha, [preferencia.strip() for preferencia in preferencias])

        elif opcao == '2':
            email = input('Insira o email cadastrado: ')
            senha = input('Insira a senha: ')
            usuario_logado = login(email, senha)
            if usuario_logado:
                while True:
                    print('Por favor selecione uma das opções a seguir:')
                    print(f'Opção 1 - Cadastrar-se em evento.\nOpção 2 - Listar Eventos Programados.\nOpção 3 - Sair.')

                    opcao_user = input('Insira a opção desejada: ')

                    if opcao_user == '1':
                        eventos_disponiveis()
                        nomeEvento = input('Insira o nome do evento desejado: ')
                        codigo = input('Insira seu código de participante: ')
                        inscricao_evento(nomeEvento,codigo)

                    elif opcao_user == '2':
                        listar_eventos_programados()

                    elif opcao_user == '3':
                        print(f'Até mais, {usuario_logado["nome"]}!')
                        menu()

        elif opcao == '3':
            menu_org()

        elif opcao == '4':
            print('Deseja verificar informações com código de participante ou email?')
            print(f'Opção 1 - Busca por código de participante.\nOpção 2 - Busca por email de participante.')
            opcao = input('Insira a opção desejada: ')
            if opcao == '1':
                codigo = input('Insira o código de participante: ')
                buscar_cod_participante(codigo)
                continuar = input('Deseja escolher outra opção? (s/n): ')
                if continuar.lower() == 's':
                    menu()
                else:
                    print('Até mais!')
                    break
            elif opcao == '2':
                email = input('Insira o email: ')
                buscar_email_participante(email)
                continuar = input('Deseja escolher outra opção? (s/n): ')
                if continuar.lower() == 's':
                    menu()
                else:
                    print('Até mais!')
                    break
            else:
                print('Insira uma opção válida.')
                continuar = input('Deseja escolher outra opção? (s/n): ')
   
        elif opcao == '5':
            print('Até outra hora!')
            break
        else:
            print('Por favor insira uma opção válida.')

if __name__ == "__main__":
    menu()