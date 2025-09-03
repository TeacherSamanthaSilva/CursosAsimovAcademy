# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random

# Definição dos naipes e valores das cartas
naipes = ["♠", "♥", "♦", "♣"]
valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

def gerar_baralho(num_baralhos=1, incluir_coringas=False, embaralhar=True):
    """
    Gera um baralho de cartas.

    Args:
        num_baralhos (int): Número de baralhos a serem gerados (1, 2, etc.).
        incluir_coringas (bool): Se True, inclui coringas no baralho.
        embaralhar (bool): Se True, embaralha o baralho.

    Returns:
        list: Uma lista de cartas (strings).
    """
    baralho = []
    for _ in range(num_baralhos):
        for naipe in naipes:
            for valor in valores:
                baralho.append(f"{valor}{naipe}")
        if incluir_coringas:
            baralho.extend(["Cor" for _ in range(num_baralhos * 2)])  # Adiciona 2 coringas por baralho
    if embaralhar:
        random.shuffle(baralho)
    return baralho

def mostrar_baralho(baralho):
    """
    Exibe o baralho.

    Args:
        baralho (list): Uma lista de cartas.
    """
    print(f"O baralho tem {len(baralho)} cartas:")
    print(", ".join(baralho))

def dar_as_cartas(baralho, num_jogadores, cartas_por_jogador):
    """
    Distribui as cartas do baralho entre os jogadores.

    Args:
        baralho (list): O baralho de cartas.
        num_jogadores (int): O número de jogadores.
        cartas_por_jogador (int): O número de cartas que cada jogador recebe.

    Returns:
        dict: Um dicionário onde as chaves são os jogadores (1, 2, 3, ...)
              e os valores são as mãos de cada jogador (listas de cartas).
    """
    if num_jogadores * cartas_por_jogador > len(baralho):
        print("Não há cartas suficientes para todos os jogadores.")
        return None

    jogadores = {}
    for i in range(1, num_jogadores + 1):
        jogadores[i] = []
        for _ in range(cartas_por_jogador):
            carta = baralho.pop(0)  # Remove a primeira carta do baralho
            jogadores[i].append(carta)
    return jogadores

def mostrar_jogadores(jogadores):
    """
    Exibe as mãos dos jogadores.

    Args:
        jogadores (dict): Um dicionário com as mãos dos jogadores.
    """
    if jogadores is None:
        return
    for jogador, mao in jogadores.items():
        print(f"Jogador {jogador} tem {len(mao)} cartas: {', '.join(mao)}")

# Testando as funções

# 1. Gerar e exibir o baralho
meu_baralho = gerar_baralho(num_baralhos=1, incluir_coringas=False, embaralhar=True)
mostrar_baralho(meu_baralho)

print("-" * 20)

# 2. Distribuir as cartas
num_jogadores = 4
cartas_por_jogador = 5
maos_jogadores = dar_as_cartas(meu_baralho, num_jogadores, cartas_por_jogador)

# 3. Exibir o baralho após a distribuição
print("-" * 20)
mostrar_baralho(meu_baralho)

# 4. Exibir as mãos dos jogadores
print("-" * 20)
mostrar_jogadores(maos_jogadores)
