from dados.participantes import participantes as dados_participante
from dados.eventos import eventos
from funcoes.utils import ler, gerar_codigo, ler_eventos
        
def cadastrar(nome, email, senha, preferencias):
    codigo = gerar_codigo()
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
        else:
            dados.append(novo_part)
            with open ('dados/participantes.py', 'w') as file:
                file.write(f'participantes = {dados}')
    print(f'Participante {nome} cadastrado com sucesso!\nCódigo de Participante: {codigo}')
    


def login(email, senha):
    pessoas = ler()
    for participante in pessoas:
        if participante['email'] == email:
            if participante['senha'] == senha:
                print(f'Seja bem vindo {participante['nome']}.')
                return
            else:
                print('Senha incorreta.')
                return
    print('Email não encontrado.')



def inscricao_evento(nomeEvento, codigo):
    participantes = ler()
    eventos = ler_eventos()

    for evento in eventos:
        if evento['nome'] == nomeEvento:
            if codigo in evento['participantes']:
                print(f'Você já está inscrito no evento {nomeEvento}')
                return
            
            if any(participante.get('codigo') == codigo for participante in participantes):
                evento['participantes'].append(codigo)
                with open ('dados/eventos.py', 'w') as file:
                    file.write(f'evento = {eventos}')
                print(f'Você se inscreveu no evento {nomeEvento}.')
                return
            else:
                print('Seu código não foi encontrado. Você está cadastrado?')
                return
    print('Evento não encontrado.')



# def buscar_cod_participante(codigo):

# def buscar_email_participante(email):
