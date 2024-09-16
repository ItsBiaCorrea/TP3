# Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro de dois mil e vinte e quatro".

def dia_para_texto(dia):
    """
    Converte um número representando o dia em uma string textual.

    Args:
        dia (int): O número do dia (1 a 31).

    Returns:
        str: A representação textual do dia.
    """
    dias_unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dias_dezenas = ["", "", "vinte", "trinta"]

    if dia < 10:
        return dias_unidades[dia]
    elif dia < 20:
        return ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"][dia - 10]
    else:
        dezena = dia // 10
        unidade = dia % 10
        if unidade == 0:
            return dias_dezenas[dezena]
        else:
            return f"{dias_dezenas[dezena]} e {dias_unidades[unidade]}"

def mes_para_texto(mes):
    """
    Converte um número representando o mês em uma string textual.

    Args:
        mes (int): O número do mês (1 a 12).

    Returns:
        str: A representação textual do mês.
    """
    meses = ["","janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return f"{meses[mes]}"

def ano_para_texto(ano):
    """
    Converte um número representando o ano em uma string textual.

    Args:
        ano (int): O ano em formato numérico.

    Returns:
        str: A representação textual do ano.
    """
    anos_mil = ["","mil", "dois mil"]
    anos_centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos", "quinhetos", "seiscentos", "setecentos", "oitocentos", "novecentos"]
    anos_dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    anos_unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    
    mil = ano // 1000
    centena = (ano % 1000)//100
    dezena = (ano % 100) // 10
    unidade = ano % 10
    texto_ano = anos_mil[mil]

    if centena > 0:
        if dezena == 0 and unidade == 0:
                texto_ano += f" e {anos_centenas[centena]}"
        else:
                texto_ano += f" e {anos_centenas[centena]}"
    if 10 <= ano % 100 < 20:
            texto_ano += f" e {['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove'][ano % 100 - 10]}"
    else:
        if dezena > 0:
            texto_ano += f" e {anos_dezenas[dezena]}"
        if unidade > 0:
            texto_ano += f" e {anos_unidades[unidade]}"

    return texto_ano.strip()

def verifica_entrada():
    """
    Solicita que o usuário insira uma data no formato 'dd/mm/aaaa', valida a entrada,
    e converte a data em uma string textual.

    Returns:
        None
    """
    while True:
        data = input("Entre com uma data válida (dd/mm/aaaa): ").strip()
        try:
            dia, mes, ano = map(int, data.split('/'))
            if 1 <= dia <= 31 and 1 <= mes <= 12 and 1000 <= ano <= 2999:
                print(f"{dia_para_texto(dia)} de {mes_para_texto(mes)} de {ano_para_texto(ano)}")
                break
            else:
                print("Data inválida. Tente novamente.")
        except ValueError:
            print("Formato inválido. Insira no formato 'dd/mm/aaaa'.")

verifica_entrada()