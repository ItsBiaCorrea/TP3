# Mini projeto 4: Processamento de Textos Jurídicos 

# Um escritório de advocacia deseja automatizar parte do processo de análise de contratos, extraindo informações relevantes de documentos longos.

# Desenvolva um programa que receba o texto completo de um contrato e extraia todas as cláusulas que mencionem valores monetários. Os valores devem ser identificados e exibidos em uma lista separada.
# Implemente uma função que, dada uma lista de termos legais, verifique quantas vezes cada termo aparece no contrato e exiba as ocorrências em ordem decrescente de frequência.
import re

contrato = '''CONTRATO DE PRESTAÇÃO DE SERVIÇOS

CONTRATANTE:
Nome: João da Silva
CPF: 123.456.789-00
Endereço: Rua das Flores, 123, Bairro Jardim, Cidade Nova, Estado XYZ
Telefone: (11) 98765-4321
E-mail: joao.silva@email.com

CONTRATADA:
Nome: Soluções Tecnológicas ABC LTDA
CNPJ: 12.345.678/0001-99
Endereço: Avenida Principal, 456, Sala 301, Centro, Cidade Nova, Estado XYZ
Telefone: (11) 91234-5678
E-mail: contato@abcsolucoes.com

OBJETO DO CONTRATO:
A prestação de serviços de desenvolvimento de software personalizado, com base nas especificações fornecidas pela CONTRATANTE.

CLÁUSULA 1 – DO OBJETO
A CONTRATADA se compromete a desenvolver e entregar um sistema de software conforme as especificações técnicas acordadas com a CONTRATANTE, conforme descrito no Anexo I deste contrato.

CLÁUSULA 2 – DO PRAZO
O prazo para a entrega do software será de 90 (noventa) dias corridos, contados a partir da assinatura deste contrato. A CONTRATADA deverá comunicar imediatamente à CONTRATANTE qualquer imprevisto que possa impactar o prazo.

CLÁUSULA 3 – DO PREÇO E FORMA DE PAGAMENTO
3.1. O valor total pelo serviço prestado será de R$ 50.000,00 (cinquenta mil reais), dividido em três parcelas:
a) Primeira parcela: R$ 15.000,00 (quinze mil reais) no ato da assinatura deste contrato;
b) Segunda parcela: R$ 20.000,00 (vinte mil reais) até 30 dias após o início dos trabalhos;
c) Terceira parcela: R$ 15.000,00 (quinze mil reais) no momento da entrega final do sistema.

3.2. O pagamento será feito via transferência bancária para a conta corrente da CONTRATADA, conforme os dados fornecidos no Anexo II.

CLÁUSULA 4 – DAS OBRIGAÇÕES DAS PARTES
4.1. Obrigações da CONTRATADA:
a) Desenvolver o software conforme as especificações descritas no Anexo I;
b) Realizar ajustes e correções de erros apontados pela CONTRATANTE durante o período de testes;
c) Oferecer suporte técnico gratuito durante os 60 (sessenta) dias subsequentes à entrega final.

4.2. Obrigações da CONTRATANTE:
a) Fornecer todas as informações necessárias para o desenvolvimento do software;
b) Realizar os pagamentos nas datas acordadas;
c) Testar o sistema e informar qualquer erro ou falha no prazo de 30 dias após a entrega final.

CLÁUSULA 5 – DA RESCISÃO
Este contrato poderá ser rescindido por qualquer uma das partes, mediante aviso prévio de 15 (quinze) dias, nos seguintes casos:
a) Descumprimento de quaisquer das obrigações contratuais;
b) Atraso superior a 15 dias no pagamento das parcelas acordadas;
c) Inviabilidade técnica comprovada do desenvolvimento do software.

CLÁUSULA 6 – DA CONFIDENCIALIDADE
Ambas as partes concordam em manter em sigilo todas as informações confidenciais trocadas durante a execução deste contrato, inclusive códigos, especificações e dados da CONTRATANTE, sob pena de indenização por danos causados.

CLÁUSULA 7 – DA PROPRIEDADE INTELECTUAL
O código fonte e demais materiais criados durante o desenvolvimento do software serão de propriedade exclusiva da CONTRATANTE, após o pagamento integral do valor acordado. A CONTRATADA não terá qualquer direito sobre a utilização do sistema desenvolvido, salvo disposição em contrário por escrito.

CLÁUSULA 8 – DA GARANTIA
A CONTRATADA garante que o software estará livre de defeitos e falhas durante o período de garantia, que será de 60 (sessenta) dias a partir da data de entrega final. Durante esse período, a CONTRATADA se compromete a corrigir qualquer erro encontrado sem custo adicional para a CONTRATANTE.

CLÁUSULA 9 – DO ADITIVO CONTRATUAL
Qualquer modificação deste contrato deverá ser formalizada por meio de Termo Aditivo, que fará parte integrante deste contrato. O Termo Aditivo deverá ser assinado por ambas as partes.

CLÁUSULA 10 – DA CONFISSÃO DE DÍVIDA
Caso haja necessidade de renegociação de valores, a CONTRATANTE concorda em assinar um documento de Confissão de Dívida, se necessário, para formalizar a renegociação.

CLÁUSULA 11 – DA SOLIDARIEDADE
As partes reconhecem a Solidariedade nas obrigações de pagamento, responsabilizando-se mutuamente por qualquer inadimplemento.

CLÁUSULA 12 – DA NOTIFICAÇÃO EXTRAJUDICIAL
Qualquer notificação ou comunicação formal entre as partes deverá ser feita por Notificação Extrajudicial, que será considerada válida após o envio e recebimento.

CLÁUSULA 13 – DO FORO
Fica eleito o foro da Comarca de Cidade Nova, Estado XYZ, para dirimir quaisquer questões oriundas deste contrato, renunciando a qualquer outro, por mais privilegiado que seja.

E, por estarem assim justas e contratadas, as partes assinam o presente contrato em 2 (duas) vias de igual teor e forma, para um só efeito, juntamente com 2 (duas) testemunhas.

Cidade Nova, XX de XXXXXXX de 2024.

CONTRATANTE
João da Silva

CONTRATADA
Soluções Tecnológicas ABC LTDA

Testemunha 1
Nome: ___________________________
CPF: ____________________________

Testemunha 2
Nome: ___________________________
CPF: ____________________________'''

