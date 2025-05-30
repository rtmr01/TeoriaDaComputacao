import random
import time
import statistics

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge process
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Função para medir tempo de execução
def medir_tempo(caso_func, n=1_000_000, repeticoes=3):
    tempos = []
    for _ in range(repeticoes):
        arr = caso_func(n)
        inicio = time.perf_counter()
        merge_sort(arr)
        fim = time.perf_counter()
        tempos.append(fim - inicio)
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    return media, desvio

# Casos de teste
def caso_melhor(n):
    return list(range(n))

def caso_pior(n):
    return list(range(n, 0, -1))

def caso_medio(n):
    arr = list(range(n))
    random.shuffle(arr)
    return arr

# Executa os testes
print("Testando Merge Sort com 1.000.000 de elementos (3 repetições por caso)...\n")
casos = {
    "Melhor Caso": caso_melhor,
    "Pior Caso": caso_pior,
    "Caso Médio": caso_medio,
}

# Exibe resultados em formato de tabela
print("{:<15} {:>12} {:>20}".format("Caso", "Média (s)", "Desvio Padrão (s)"))
print("-" * 50)
for nome, func in casos.items():
    media, desvio = medir_tempo(func)
    print("{:<15} {:>12.4f} {:>20.4f}".format(nome, media, desvio))
