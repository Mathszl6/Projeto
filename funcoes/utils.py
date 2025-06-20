from dados.participantes import participantes as dados_participante
from random import randint
import ast ## abstract syntax tree, le codigos como se fosse string, assim executado codigos seguros, caso contrario ele exibe erro.

def ler():
    with open ('dados/participantes.py', 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()
 
        if not lendo: ## para situacoes onde eu zerei os dados de participantes e vou inserir do 0
            return []
        ## Encontrando o inicio da lista de vdd pois esta considerando 'participantes =' como atributo inves de var 
        inicio_lista = lendo.find('[')
        total_dados = lendo[inicio_lista:]
        return ast.literal_eval(total_dados)

def ler_eventos():
    with open ('dados/eventos.py', 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()
        
        if not lendo: ## para situacoes onde eu zerei os dados de eventos e vou inserir do 0
            return []
        ## Encontrando o inicio da lista de vdd pois esta considerando 'eventos =' como atributo inves de var 
        inicio_eventos = lendo.find('[')
        final_dados = lendo[inicio_eventos:]
        return ast.literal_eval(final_dados)



def gerar_codigo():
    dados_participante = ler() ## para confirmar se o codigo esta vazio ou tem algo para comparar com o codigo de participante
    while True: #garante que o código seja unico
        codigo = f'PA{randint(1000,9999)}'
        if not any(participante['codigo'] == codigo for participante in dados_participante):
            return codigo
        else: 
            continue