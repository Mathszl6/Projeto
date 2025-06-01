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
    participantes.append(novo_part)
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
def inscricao_evento(eventos.nome, codigo):
    

def buscar_cod_participante(codigo):

def buscar_email_participante(email):
