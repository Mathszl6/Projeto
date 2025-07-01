from dados.participantes import participantes as dados_participante
from dados.eventos import evento
from funcoes.utils import ler, gerar_codigoPA, ler_eventos
        
def cadastrar(nome, email, senha, preferencias):
    codigo = gerar_codigoPA()
    novo_part = {
        'codigo': codigo,
        'nome': nome,
        'email': email,
        'senha': senha,
        'preferencias': preferencias
    }
    dados = dados_participante.copy()
    pessoas = ler()
    for participante in pessoas:
        if participante['email'] == novo_part['email']:
            print('Email já cadastrado em outro participante.')
            return False

    dados.append(novo_part)
    with open ('dados/participantes.py', 'w') as file:
        file.write(f'participantes = {dados}')
    print(f'\nParticipante {nome} cadastrado com sucesso!\nCódigo de Participante: {codigo}\n')
    


def login(email, senha):
    pessoas = ler()
    for participante in pessoas:
        if participante['email'] == email:
            if participante['senha'] == senha:
                print(f'\n\nSeja bem vindo ao menu do usuário, {participante['nome']}!')
                return participante
            else:
                print('\nSenha incorreta.')
                return
    print('\nEmail não encontrado.')

def inscricao_evento(nome_evento, codigo):
    participantes = ler()
    evento = ler_eventos()
    for event in evento:
        if event['nome'] == nome_evento:
            if codigo in event['participantes']:
                print(f'\nVocê já está inscrito no evento {nome_evento}.')
                return
            if any(participante.get('codigo') == codigo for participante in participantes):
                event['participantes'].append(codigo)
                with open ('dados/eventos.py', 'w') as file:
                    file.write(f'evento = {evento}')
                print(f'\nVocê se inscreveu no evento {nome_evento}!')
                return
            else:
                print('\nSeu código não foi encontrado. Você está cadastrado?')
                return
    print('\nEvento não encontrado.')



def buscar_cod_participante(codigo):
    participantes = ler()
    for participante in participantes:
        if participante['codigo'] == codigo:
            print(f'\n\nForam encontradas as seguintes informações do participante com código: {participante['codigo']}')
            print(f'\nCódigo:{participante['codigo']} | Nome: {participante["nome"]} | Email: {participante["email"]} | Preferências: {participante["preferencias"]}\n')
            return
    print('\nCódigo não encontrado.\n')
    return

def buscar_email_participante(email):
    participantes = ler()
    for participante in participantes:
        if participante['email'] == email:
            print(f'\n\nForam encontradas as seguintes informações do participante com email: {participante['email']}')
            print(f'\nCódigo:{participante['codigo']} | Nome: {participante["nome"]} | Email: {participante["email"]} | Preferências: {participante["preferencias"]}\n')
            return
    print('\nEmail não encontrado.\n')
    return