# from dados.participantes import participantes as dados_participante
from dados.organizador import organizadores as dados_organizador
from dados.eventos import eventos as dados_evento
from random import randint
from collections import Counter #literalmente um contador
import ast ## abstract syntax tree, le codigos como se fosse string, assim executado codigos seguros, caso contrario ele exibe erro.
#no mesmo lugar do main para evitar conflito de importacao e reduzir as funcoes de leitura em uma

#funcao de leitura de arquivos
def ler(file_name):
    with open (file_name, 'r', encoding='utf-8') as file: 
        lendo = file.read().strip()
 
        ## Encontrando o inicio da lista de vdd pois esta considerando 'participantes =' como atributo inves de var 
        inicio_lista = lendo.find('[')
        total_dados = lendo[inicio_lista:]
        return ast.literal_eval(total_dados)

## Funcoes para geração de codigo de Participante e de Organizador

def gerar_codigoPA():
    dados_participante = ler('dados/participantes.py') ## para confirmar se o codigo esta vazio ou tem algo para comparar com o codigo de organizador
    while True: #garante que o código seja unico
        codigo = f'PA{randint(1000,9999)}'
        if not any(participante['codigo'] == codigo for participante in dados_participante):
            return codigo
        else: 
            continue

def gerar_codigoORG():
    dados_organizador = ler('dados/organizador.py') ## para confirmar se o codigo esta vazio ou tem algo para comparar com o codigo de participante
    while True: #garante que o código seja unico
        codigo = f'OR{randint(1000,9999)}'
        if not any(organizador['codigo'] == codigo for organizador in dados_organizador): #any() ao inves de utilizar um for para percorrer a lista toda eu uso o any() onde qualquer parametro que tiver dentro dele, se ja coincidir ele vai pegar
            return codigo
        else: 
            continue


def gerar_estatisticas():
    dados_evento = ler('dados/eventos.py')
    contagem = Counter()
    temas = Counter()
    
    for evento in dados_evento:
        tema = evento.get('tema', '').strip().lower() 
        temas[tema] += 1 #vai receber o tema que for igual para adicionar no counter()

        for codigo in evento.get('participantes', []):
            contagem[codigo] += 1 #mesma intencao para o codigo

    print('\nTemas mais frequentes:\n')
    for tema, qtd in temas.most_common(3):
        if qtd == 1:
            print(f'{tema.capitalize()}: aparece em {qtd} evento.') #capitalize serve para deixar a primeira letra em maiusculo.
        else:
            print(f'{tema.capitalize()}: aparece em {qtd} eventos.')
    print('\nParticipantes mais ativos:\n')        
    for codigo, qtd in contagem.most_common(3): #most_common vc pega o parametro para exibir os 3 mais frequentes, se trocar o numero, é o intervalo que ele vai exibir.
        if qtd == 1:
            print(f'O participante com código: {codigo}, participou em {qtd} evento.')
        else: 
            print(f'O participante com código: {codigo}, participou em {qtd} eventos.')