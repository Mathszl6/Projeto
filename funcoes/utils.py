from dados.participantes import participantes as dados_participante
from dados.organizador import organizadores as dados_organizador
from dados.eventos import evento as dados_evento
from random import randint
from collections import Counter
import ast ## abstract syntax tree, le codigos como se fosse string, assim executado codigos seguros, caso contrario ele exibe erro.

def ler():
    with open ('dados/participantes.py', 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()
 
        ## Encontrando o inicio da lista de vdd pois esta considerando 'participantes =' como atributo inves de var 
        inicio_lista = lendo.find('[')
        total_dados = lendo[inicio_lista:]
        return ast.literal_eval(total_dados)

def ler_eventos():
    with open ('dados/eventos.py', 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()
        
        ## Encontrando o inicio da lista de vdd pois esta considerando 'eventos =' como atributo inves de var 
        inicio_eventos = lendo.find('[')
        final_dados = lendo[inicio_eventos:]
        return ast.literal_eval(final_dados)

def ler_org():
    with open ('dados/organizador.py', 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()

        ## Encontrando o inicio da lista de vdd pois esta considerando 'organizador =' como atributo inves de var 
        inicio_lista = lendo.find('[')
        total_dados = lendo[inicio_lista:]
        return ast.literal_eval(total_dados)


## Funcoes para geração de codigo de Participante e de Organizador

def gerar_codigoPA():
    dados_participante = ler() ## para confirmar se o codigo esta vazio ou tem algo para comparar com o codigo de organizador
    while True: #garante que o código seja unico
        codigo = f'PA{randint(1000,9999)}'
        if not any(participante['codigo'] == codigo for participante in dados_participante):
            return codigo
        else: 
            continue

def gerar_codigoORG():
    dados_organizador = ler_org() ## para confirmar se o codigo esta vazio ou tem algo para comparar com o codigo de participante
    while True: #garante que o código seja unico
        codigo = f'OR{randint(1000,9999)}'
        if not any(organizador['codigo'] == codigo for organizador in dados_organizador):
            return codigo
        else: 
            continue

def gerar_estatisticas():
    dados_evento = ler_eventos()
    contagem = Counter()
    temas = Counter()
    
    for evento in dados_evento:
        tema = evento.get('tema', '').strip().lower()
        temas[tema] += 1

        for codigo in evento.get('participantes', []):
            contagem[codigo]+=1

    print('\nTemas mais frequentes:\n')
    for tema, qtd in temas.most_common(3):
        if qtd == 1:
            print(f'{tema.capitalize()}: aparece em {qtd} evento.')
        else:
            print(f'{tema.capitalize()}: aparece em {qtd} eventos.')
    print('\nParticipantes mais ativos:\n')        
    for codigo, qtd in contagem.most_common(3):
        if qtd == 1:
            print(f'O participante com código: {codigo}, participou em {qtd} evento.')
        else: 
            print(f'O participante com código: {codigo}, participou em {qtd} eventos.')