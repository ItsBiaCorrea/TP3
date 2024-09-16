# Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro

# Na vida de um desenvolvedor e analista de sistemas a validação de dados é uma etapa extremamente importante que previne diversas dificuldades posteriores à coleta dos dados.

# Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
# CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
# E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
# Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.

import re

def verifica_cpf(cpf):
    """
    Verifica e formata um CPF.

    O CPF deve conter 11 dígitos numéricos. Qualquer outro caractere
    será removido. Se o CPF for válido (11 dígitos), ele será formatado
    no padrão "xxx.xxx.xxx-xx".

    Args:
        cpf (str): O CPF a ser verificado e formatado.

    Returns:
        str: O CPF formatado se válido, ou "Valor inválido!" se não for válido.
    """
    cpf_limpo = re.sub(r'\D', '', cpf)
    if len(cpf_limpo) != 11:
        return "Valor Inválido"
    else:
        cpf_formatado = f"{cpf_limpo[:3]}.{cpf_limpo[3:6]}.{cpf_limpo[6:9]}-{cpf_limpo[9:]}"
        return cpf_formatado
    
def verifica_email(email):
    """
    Verifica e formata um e-mail.

    O e-mail deve seguir o padrão de formato "nome@dominio.com".
    Se for válido, o e-mail é retornado em letras minúsculas.

    Args:
        email (str): O e-mail a ser verificado e formatado.

    Returns:
        str: O e-mail formatado se válido, ou "Valor Inválido" se não for válido.
    """
    verificar = r'^[a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    if re.match(verificar, email):
        email_formatado = email.lower()
        return email_formatado
    else:
        return "Valor Inválido"
    
def verifica_telefone(telefone):
    """
    Verifica e formata um número de telefone.

    O número de telefone pode conter 10 ou 11 dígitos. Caracteres não
    numéricos serão removidos. Se for válido, será retornado no formato
    "(XX) XXXXX-XXXX" para números com 11 dígitos ou "(XX) XXXX-XXXX" para números com 10 dígitos.

    Args:
        telefone (str): O número de telefone a ser verificado e formatado.

    Returns:
        str: O número de telefone formatado se válido, ou "Valor inválido!" se não for válido.
    """
    telefone_limpo = re.sub(r'\D', '', telefone) 
    if len(telefone_limpo) not in [10, 11]:
        return "Valor Inválido"
    else:
        telefone_inteiro = int(telefone_limpo)
        print("Número me formato inteiro: " + telefone_inteiro)
        if len(telefone_limpo) == 11:
            telefone_formatado = f"({telefone_limpo[:2]}){telefone_limpo[2:7]}-{telefone_limpo[7:]}"
        else:
            telefone_formatado = f"({telefone_limpo[:2]}){telefone_limpo[2:6]}-{telefone_limpo[6:]}"
        return telefone_formatado

def validar_entrada():
    """
    Solicita ao usuário que insira CPF, e-mail e telefone, e os valida.

    O programa pede ao usuário para inserir os dados e valida cada entrada
    utilizando as funções `verifica_cpf`, `verifica_email` e `verifica_telefone`.
    Os dados são exibidos formatados se forem válidos, e o loop continua
    até que todas as entradas sejam válidas.

    Returns:
        None
    """
    while True:
        cpf = input("Entre com o seu CPF: ")
        email = input("Entre com o seu e-mail: ")
        telefone = input("Entre com o seu telefone: ")

        email_validado = verifica_email(email)
        cpf_validado = verifica_cpf(cpf)
        telefone_validado = verifica_telefone(telefone)

        if email_validado != "Valor Inválido" and cpf_validado != "Valor Inválido" and telefone_validado != "Valor Inválido":
            print(f"CPF: {cpf_validado}")
            print(f"E-mail: {email_validado}")
            print(f"Telefone: {telefone_validado}")
            break
        else:
            print("Entrada Inválida, por favor tente novamente.")

validar_entrada()
