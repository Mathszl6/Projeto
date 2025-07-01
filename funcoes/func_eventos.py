from dados.eventos import evento as dados_evento
from funcoes.utils import ler_eventos

def eventos_disponiveis():
    print('\nEventos disponiveis para inscrição: ')
    for event in dados_evento:
        print(f'Nome: {event['nome']} | Data: {event['data']} | Tema : {event['tema']}\n')

def listar_eventos_programados():
    print('\nLista dos Eventos Programados: \n')
    for event in dados_evento:
        print(f'Nome: {event['nome']} | Data: {event["data"]} | Tema: {event['tema']}')

def cadastrar_evento(nome,data,tema):
    novo_evento = {
        'nome': nome,
        'data': data,
        'tema': tema,
        'participantes': []
    }
    dados = dados_evento.copy()
    eventos = ler_eventos()
    for evento in eventos:
        if evento['nome'] == novo_evento['nome']:
            print('\nEvento já cadastrado.')
            return False

    dados.append(novo_evento)
    with open ('dados/eventos.py', 'w') as file:
        file.write(f'evento = {dados}')
    print(f'\nEvento: {nome} com o tema {tema} foi cadastrado com sucesso!')
