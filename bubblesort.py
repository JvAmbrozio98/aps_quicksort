import random
import time
import sys

def BubbleSort(lista):
    n = len(lista)
    for i in range(n):  # Percorrer todos os elementos da lista
        for j in range(0, n-i-1):  # A última parte já estará ordenada, então o loop vai até n-i-1
            if lista[j] > lista[j+1]:
                # Troca se o elemento encontrado for maior que o próximo
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def odenado(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            print("não ordenado")
            break
    else:
        print("Lista está ordenada.")

# Verificar se um argumento foi passado
if len(sys.argv) != 2:
    print("Uso: python quicksort.py <tamanho_da_lista>")
    sys.exit(1)

# Pegar o tamanho da lista da linha de comando
try:
    tamanho_lista = int(sys.argv[1])
except ValueError:
    print("Por favor, forneça um número válido para o tamanho da lista.")
    sys.exit(1)

# Gera uma lista de números aleatórios
lista_numeros = [random.randint(0, 50000) for _ in range(tamanho_lista)]

# Medir o tempo de execução do Bubble Sort
inicio_tempo = time.time()
lista_ordenada = BubbleSort(lista_numeros)
fim_tempo = time.time()

# Verificar se a lista está ordenada
odenado(lista_ordenada)

# Exibir o tempo de execução
print(f"Tempo para ordenar: {fim_tempo - inicio_tempo:.9f} segundos")
