from dados.participantes import participantes as dados_participante
from dados.eventos import eventos
from utils import ler, gerar_codigoPA
        
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
    pessoas = ler('dados/participantes.py')
    for participante in pessoas:
        if participante['email'] == novo_part['email']:
            print('Email já cadastrado em outro participante.')
            return False

    dados.append(novo_part)
    with open ('dados/participantes.py', 'w') as file:
        file.write(f'participantes = {dados}')
    print(f'\nParticipante {nome} cadastrado com sucesso!\nCódigo de Participante: {codigo}\n')
    


def login(email, senha):
    pessoas = ler('dados/participantes.py')
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
    participantes = ler('dados/participantes.py')
    evento = ler('dados/eventos.py')
    for event in evento:
        if event['nome'] == nome_evento:
            if codigo in event['participantes']:
                print(f'\nVocê já está inscrito no evento {nome_evento}.')
                return
            if any(participante['codigo'] == codigo for participante in participantes):
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
    participantes = ler('dados/participantes.py')
    for participante in participantes:
        if participante['codigo'] == codigo:
            print(f'\n\nForam encontradas as seguintes informações do participante com código: {participante['codigo']}')
            print(f'\nCódigo:{participante['codigo']} | Nome: {participante["nome"]} | Email: {participante["email"]} | Preferências: {participante["preferencias"]}\n')
            return
    print('\nCódigo não encontrado.\n')
    return

def buscar_email_participante(email):
    participantes = ler('dados/participantes.py')
    for participante in participantes:
        if participante['email'] == email:
            print(f'\n\nForam encontradas as seguintes informações do participante com email: {participante['email']}')
            print(f'\nCódigo:{participante['codigo']} | Nome: {participante["nome"]} | Email: {participante["email"]} | Preferências: {participante["preferencias"]}\n')
            return
    print('\nEmail não encontrado.\n')
    return

def atualizar_dados_participante(codigo, novo_email=None, nova_senha=None):
    participantes = ler('dados/participantes.py')
    encontrado = False

    for participante in participantes:
        if participante['codigo'] == codigo:
            if novo_email:
                participante['email'] = novo_email
            if nova_senha:
                participante['senha'] = nova_senha
            encontrado = True
            break
    if encontrado:
        with open ('dados/participantes.py', 'w') as file:
            file.write(f"participantes = {participantes}")
        print("\nDados atualizados com sucesso!")
    else:
        print("\nParticipante não encontrado. Você inseriu o código certo?")

def remover_participante_e_atualizar_eventos(codigo_participante):
    # Remove do arquivo de participantes
    participantes = ler('dados/participantes.py')
    nova_lista = [participante for participante in participantes if participante['codigo'] != codigo_participante]

    if len(nova_lista) == len(participantes):
        print("\nParticipante não encontrado.")
        return
    else:
        with open ('dados/participantes.py', 'w') as file:
            file.write(f"participantes = {nova_lista}")
        print(f"\nParticipante com o código: {codigo_participante} foi removido com sucesso.")

    # Atualiza os eventos, removendo esse participante das listas
    eventos = ler('dados/eventos.py')
    for evento in eventos:
        if codigo_participante in evento['participantes']:
            evento['participantes'].remove(codigo_participante)

    with open ('dados/eventos.py', 'w') as file:
        file.write(f"eventos = {eventos}")
    print(f"\nO participante com o código: {codigo_participante} também foi removido de todos os eventos.")