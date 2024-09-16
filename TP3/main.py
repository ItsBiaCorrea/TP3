def executar_questao(nivel, questao):
  caminhos = {
      "nivel_minhoca_1": './nivel_minhoca/questao_1.py',
      "nivel_minhoca_2": './nivel_minhoca/questao_2.py',
      "nivel_minhoca_3": './nivel_minhoca/questao_3.py',
      "nivel_minhoca_4": './nivel_minhoca/questao_4.py',
      "nivel_minhoca_5": './nivel_minhoca/questao_5.py',
      "nivel_cobrinha_1": './nivel_cobrinha/questao_1.py',
      "nivel_cobrinha_2": './nivel_cobrinha/questao_2.py',
      "nivel_python_1": './nivel_python/mini_projeto_1.py',
      "nivel_python_2": './nivel_python/mini_projeto_2.py',
      "nivel_python_3": './nivel_python/mini_projeto_3.py',
      "nivel_python_4": './nivel_python/mini_projeto_4.py'
  }

  chave = f"{nivel}_{questao}"

  exec(open(caminhos[chave]).read())

nivel = input("Digite o nível (ex: nivel_minhoca, nivel_cobrinha, nivel_python): ")
questao = input("Digite a questão: ")
executar_questao(nivel, questao)

# Usar docstring em todas as funções
# Usar exceçãp