from dados.participantes import participantes
from dados.eventos import eventos
from random import randint

def gerar_codigo():
    while True: #garante que o código seja unico
        codigo = f'PA{randint(1000,9999)}'
        if not any(participante['codigo'] == codigo for participante in participantes):
            return codigo
        
def cadastrar(nome, email, senha, preferencias):
    codigo = gerar_codigo()
    novo_part = {
        'codigo': codigo,
        'nome': nome,
        'email': email,
        'senha': senha,
        'preferencias': preferencias
    }
    with open ('participantes.py', 'w') as file:
        file.write(f'participantes = {participantes}\n{participantes.append(novo_part)}')
    print(f'Participante {nome} cadastrado com sucesso!\nCódigo de Participante: {codigo}')

def login(email, senha):
    for participante in participantes:
        if participante['email'] == email:
            if participante['senha'] == senha:
                print(f'Seja bem vindo {participante['nome']}.')
            else:
                print('Senha incorreta.')
        else:
            print('Email não encontrado.')

def inscricao_evento(nomeEvento, codigo):
    for evento in eventos:
        if evento['nome'] == nomeEvento:
            for participante in participantes:
                if participante['codigo'] == codigo:
                    eventos['participantes'].append(participante)
                    print(f'Você está inscrito no evento {nomeEvento}')
            else:
                print('Seu código não foi encontrado. Você está cadastrado?')
        else:
            print('Evento não encontrado.')

# def buscar_cod_participante(codigo):

# def buscar_email_participante(email):
