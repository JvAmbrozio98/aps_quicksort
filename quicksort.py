import random
import time
import argparse

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Escolhe o pivô
        left = [x for x in arr if x < pivot]  # Elementos menores que o pivô
        middle = [x for x in arr if x == pivot]  # Elementos iguais ao pivô
        right = [x for x in arr if x > pivot]  # Elementos maiores que o pivô
        return quick_sort(left) + middle + quick_sort(right)

def main():
    # Parser para argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Ordenação Quick Sort")
    parser.add_argument(
        "size", type=int, help="Tamanho da lista a ser gerada para ordenação"
    )
    args = parser.parse_args()

    # Gera a lista com o tamanho informado pelo usuário
    data = [random.randint(1, 10000000) for _ in range(args.size)]

    start_time = time.time()
    sorted_data = quick_sort(data)
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Tempo de execução do Quick Sort: {execution_time:.6f} segundos")
    print("Dados ordenados:")
    print(sorted_data)

if __name__ == "__main__":
    main()
