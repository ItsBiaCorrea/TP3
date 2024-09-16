# Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.
def calcular_soma_string(texto):
    """
    Calcula e imprime a soma dos dígitos em uma string numérica.

    Args:
        texto (str): A string numérica fornecida pelo usuário.

    Returns:
        None
    """
    soma = 0
    for numero in texto:
        soma += int(numero)
    print(f"A soma dos dígitos é: {soma}")

def verificar_se_so_numeros(texto):
    """
    Verifica se a string fornecida contém apenas dígitos.

    Args:
        texto (str): A string a ser verificada.

    Returns:
        bool: Retorna True se a string contiver apenas dígitos, False caso contrário.
    """
    return texto.isdigit()

def verifica_entrada():
    """
    Solicita que o usuário insira uma string numérica e calcula a soma dos dígitos se a entrada for válida.
    Valida se a entrada contém apenas números.

    Returns:
        None
    """
    while True:
        string = input("Entre com uma string numérica: ").strip()
        if verificar_se_so_numeros(string):
            calcular_soma_string(string)
            break
        else:
            print("Entrada inválida. Tente novamente.")

verifica_entrada()

