from funcoes.func_eventos import listar_eventos
from funcoes.func_participantes import cadastrar,login,inscricao_evento#,buscar_cod_participante,buscar_email_participante ##codigo nao funciona pois importei primeiro

def menu():
    while True:
        print("Bem vindo ao Gerenciamento de eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print(f'Opção 1 - Cadastrar usuário.\nOpção 2 - Fazer login.\nOpção 3 - Cadastrar-se em evento.\nOpção 4 - Listar Eventos Programados.\nOpção 5 - Listar participantes por evento.\nOpção 6 - Verificar informações com código de participante.\nOpção 7 - Verificar informações com email de participante.\nOpção 8 - Sair.')

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
            login(email, senha)

        elif opcao == '3':
            print(f'Eventos disponiveis:\n{listar_eventos()}')
            nomeEvento = input('Insira o nome do evento desejado: ')
            codigo = input('Insira seu código de participante: ')
            inscricao_evento(nomeEvento,codigo)

        elif opcao == '4':
            listar_eventos()

        #elif opcao == '5': talvez colocar essa opcao no perfil de gerenciadores, clientes nao conseguiriam ver os participantes.

        # elif opcao == '6':
        #     codigo = input('Insira seu código de participante:')
        #     buscar_cod_participante(codigo)

        # elif opcao == '7':
        #     email = input('Insira seu email de participante:')
        #     buscar_email_participante(email)
        
        elif opcao == '8':
            print('Até outra hora!')
            break
        else:
            print('Por favor insira uma opção válida.')

if __name__ == "__main__":
    menu()