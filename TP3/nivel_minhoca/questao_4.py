# Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

import re

def contagem_de_caracteres(frase):
    """
    Conta o número de caracteres na frase, desconsiderando os espaços em branco.

    Args:
        frase (str): A frase fornecida pelo usuário.

    Returns:
        None. Exibe a contagem de caracteres.
    """
    caracteres = frase.replace(" ", '')
    print(f"Essa frase tem {len(caracteres)} caracteres.")

def contagem_de_palavras(frase):
    """
    Conta o número de palavras na frase.

    Args:
        frase (str): A frase fornecida pelo usuário.

    Returns:
        None. Exibe a contagem de palavras.
    """
    palavras = frase.split()
    print(f"Essa frase tem {len(palavras)} palavras.")

def contagem_de_espacos(frase):
    """
    Conta o número de espaços em branco na frase.

    Args:
        frase (str): A frase fornecida pelo usuário.

    Returns:
        None. Exibe a contagem de espaços.
    """
    espacos = len(re.findall(r'\s', frase))
    print(f"Essa frase tem {espacos} espaços.")

def validar_entrada():
    """
    Solicita que o usuário insira uma frase e valida se a entrada não está vazia.
    Se a entrada for válida, conta e exibe o número de caracteres, palavras e espaços.

    Returns:
        None.
    """
    while True:
        frase = input("Entre com uma frase: ").strip()
        if frase == '':
            print("Valor inválido. Digite novamente.")
        else:
            contagem_de_caracteres(frase)
            contagem_de_palavras(frase)
            contagem_de_espacos(frase)
            break

validar_entrada()
