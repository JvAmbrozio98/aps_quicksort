import time
import random
import sys

def ShellSort(lista):
    n = len(lista)
    gap = n // 2  # Inicialmente o gap é metade do tamanho da lista
    while gap > 0:
        for i in range(gap, n):  # Fazer a ordenação por inserção para os elementos com o gap atual
            temp = lista[i]
            j = i
            while j >= gap and lista[j - gap] > temp:  # Comparar elementos a gap posições de distância
                lista[j] = lista[j - gap]
                j -= gap
            lista[j] = temp
        gap //= 2  # Reduzir o gap pela metade
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
    print("Uso: python shellsort.py <tamanho_da_lista>")
    sys.exit(1)

# Pegar o tamanho da lista da linha de comando
try:
    tamanho_lista = int(sys.argv[1])
except ValueError:
    print("Por favor, forneça um número válido para o tamanho da lista.")
    sys.exit(1)

# Gera uma lista de números aleatórios com o tamanho fornecido
lista_numeros = [random.randint(0, 50000) for _ in range(tamanho_lista)]

# Medir o tempo de execução do Shell Sort
inicio_tempo = time.time()
lista_ordenada = ShellSort(lista_numeros)
fim_tempo = time.time()

# Verificar se a lista está ordenada
odenado(lista_ordenada)

# Exibir o tempo de execução
print(f"Tempo para ordenar: {fim_tempo - inicio_tempo:.9f} segundos")
