# Mini Projeto 3: Gerenciamento de Senhas 

# Um administrador de sistemas precisa desenvolver uma ferramenta para gerenciar senhas de usuários em uma rede corporativa.

# Desenvolva uma função que gera senhas aleatórias seguras, atendendo aos critérios: mínimo de 8 caracteres, incluindo letras maiúsculas, minúsculas, números e caracteres especiais.
# Implemente uma função que receba uma senha do usuário e verifique se ela atende aos critérios de segurança mencionados. Para cada senha que não atender aos critérios, sugerir uma senha nova.
# Crie um programa que criptografa uma lista de senhas utilizando uma cifra de substituição (similar à cifra de Cesar) considerando todos os caracteres imprimíveis da tabela ASCII e armazene o resultado. Inclua uma função para descriptografar as senhas quando necessário.

import random 
from random import choice
import string
import re

lista_senhas = ["A$4kX9!w*H8z", "bR@5uP7#^xJ0", "m3^&X1!T#yL9", "Z!8qF$4rK@7b", "J1%wP6*D@xZ2"]

def gerar_senha():
    """
    Gera uma senha aleatória e segura.

    A senha gerada terá entre 8 e 20 caracteres, contendo uma combinação de letras maiúsculas,
    letras minúsculas, números e caracteres especiais.

    Returns:
        senha_segura (str): Uma senha gerada aleatoriamente.
    """
    comprimento = random.randint(8, 20)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_segura = ''
    for i in range(comprimento):
        senha_segura += choice(caracteres)
    return senha_segura

def verificar_senha(senha):
    """
    Verifica se a senha fornecida atende aos critérios de segurança.

    A senha deve ter pelo menos 8 caracteres, incluindo letras maiúsculas, letras minúsculas,
    números e caracteres especiais. Caso a senha não atenda aos critérios, uma nova senha
    aleatória será gerada e sugerida.

    Args:
        senha (str): A senha fornecida pelo usuário.

    Returns:
        senha (str): A senha original, se for válida, ou uma nova senha gerada caso seja inválida.
    """
    tamanho = len(senha)
    letras = re.search(r'[a-zA-Z]', senha)
    numeros = re.search(r'\d', senha)
    pontuacao = re.search(r'[!@#$%^&*(),.?":{}|<>-_]', senha)
    if tamanho == 8 and letras and numeros and pontuacao:
        lista_senhas.append(senha)
        return senha
    else: 
        print("Sua senha não atende aos critérios. Gerando uma senha para você.")
        nova_senha = gerar_senha()
        lista_senhas.append(nova_senha)
        return nova_senha

def criptografar(lista, chave=3):
    """
    Criptografa uma lista de senhas usando a cifra de Cesar.

    Cada caractere da senha será deslocado por uma quantidade de posições na tabela ASCII
    com base no valor da chave fornecida. Funciona para letras, números e caracteres especiais.

    Args:
        lista (list): A lista de senhas a ser criptografada.
        chave (int): O número de posições de deslocamento na tabela ASCII. O padrão é 3.

    Returns:
        lista_criptografada (list): A lista de senhas criptografadas.
    """
    lista_criptografada = []
    for senha in lista:
        senha_criptografada = ''
        for char in senha:
            if char.isalpha():
                deslocamento = 65 if char.isupper() else 97
                senha_criptografada += chr((ord(char) - deslocamento + chave) % 26 + deslocamento)
            elif char.isdigit(): 
                senha_criptografada += chr((ord(char) - ord('0') + chave) % 10 + ord('0'))
            else:
                senha_criptografada += chr((ord(char) - 32 + chave) % 95 + 32)
        lista_criptografada.append(senha_criptografada)
    
    return lista_criptografada

def descriptografar(lista, chave=3):
    """
    Descriptografa uma lista de senhas usando a cifra de Cesar.

    O processo de descriptografia é feito invertendo o valor da chave usado na criptografia.

    Args:
        lista (list): A lista de senhas a ser descriptografada.
        chave (int): O número de posições de deslocamento na tabela ASCII. O padrão é 3.

    Returns:
        senhas_descriptografadas (list): A lista de senhas descriptografadas.
    """
    senhas_descriptografadas = criptografar(lista, -chave)
    return senhas_descriptografadas

def verificar_entrada():
    """
    Interage com o usuário para verificar, criptografar ou descriptografar senhas.

    A função solicita que o usuário insira uma senha e, se a senha for válida, o programa
    permite que o usuário escolha criptografar ou descriptografar a senha. Caso a senha seja
    inválida, uma nova senha aleatória será gerada.

    Returns:
        None
    """
    while True:
        senha = input("Entre com a sua senha: ")
        if senha == '':
            print("Não pode estar vazio")
        else:
            verificar_senha(senha)
            escolha = int(input("O que deseja fazer? \n 1 - Criptografar sua Senha 2 - Descriptografar 3 - Encerrar o programa"))
            if escolha == 1:
                senhas_criptografadas = criptografar(lista_senhas)
                print("Senhas Criptografadas:")
                for senha in senhas_criptografadas:
                    print(senha)
            elif escolha == 2:
                print("Senhas Descriptografadas:")
                print(descriptografar(senhas_criptografadas))
            else:
                break

verificar_entrada();

