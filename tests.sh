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

echo "Arquivos compactados com sucesso."

# Criação dos buckets S3 com verificação
for bucket_name in "unip-aps-quicksort" "unip-aps-bubblesort" "unip-aps-shellsort"; do
    if aws s3api head-bucket --bucket $bucket_name 2>/dev/null; then
        echo "Bucket $bucket_name já existe, pulando criação..."
    else
        aws s3api create-bucket --bucket $bucket_name --region us-east-1
        echo "Bucket $bucket_name criado com sucesso."
    fi
done

# Upload dos arquivos para os respectivos buckets
aws s3 cp saidas_quicksort.tar.gz s3://unip-aps-quicksort/
aws s3 cp saidas_bubblesort.tar.gz s3://unip-aps-bubblesort/
aws s3 cp saidas_shellsort.tar.gz s3://unip-aps-shellsort/

echo "Arquivos enviados para os buckets no S3 com sucesso."
