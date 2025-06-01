from funcoes.func_eventos import listar_eventos
from funcoes.func_participantes import buscar_participante

def menu():
    while True:
        print("Bem vindo ao Gerenciamento de eventos!")
        print('Por favor selecione uma das opções a seguir:')
        print(f'Opção 1 - Cadastrar usuário.\nOpção 2 - Cadastrar-se em evento.\nOpção 3 - Listar Eventos Programados.\nOpção 4 - Listar participantes por evento.\nOpção 5 - Verificar código ou email de participante.\nOpção 6 - Sair.')