termos_legais = [
    "Aditivo Contratual",
    "Alienação Fiduciária",
    "Anuência",
    "Cessão de Direitos",
    "Cláusula Penal",
    "Condição Resolutiva",
    "Confissão de Dívida",
    "Contrato de Adesão",
    "Contrato Social",
    "Culpa In Vigilando",
    "Dolo",
    "Exequibilidade",
    "Força Maior",
    "Indenização",
    "Instrumento Público",
    "Litisconsórcio",
    "Notificação Extrajudicial",
    "Nulidade",
    "Obrigações Solidárias",
    "Perempção",
    "Prescrição",
    "Provisão",
    "Quórum",
    "Rescisão",
    "Solidariedade",
    "Sub-rogação",
    "Termo Aditivo",
    "Usufruto",
    "Vigência",
    "Vício Redibitório"
]

def extrair_valores_monetarios(texto):
    valores_monetarios = []
    contrato = texto.split("CLÁUSULA")
    for clausula in contrato:
        valores = re.findall(r'R\$ \d+(?:\.\d{3})*(?:,\d{2})?', clausula)
        if valores:
            valores_monetarios.append(valores)
    
    return valores_monetarios

def qtd_termos_legais(texto, termos):
    lista_total = []
    texto = texto.lower()
    for termo in termos:
        termo_lower = termo.lower()
        qtd = texto.count(termo_lower)
        lista_total.append([termo, qtd])
    
    lista_total = sorted(lista_total, key=lambda x: x[1], reverse=True)
    return lista_total

valores_monetarios = extrair_valores_monetarios(contrato)
termos_legais_qtd = qtd_termos_legais(contrato, termos_legais)

print("Valores mencionados no contrato:")
for clausula in valores_monetarios:
    print(clausula)

print("\nQuantidade de termos legais encontrados:")
for termo, qtd in termos_legais_qtd:
    print(f"{termo}: {qtd}")

