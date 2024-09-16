# Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.
import re

def calcular_string(texto):
    """
    Calcula e imprime o resultado dos dígitos e operadores em uma string numérica.

    Args:
        texto (str): A string numérica fornecida pelo usuário.

    Returns:
        None
    """
    texto_limpo = texto.replace(" ", "")
    try:
        resultado = eval(texto_limpo)
        print(f"O cálculo dos dígitos é: {resultado}")
    except Exception as e:
        print(f"Erro ao calcular a string: {e}")

def verificar_numeros_e_operacoes(texto):
    """
    Verifica se a string fornecida contém apenas dígitos e operadores matemáticos válidos.

    Args:
        texto (str): A string a ser verificada.

    Returns:
        bool: Retorna True se a string contiver apenas dígitos e operadores válidos, False caso contrário.
    """
    padrao = r'^[0-9+\-*/.\s]+$'
    return bool(re.match(padrao, texto))

def verifica_entrada():
    """
    Solicita que o usuário insira uma string numérica e calcula o resultado dos dígitos e operadores se a entrada for válida.
    Valida se a entrada contém apenas números e operadores válidos.

    Returns:
        None
    """
    while True:
        string = input("Entre com uma string numérica: ").strip()
        if verificar_numeros_e_operacoes(string):
            calcular_string(string)
            break
        else:
            print("Entrada inválida. Tente novamente.")

verifica_entrada()