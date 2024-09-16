# Crie um programa que solicite um nome completo ao usuário e formate-o de forma que todas as palavras comecem com letra maiúscula e o restante seja minúsculo e exiba-o na tela.

def primeira_letra_maiuscula(text):
    """
    Formata o nome fornecido, garantindo que a primeira letra de cada palavra seja maiúscula e o restante seja minúsculo.

    Args:
        text (str): O nome completo do usuário.

    Returns:
        None. Exibe o nome formatado na tela.
    """
    partes_nome = text.split()
    nome = ' '.join(parte.capitalize() for parte in partes_nome)
    print(nome)

def validar_entrada():
    """
    Solicita que o usuário insira um nome completo. 
    Valida se a entrada não está vazia e, se válida, formata o nome e exibe-o.

    Returns:
        None. Continua solicitando o nome até que uma entrada válida seja fornecida.
    """
    while True:
        nome_completo = input("Entre com o seu nome completo: ").strip()
        if nome_completo == '':
            print("Valor inválido. Digite novamente.")
        else:
            primeira_letra_maiuscula(nome_completo)
            break

validar_entrada()

