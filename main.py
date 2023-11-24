def processa_lista(valores):
    pass

def indice_menor(lista):
    pass

def organizar_alturas(lista):
    pass

def ler_valores():
    pass

def formatar_alturas(lista):
    pass

def intercalar_listas(lista1, lista2):
    pass

def lista_maior18(pessoas):
    pass

def q1(pessoas = {"Joao": 25, "Maria": 10}):
    # resultado = lista_maior18(pessoas)
    # return resultado
    def nomes_maiores_18(pessoas):
    maiores_18 = [nome for nome, idade in pessoas.items() if idade > 18]
    return sorted(maiores_18)

def q2(lista1 = [1, 3, 5], lista2 = [2, 4, 6, 8, 10]):
    # resultado_intercalado = intercalar_listas(lista1, lista2)
    # return resultado_intercalado
    def intercalar_listas(lista1, lista2):
    resultado = []
    tamanho = max(len(lista1), len(lista2))
    for i in range(tamanho):
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])
    return resultado
def intercalar_listas(lista1, lista2):
    resultado = []
    tamanho = max(len(lista1), len(lista2))
    for i in range(tamanho):
        if i < len(lista1):
            resultado.append(lista1[i])
        if i < len(lista2):
            resultado.append(lista2[i])
    return resultado
def q3(valores = None):
    #valores = ler_valores()
    # pares, impares = processa_lista(valores)
    # return pares, impares
def ler_valores():
    valores = []
    while True:
        valor = int(input("Digite um valor (0 para sair): "))
        if valor == 0:
            break
        valores.append(valor)
    return valores

def processa_lista(lista):
    pares = []
    impares = []
    for valor in lista:
        if valor % 2 == 0:
            if len(pares) == 5:
                pares.pop(0)
            pares.append(valor)
        else:
            if len(impares) == 5:
                impares.pop(0)
            impares.append(valor)
    return pares, impares

valores = ler_valores()
pares, impares = processa_lista(valores)

print("Lista de Pares:", pares)
print("Lista de Ímpares:", impares)
def q4(valores = None):
    #valores = ler_valores()
    # lista_ambrosina = organizar_alturas(valores)
    # return formatar_alturas(lista_ambrosina)
def ler_valores():
    valores = []
    while True:
        valor = float(input("Digite a altura de uma pessoa (0 para sair): "))
        if valor == 0:
            break
        valores.append(valor)
    return valores

def organizar_alturas(lista):
    lista.sort()
    return [lista[0], lista[2], lista[3], lista[1]]

def formatar_alturas(lista):
    return [f"{altura:.2f}" for altura in lista]

alturas = ler_valores()
organizadas = organizar_alturas(alturas)
formatadas = formatar_alturas(organizadas)

print(formatadas)





def main():
    pass

if __name__ == "__main__":
    main()


