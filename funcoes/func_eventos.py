from dados.eventos import eventos as dados_evento
from utils import ler

def eventos_disponiveis():
    print('\nEventos disponiveis para inscrição: ')
    for event in dados_evento:
        print(f'Nome: {event['nome']} | Data: {event['data']} | Tema : {event['tema']}\n')

def listar_eventos_programados():
    eventos = ler('dados/eventos.py')
    print('\nLista dos Eventos Programados: \n')
    for evento in eventos:
        print(f'Nome: {evento['nome']} | Data: {evento["data"]} | Tema: {evento['tema']}')

def cadastrar_evento(nome,data,tema):
    novo_evento = {
        'nome': nome,
        'data': data,
        'tema': tema,
        'participantes': []
    }
    dados = dados_evento.copy()
    eventos = ler('dados/eventos.py')
    for evento in eventos:
        if evento['nome'] == novo_evento['nome']:
            print('\nEvento já cadastrado.')
            return False

    dados.append(novo_evento)
    with open ('dados/eventos.py', 'w') as file:
        file.write(f'evento = {dados}')
    print(f'\nEvento: {nome} com o tema {tema} foi cadastrado com sucesso!')

def buscar_evento_por_tema(tema):
    eventos = ler('dados/eventos.py')
    eventos_temas_encontrados = [evento for evento in eventos if evento['tema']  == tema] #lista para adicionar os eventos que foram encontrados desse tema
    if eventos_temas_encontrados:
        print('\n\nEventos encontrados:')
        for tema_encontrado in eventos_temas_encontrados:
            print(f"\nNome: {tema_encontrado["nome"]} | Data: {tema_encontrado["data"]} | Tema: {tema_encontrado["tema"]}")
    else:
        print('Nenhum evento encontrado!')

    
def buscar_evento_por_data(data):
    eventos = ler('dados/eventos.py')
    eventos_datas_encontrado = [evento for evento in eventos if evento['data'] == data]
    if eventos_datas_encontrado:
        print('\nEventos encontrados:')
        for data_encontrada in eventos_datas_encontrado:
            print(f"\nNome: {data_encontrada["nome"]} | Data: {data_encontrada["data"]} | Tema: {data_encontrada["tema"]}")
    else:
        print('Nenhum evento encontrado!')

def atualizar_dados_evento(nome, novo_tema=None, nova_data=None):
    eventos = ler('dados/eventos.py')
    encontrado = False

    for evento in eventos:
        if evento['nome'] == nome:
            if novo_tema:
                evento['tema'] = novo_tema
            if nova_data:
                evento['data'] = nova_data
            encontrado = True
            break
    if encontrado:
        with open ('dados/eventos.py', 'w') as file:
            file.write(f"eventos = {eventos}")
        print("\nDados atualizados com sucesso!")
    else:
        print("\nEvento não encontrado. Você inseriu o nome certo?")
        
def buscar_evento_por_tema_org(tema):
    eventos = ler('dados/eventos.py')
    eventos_temas_iguais = [evento for evento in eventos if evento['tema']  == tema] #lista para adicionar os eventos que foram encontrados desse tema
    if eventos_temas_iguais:
        print('\n\nEventos encontrados:')
        for tema_encontrado in eventos_temas_iguais:
            print(f"\nNome: {tema_encontrado["nome"]} | Data: {tema_encontrado["data"]} | Tema: {tema_encontrado["tema"]} | Participantes: {tema_encontrado["participantes"]}")
    else:
        print('Nenhum evento encontrado!')

    
def buscar_evento_por_data_org(data):
    eventos = ler('dados/eventos.py')
    eventos_datas_iguais = [evento for evento in eventos if evento['data'] == data]
    if eventos_datas_iguais:
        print('\nEventos encontrados:')
        for data_encontrada in eventos_datas_iguais:
            print(f"\nNome: {data_encontrada["nome"]} | Data: {data_encontrada["data"]} | Tema: {data_encontrada["tema"]} | Participantes: {data_encontrado["participantes"]}")
    else:
        print('Nenhum evento encontrado!')
