# Mini projeto 2: Análise de Dados de Vendas 

# Uma empresa de comércio eletrônico deseja analisar os dados de vendas para entender melhor o comportamento dos clientes e otimizar as estratégias de marketing.

# Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário". O programa deve calcular e exibir o valor total das vendas para cada produto.
# Crie uma função que receba a lista de transações e retorne o produto mais vendido (baseado na quantidade) e o produto que gerou a maior receita total.
# Escreva um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário. Exiba os valores convertidos no formato monetário adequado.

lista_transacoes = ["001,Bicicleta,10,850.00",
"002,Notebook,5,3500.00",
"003,Cadeira_Gamer,15,650.00",
"004,Smartphone,20,2500.00",
"005,Teclado_Mecânico,30,350.00"]

def valor_total_produto(lista_transacoes):
    """
    Calcula e exibe o valor total das vendas para cada produto.

    Args:
        lista_transacoes (list): Lista de transações no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário".
    
    Returns:
        None
    """
    for item in lista_transacoes:
        produto = item.split(",")
        qtd = int(produto[2])
        uni = float(produto[3])
        valor_total = qtd * uni
        print(f"Valor Total do(a) {produto[1]}: R${valor_total}")

def produto_mais_vendido_e_maior_receita(lista_transacoes):
    """
    Identifica e exibe o produto mais vendido e o produto que gerou a maior receita total.

    Args:
        lista_transacoes (list): Lista de transações no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário".
    
    Returns:
        None
    """
    qtd_mais_vendido = 0
    mais_vendido = ''
    valor_maior_receita = 0
    maior_receita = ''
    for item in lista_transacoes:
        produto = item.split(",")
        qtd = int(produto[2])
        uni = float(produto[3])
        valor_total = qtd * uni
        if (qtd > qtd_mais_vendido):
            qtd_mais_vendido = qtd
            mais_vendido = produto[1]
        if (valor_total > valor_maior_receita):
            valor_maior_receita = valor_total
            maior_receita = produto[1]

    print(f"O produto mais vendido foi {mais_vendido} com {qtd_mais_vendido} itens vendidos.")
    print(f"O produto com maior receita foi {maior_receita} com R${valor_maior_receita:.2f}")

def converter_valores_totais(lista_transacoes, fator_conversao, simbolo_moeda='US$'):
    """
    Converte e exibe os valores totais de vendas para uma nova moeda.

    Args:
        lista_transacoes (list): Lista de transações no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário".
        fator_conversao (float): Fator de conversão para a nova moeda.
        simbolo_moeda (str): Símbolo da moeda para exibição (default é 'US$').
    
    Returns:
        None
    """
    for item in lista_transacoes:
        produto = item.split(',')
        nome_produto = produto[1]
        qtd = int(produto[2])
        uni = float(produto[3])
        valor_total = qtd * uni
        valor_convertido = valor_total * fator_conversao
        print(f"Valor Total convertido do(a) {nome_produto}: {simbolo_moeda} {valor_convertido:.2f}")

def verificar_entrada():
    """
    Solicita o fator de conversão ao usuário e realiza a conversão dos valores totais de vendas.

    Args:
        None
    
    Returns:
        None
    """
    while True:
        try:
            fator_conversao = float(input("Entre com um fator de conversão: "))
            simbolo_moeda = input("Entre com o símbolo da nova moeda (ex: US$, €): ")
            converter_valores_totais(lista_transacoes, fator_conversao, simbolo_moeda)
            break
        except ValueError:
            print("Valor inválido! Por favor, insira um número válido.")
        

valor_total_produto(lista_transacoes)
produto_mais_vendido_e_maior_receita(lista_transacoes)
verificar_entrada()