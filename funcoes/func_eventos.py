from dados.eventos import eventos

def listar_eventos():
    print('Lista dos Eventos Programados')
    for evento in eventos:
        print(f'Nome: {evento['nome']} | Data: {evento["data"]} | Tema: {evento['tema']}')