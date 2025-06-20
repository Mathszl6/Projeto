from dados.eventos import eventos

def eventos_disponiveis():
    print('Eventos disponiveis para inscrição: ')
    for evento in eventos:
        print(f'Nome: {evento['nome']} | Data: {evento['data']} | Tema : {evento['tema']}')

def listar_eventos_programados():
    print('Lista dos Eventos Programados')
    for evento in eventos:
        print(f'Nome: {evento['nome']} | Data: {evento["data"]} | Tema: {evento['tema']}')