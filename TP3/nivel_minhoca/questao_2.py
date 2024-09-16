# Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.

texto_base = "Na noite silenciosa, as estrelas brilhavam e brilhavam, enquanto o vento sussurrava e sussurrava segredos para as árvores que balançavam e balançavam ao ritmo do universo."
def substituir_palavra(texto, palavra, palavra_substituta):
    """
    Substitui todas as ocorrências de 'palavra' no 'texto' pela 'palavra_substituta'.

    Args:
        texto (str): O texto original.
        palavra (str): A palavra a ser substituída.
        palavra_substituta (str): A palavra substituta.

    Returns:
        str: O texto modificado com as substituições feitas.
    """
    novo_texto = texto.replace(palavra, palavra_substituta)
    print("\nTexto modificado:\n" + novo_texto)

def validar_entrada():
    """
    Valida a entrada do usuário para garantir que uma palavra válida seja escolhida para substituição.
    """
    while True:
        print("\nTexto atual: \n" + texto_base)
        palavra = input("Entre com a palavra que deseja substituir: ").strip()
        if palavra == '':
            print("Valor inválido. Digite novamente.")
        elif palavra not in texto_base:
            print(f"A frase não contém a palavra '{palavra}'. Tente novamente.")
        else:
            nova_palavra = input("Entre com a palavra que será a substituta: ")
            if nova_palavra == '':
                print("Valor inválido. Digite novamente.")
            else: 
                substituir_palavra(texto_base, palavra, nova_palavra)
                break

validar_entrada()