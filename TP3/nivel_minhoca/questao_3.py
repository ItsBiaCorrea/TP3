# Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.
import re

def definir_palavra_mais_longa(frase):
    """
    Encontra e retorna a palavra mais longa em uma frase, desconsiderando a pontuação.

    Args:
        frase (str): A frase fornecida pelo usuário.

    Returns:
        str: A palavra mais longa da frase.
    """
    frase_limpa = re.sub(r'[^\w\s]', '', frase)
    palavras = frase_limpa.split()
    maior_palavra = ''
    for palavra in palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    print(f'A maior palavra é {maior_palavra}')

def validar_entrada():
    """
    Solicita que o usuário insira uma frase. 
    Valida se a entrada não está vazia.

    Returns:
        None. Continua solicitando a frase até que uma entrada válida seja fornecida.
    """
    while True:
        frase = input("Entre com uma frase: ").strip()
        if frase == '':
            print("Valor inválido. Digite novamente.")
        else:
            definir_palavra_mais_longa(frase)
            break

validar_entrada()

