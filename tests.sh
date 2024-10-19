#!/bin/bash

# Lista de valores para passar como argumentos ao script Python
valores=(500 5000 50000)

# Loop para executar o Python Quick Sort com diferentes valores
for valor in "${valores[@]}"; do
    # Executa o script Python com o valor atual e redireciona a saída para um arquivo
    echo "Executando os algoritmos com $valor elementos"
    
    # Executa Quick Sort
    python3 quicksort.py $valor > quicksort_output_$valor.txt
    echo "Saída do Quick Sort salva em quicksort_output_$valor.txt"

    # Executa Bubble Sort
    python3 bubblesort.py $valor > bubblesort_output_$valor.txt
    echo "Saída do Bubble Sort salva em bubblesort_output_$valor.txt"

    # Executa Shell Sort
    python3 shellsort.py $valor > shellsort_output_$valor.txt
    echo "Saída do Shell Sort salva em shellsort_output_$valor.txt"
done

# Compacta os arquivos de saída em arquivos tar.gz
tar -czvf saidas_quicksort.tar.gz quicksort_output_*.txt
tar -czvf saidas_bubblesort.tar.gz bubblesort_output_*.txt
tar -czvf saidas_shellsort.tar.gz shellsort_output_*.txt

echo "Arquivos compactados com sucesso."
